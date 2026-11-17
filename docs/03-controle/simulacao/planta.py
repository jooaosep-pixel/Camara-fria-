# -*- coding: utf-8 -*-
"""Modelo termico e eletrico simples da camara + banco de gelo + sol.

Numeros do doc 01 (versao com 87,3 kWh/dia, ar novo de 30 m3/h e agua a 6 C
das 17 h as 7 h). E um modelo de parametros concentrados para testar a
LOGICA, nao para redimensionar o projeto: o dimensionamento e o do doc 01.
Cada parametro esta marcado com a origem.
"""

import math

# ---- parametros (doc 01 salvo indicacao) -----------------------------------
UA_INV = 33.0          # W/K, reefer usado (doc 01, 1.2)
C_AR = 300e3           # J/K, ar + forro interno [SUPOSTO para o modelo]
C_FRUTA = 3940.0       # J/kg.K: 3,77 kJ/kg.K + embalagem 90 kg/t x 1,9 (doc 01, 3.1)
HA_POR_T = 130.9       # W/K por tonelada -> constante de tempo de 8 h (doc 01, 3.1)
RESP_W_T = 83.0        # W/t a 10 C, fator 2,5 por 10 C, teto a 38 C (doc 01, 2.1)
CO2_ML_KG_H = 17.0     # ml/kg.h a 12-13 C (doc 01, 11.2)
V_AR_LIVRE = 15.0      # m3 (doc 01, 11.2)
K_SERP = 940.0         # W/K com ventilador a 100 % (8,5 kW a 12/3 C, doc 01, 9.3)
VENT_W = 238.0         # W dos 2 ventiladores a 100 % (doc 01, 12.1)
UA_BANCO = 3.5         # W/K perdas do banco (doc 01, 3.1)
FRACAO_UTIL = 0.90     # do gelo [SUPOSTO; achado N8]
AGUA_POR_KG_GELO = 1.7 # kg de agua no tanque por kg de gelo nominal [SUPOSTO]
RHO_CP_AR = 0.335      # W/(K.m3/h)
FATOR_LAT_AR_NOVO = 1.25   # latente do ar novo: 30 m3/h -> 6,6 kWh/dia a 41 C (doc 01)
FATOR_LAT_PORTA = 3.0      # porta: ~4 kWh/dia no dia de projeto (doc 01, 3.2) [ajuste]
PESSOAS_LUZ_W = 290.0      # 7 h-14 h -> 2,0 kWh/dia (doc 01, 3.2)
NASCER, POR = 5.5, 17.67   # doc 01, secao 4
EXP_SOL = 1.3
PR = 0.75
PSH_BAR = 18.0         # pressostato de alta de HARDWARE, rearme manual [VALIDAR]
INV_CORTE_SOC = 20.0   # Rota A: contato seco do inversor hibrido corta compressores (hardware)


def _media_sin_exp():
    n = 2000
    s = 0.0
    for k in range(n):
        x = math.pi * (k + 0.5) / n
        s += math.sin(x) ** EXP_SOL
    return s / n


_MEDIA = _media_sin_exp()


def irradiancia(h, H_kwh_m2):
    if h <= NASCER or h >= POR:
        return 0.0
    L = POR - NASCER
    s = math.sin(math.pi * (h - NASCER) / L) ** EXP_SOL
    return H_kwh_m2 * 1000.0 * s / (L * _MEDIA)


def t_externa(h, tmin, tmax):
    mid = (tmin + tmax) / 2.0
    amp = (tmax - tmin) / 2.0
    return mid - amp * math.cos(2 * math.pi * (h - 3.0) / 24.0)


def psat_rel(tc):
    """Pressao relativa (bar) de saturacao do R134a (mesmo ajuste da logica)."""
    return math.exp(10.826 - 2665.5 / (tc + 273.15)) - 0.97


def cop(arq, text):
    # pontos do doc 01, 5.1; interpolacao quadratica
    if arq == "b":
        pts = ((27.0, 2.90), (34.0, 2.38), (41.0, 1.98))
    else:
        pts = ((27.0, 2.45), (34.0, 2.03), (41.0, 1.70))
    (x0, y0), (x1, y1), (x2, y2) = pts
    x = text
    return (y0 * (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))
            + y1 * (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))
            + y2 * (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1)))


def resp_w(m_kg, T):
    return m_kg / 1000.0 * RESP_W_T * 2.5 ** ((min(T, 38.0) - 10.0) / 10.0)


class Planta:
    def __init__(self, cfg, gelo_ini=0.8, starlink_w=30.0, bat_ini=0.9):
        self.cfg = cfg
        self.rota = cfg["rota"]["rota"]
        self.arq = cfg["arq"]["nome"]
        self.kwp = cfg["kwp"]
        self.cap_kwh = cfg["gelo_kg"] * 334.0 / 3600.0 * FRACAO_UTIL
        self.E = gelo_ini * self.cap_kwh
        self.Tb = 0.5
        self.m_agua = cfg["gelo_kg"] * AGUA_POR_KG_GELO
        self.Tar = 12.0
        self.lotes = [{"m": 5000.0, "T": 12.5, "t": -1e9}]   # estoque inicial
        self.co2 = 0.30
        self.bat_cap = cfg["rota"]["bateria_kwh_util"]
        self.bat = bat_ini * self.bat_cap
        self.starlink_w = starlink_w
        self.psh_aberto = [False] * cfg["rota"]["n_comp"]
        self.falha_inv = [0.0] * cfg["rota"]["n_comp"]
        self.falha_vent_cond = False
        self.apagao = False
        self.aux_kw = 0.36
        self.carga_kw = 0.5
        self.pv_kw = 0.0
        self.G = 0.0
        self.Text = 30.0
        self.porta_alta = False
        # acumuladores
        self.acc = {}

    # ------------------------------------------------------------------
    def somar(self, k, v):
        self.acc[k] = self.acc.get(k, 0.0) + v

    def tt2(self):
        return self.lotes[0]["T"]

    def tt3(self):
        return self.lotes[-1]["T"]

    def lt1(self):
        return 100.0 * self.E / self.cap_kwh

    def receber(self, kg, T, t):
        if kg > 0:
            self.lotes.append({"m": kg, "T": T, "t": t})

    def expedir(self, kg):
        # sai a fruta mais antiga (estoque)
        st = self.lotes[0]
        st["m"] = max(500.0, st["m"] - kg)

    def juntar_lotes(self, t):
        st = self.lotes[0]
        novos = [st]
        for l in self.lotes[1:]:
            if t - l["t"] > 48 * 3600:
                M = st["m"] + l["m"]
                st["T"] = (st["m"] * st["T"] + l["m"] * l["T"]) / M
                st["m"] = M
            else:
                novos.append(l)
        self.lotes = novos

    # ------------------------------------------------------------------
    def entradas(self, t, hora, dia, sensores_falhos=(), com_inversor=True):
        e = {"t": t, "hora": hora, "dia": dia,
             "TT1": self.Tar, "TT2": self.tt2(), "TT3": self.tt3(),
             "UR1": 88.0, "CO2": self.co2, "TT4": self.Tb,
             "TT5": max(self.Tb, 3.0), "LT1": self.lt1(), "TT6": self.Text,
             "G": self.G, "EI1": self.lt1() >= 101.0,
             "porta": False, "botao_entrada": False, "pessoa_presa": False,
             "gas": False, "fluxo_ok": True, "com_inversor": com_inversor,
             "aux_kw": self.aux_kw, "carga_kw": self.carga_kw, "pv_kw": self.pv_kw,
             "soc": 100.0 * self.bat / self.bat_cap,
             "T_glicol": -6.0 if self.acc.get("_rodando", 0) else max(self.Tb, 0.0),
             "comp": []}
        if self.rota == "A" and not com_inversor:
            e["soc"] = None
            e["pv_kw"] = None
            e["carga_kw"] = None
        for i in range(self.cfg["rota"]["n_comp"]):
            rod = self._rod[i] if hasattr(self, "_rod") else False
            sol = self._sol[i] if hasattr(self, "_sol") else False
            if rod and sol:
                pt1 = psat_rel(-7.0 if self.arq == "b" else -10.5)
            elif rod:
                pt1 = 0.8
            else:
                pt1 = psat_rel(max(self.Tb, 0.0))
            tc = self.Text + (10.0 if rod else 0.0) + (14.0 if (rod and self.falha_vent_cond) else 0.0)
            e["comp"].append({"PT1": pt1, "PT2": psat_rel(tc),
                              "cadeia_ok": not self.psh_aberto[i],
                              "inversor_falha": self.falha_inv[i] > 0})
        for k in sensores_falhos:
            if k in e:
                e[k] = None
        return e

    # ------------------------------------------------------------------
    def passo(self, t, hora, dt, s, clima, recepcao_ativa):
        tmin, tmax, H = clima
        self.Text = t_externa(hora, tmin, tmax)
        self.G = irradiancia(hora, H)
        pv_tot = self.kwp * self.G / 1000.0 * PR
        n = self.cfg["rota"]["n_comp"]
        r = self.cfg["rota"]

        if self.apagao:
            s = None
        # ---- cargas auxiliares (kW)
        if s is None:   # sem energia nenhuma: tudo parado
            f, p2, ar, agua = 0.0, False, 0.0, 3.0
            liga = [False] * n
            sol = [False] * n
            freq = [0.0] * n
            carter = [False] * n
            bat_comp = False
            bomba_banco = False
            starlink = False
            ctrl_w = 0.0
        else:
            f = s["vent_serp"]
            p2 = s["bomba_p2"]
            ar = s["ar_novo_m3h"]
            agua = s["agua_sp"]
            liga = [c["liga"] for c in s["comp"]]
            sol = [c["solenoide"] for c in s["comp"]]
            freq = [c["freq"] for c in s["comp"]]
            carter = [c["carter"] for c in s["comp"]]
            bat_comp = s["bat_comp"]
            bomba_banco = s["bomba_banco"]
            starlink = s["starlink"]
            ctrl_w = 15.0
        # hardware: PSH aberto ou contato do inversor hibrido impedem o compressor
        for i in range(n):
            if self.psh_aberto[i]:
                liga[i] = False
            if self.falha_inv[i] > 0:
                liga[i] = False
                self.falha_inv[i] -= dt
        if self.rota == "A" and 100.0 * self.bat / self.bat_cap < INV_CORTE_SOC:
            liga = [False] * n
        vent_w = VENT_W * f ** 3 if (p2 or s is None and f > 0) else VENT_W * f ** 3
        aux_int = (vent_w + (25.0 + 85.0 * f if p2 else 0.0) + ar / 2.0 + ctrl_w
                   + (self.starlink_w if starlink else 0.0)
                   + 50.0 * sum(1 for c in carter if c)
                   + (40.0 if recepcao_ativa else 0.0)) / 1000.0
        aux_dia = 0.15 * sum(1 for x in liga if x) + ((0.26 if self.arq == "a" else 0.06) if bomba_banco else 0.0)

        # ---- compressores
        cop_v = cop(self.arq, self.Text)
        p_el = [0.0] * n
        bat_saida_comp = 0.0
        if self.rota == "B":
            grp = self.kwp / n * self.G / 1000.0 * PR
            # carregador/inversor de 48 V no grupo 1: atende auxiliares e carrega a bateria
            soc = self.bat / self.bat_cap
            falta = (self.bat_cap - self.bat)
            carga_bat = min(1.5, falta * 3600.0 / dt) if falta > 0.01 else 0.0
            pedido = aux_int + aux_dia + carga_bat
            carregador = min(grp, pedido)
            self.aux_kw = carregador
            disp = [grp - carregador] + [grp] * (n - 1)
            for i in range(n):
                if not liga[i]:
                    continue
                pf = r["p_max_kw"] * max(freq[i], r["f_min_hz"]) / r["f_max_hz"]
                if i == 0 and bat_comp:
                    pb = r["p_min_kw"]
                    p_el[i] = pb
                    bat_saida_comp = pb / 0.9
                    continue
                if disp[i] < 0.8 * r["p_max_kw"] * r["f_min_hz"] / r["f_max_hz"]:
                    # inversor de bombeamento nao sustenta: desarma (protecao do proprio inversor)
                    self.falha_inv[i] = 60.0
                    p_el[i] = 0.0
                    self.somar("desarmes_inversor", 1)
                    continue
                p_el[i] = min(pf, disp[i])
            # balanco da bateria de 48 V
            sobra_bat = carregador - (aux_int + aux_dia)
            if sobra_bat >= 0:
                self.bat += sobra_bat * 0.95 * dt / 3600.0
            else:
                self.bat += sobra_bat / 0.95 * dt / 3600.0
            self.bat -= bat_saida_comp * dt / 3600.0
            self.somar("pv_usado_kwh", (carregador + sum(p_el) - (p_el[0] if bat_comp else 0)) * dt / 3600.0)
        else:
            for i in range(n):
                if liga[i]:
                    p_el[i] = r["p_unidade_kw"]
            carga = aux_int + aux_dia
            self.carga_kw = carga
            self.pv_kw = pv_tot
            liq = pv_tot - carga - sum(p_el)
            if liq >= 0:
                cab = (self.bat_cap - self.bat) * 3600.0 / dt / 0.95
                usado = min(liq, cab)
                self.bat += usado * 0.95 * dt / 3600.0
                self.somar("pv_usado_kwh", (pv_tot - liq + usado) * dt / 3600.0)
            else:
                self.bat += liq / 0.95 * dt / 3600.0
                self.somar("pv_usado_kwh", pv_tot * dt / 3600.0)
        self.bat = min(self.bat, self.bat_cap)
        if self.bat <= 0.0:
            self.bat = 0.0
            if not self.apagao:
                self.somar("apagoes", 1)
            self.apagao = True
        elif self.apagao and self.bat / self.bat_cap > 0.05:
            self.apagao = False
        self.somar("pv_disp_kwh", pv_tot * dt / 3600.0)
        self.somar("comp_kwh", sum(p_el) * dt / 3600.0)

        # PSH de hardware (independente do controlador)
        for i in range(n):
            if p_el[i] > 0:
                tc = self.Text + 10.0 + (14.0 if self.falha_vent_cond else 0.0)
                if psat_rel(tc) >= PSH_BAR:
                    self.psh_aberto[i] = True
                    p_el[i] = 0.0
        self._rod = [p > 0 for p in p_el]
        self._sol = sol
        self.acc["_rodando"] = 1 if any(self._rod) else 0

        frio = sum(p_el) * cop_v * 1000.0  # W
        # ---- banco: agua da serpentina
        tw = max(self.Tb, agua)
        q_serp = 0.0
        if p2 and s is not None:
            q_serp = max(0.0, K_SERP * f ** 0.8 * (self.Tar - tw))
        elif s is None and self.apagao is False and f > 0:
            q_serp = max(0.0, K_SERP * f ** 0.8 * (self.Tar - tw))
        q_banco = UA_BANCO * (self.Text - self.Tb)
        liq_banco = q_serp + q_banco - frio      # W retirados do banco
        dE = -liq_banco * dt / 3.6e6             # kWh
        if self.Tb > 0.5 and dE > 0:
            # primeiro esfria a agua
            dT = dE * 3.6e6 / (self.m_agua * 4186.0)
            self.Tb = max(0.5, self.Tb - dT)
        else:
            self.E += dE
            if self.E > self.cap_kwh:
                self.E = self.cap_kwh
            if self.E < 0:
                self.Tb += (-self.E) * 3.6e6 / (self.m_agua * 4186.0)
                self.E = 0.0
        self.somar("frio_kwh", frio * dt / 3.6e6)
        self.somar("serp_kwh", q_serp * dt / 3.6e6)

        # ---- camara
        inf = 15.4 if recepcao_ativa else 3.2      # m3/h equivalentes de porta
        q_inv = UA_INV * (self.Text - self.Tar)
        q_porta = inf * RHO_CP_AR * FATOR_LAT_PORTA * (self.Text - self.Tar)
        q_arn = ar * RHO_CP_AR * FATOR_LAT_AR_NOVO * (self.Text - self.Tar)
        q_pes = PESSOAS_LUZ_W if recepcao_ativa else 0.0
        q_fr = 0.0
        g_co2 = 0.0
        for l in self.lotes:
            ha = HA_POR_T * l["m"] / 1000.0
            q = ha * (l["T"] - self.Tar)
            r_w = resp_w(l["m"], l["T"])
            l["T"] += (r_w - q) * dt / (l["m"] * C_FRUTA)
            q_fr += q
            g_co2 += l["m"] * CO2_ML_KG_H * 1e-6 * 2.5 ** ((min(l["T"], 38.0) - 12.5) / 10.0)
        dQ = q_inv + q_porta + q_arn + q_pes + vent_w + q_fr - q_serp
        self.Tar += dQ * dt / C_AR
        # CO2 (% vol)
        vent_tot = ar + inf
        frac = self.co2 / 100.0
        frac += (g_co2 - vent_tot * (frac - 0.0004)) * dt / 3600.0 / V_AR_LIVRE
        self.co2 = max(0.04, frac * 100.0)
        self.somar("ar_novo_kwh", q_arn * dt / 3.6e6)
        self.somar("carga_kwh", (q_inv + q_porta + q_arn + q_pes + vent_w) * dt / 3.6e6)
        self.somar("aux_noite_kwh", aux_int * dt / 3600.0 if (hora >= 17 or hora < 7) else 0.0)
