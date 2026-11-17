# -*- coding: utf-8 -*-
"""Logica de controle da camara fria solar com banco de gelo.

ESTE ARQUIVO E O MESMO no controlador (MicroPython no ESP32) e na simulacao
(CPython). Nao usa nenhuma biblioteca alem de 'math'. Nao le pinos nem rede:
recebe um dicionario de entradas e devolve um dicionario de saidas. Quem le
os sensores e aciona os reles e o main_esp32.py (placa) ou o simulador.

Funcoes de seguranca NAO dependem deste arquivo: pressostato de alta (PSH),
pressostato de baixa (PSL), termostato de glicol (TSL), chave de fluxo,
protetor do motor, botao de emergencia e detector de gas abrem a cadeia de
seguranca em hardware (ver LEIAME, secao 6). O software so le essa cadeia
para avisar e para nao insistir.

Convencao de entradas (None = sensor em falha ou fora da faixa):
  t (s, monotono), hora (0-24), dia (inteiro)
  TT1 ar da camara, TT2 polpa do estoque, TT3 polpa do lote novo,
  UR1, CO2 (% vol), TT4 agua saida do banco, TT5 agua p/ serpentina,
  LT1 (% do gelo util), TT6 ar externo, G irradiancia no plano (W/m2),
  EI1 (bool, fim de carga por espessura), porta (bool aberta),
  botao_entrada (bool), pessoa_presa (bool), gas (bool),
  soc (% da bateria; Rota B = bateria 48 V), pv_kw e carga_kw (Rota A,
  lidos do inversor hibrido), aux_kw (Rota B), com_inversor (bool),
  T_glicol (arquitetura a), fluxo_ok (bool),
  comp: lista com {PT1, PT2 (bar rel), cadeia_ok, inversor_falha}
"""

import math

VERSAO = "1.0"

PARADO = "PARADO"
RODANDO = "RODANDO"
RECOLHENDO = "RECOLHENDO"
BLOQUEADO = "BLOQUEADO"
TRAVADO = "TRAVADO"  # so sai com reset manual

AV_NORMAL = "RECEBER_NORMAL"
AV_MEIA = "MEIA_CARGA"
AV_NAO = "NAO_RECEBER"

# Faixas validas dos sensores (fora disso = falha)
FAIXAS = {
    "TT1": (-20.0, 60.0), "TT2": (-20.0, 60.0), "TT3": (-20.0, 60.0),
    "TT4": (-20.0, 60.0), "TT5": (-20.0, 60.0), "TT6": (-10.0, 60.0),
    "UR1": (0.0, 100.0), "CO2": (0.0, 5.0), "LT1": (-5.0, 110.0),
    "G": (0.0, 1500.0), "soc": (0.0, 100.0), "T_glicol": (-30.0, 40.0),
}


def tsat_r134a(p_rel_bar):
    """Temperatura de saturacao (C) a partir da pressao relativa (bar).
    Ajuste de 2 pontos do doc 01 (5.1): -7 C = 2,25 bar abs; 51 C = 13,51.
    Para R513A usar a tabela do gas [VALIDAR]."""
    pabs = p_rel_bar + 0.97
    if pabs <= 0.05:
        return -60.0
    return 2665.5 / (10.826 - math.log(pabs)) - 273.15


def limitar(x, a, b):
    if x < a:
        return a
    if x > b:
        return b
    return x


class Compressor:
    """Maquina de estados de um compressor com as protecoes de tempo."""

    def __init__(self, idx, cc, t0):
        self.idx = idx
        self.cc = cc
        self.estado = PARADO
        self.t_ligou = -1e9
        # Ao energizar o controlador conta como "acabou de parar":
        # depois de uma falta de energia o compressor espera o minimo desligado.
        self.t_desligou = t0
        self.t_rec = 0.0
        self.partidas = []
        self.bloq_ate = 0.0
        self.bloqueios = []
        self.motivo = ""
        self.freq = 0.0
        self.paradas_forcadas = 0
        self.paradas_curtas = 0  # paradas forcadas antes do minimo ligado
        self.modo_cheio = False

    def partidas_ultima_hora(self, t):
        self.partidas = [p for p in self.partidas if t - p < 3600]
        return len(self.partidas)

    def pode_partir(self, t):
        if self.estado != PARADO:
            return False
        if t - self.t_desligou < self.cc["min_desligado_s"]:
            return False
        if self.partidas_ultima_hora(t) >= self.cc["max_partidas_hora"]:
            return False
        return True

    def min_ligado(self):
        if self.modo_cheio:
            return self.cc["min_ligado_banco_cheio_s"]
        return self.cc["min_ligado_s"]

    def bloquear(self, t, motivo, dur):
        self.bloqueios = [b for b in self.bloqueios if t - b < 3600]
        self.bloqueios.append(t)
        self._parar(t, True)
        self.motivo = motivo
        if len(self.bloqueios) >= self.cc["falhas_para_bloqueio"]:
            self.estado = TRAVADO
        else:
            self.estado = BLOQUEADO
            self.bloq_ate = t + dur

    def reset_manual(self, t):
        if self.estado in (BLOQUEADO, TRAVADO):
            self.estado = PARADO
            self.bloqueios = []
            self.motivo = ""

    def _parar(self, t, forcada):
        if self.estado in (RODANDO, RECOLHENDO):
            self.t_desligou = t
            if forcada:
                self.paradas_forcadas += 1
                if t - self.t_ligou < self.min_ligado():
                    self.paradas_curtas += 1
        if self.estado not in (BLOQUEADO, TRAVADO):
            self.estado = PARADO

    def atualizar(self, t, quer, forcar, freq, pt1, permite_partida):
        if self.estado == BLOQUEADO and t >= self.bloq_ate:
            self.estado = PARADO
            self.motivo = ""
        if self.estado in (BLOQUEADO, TRAVADO):
            self.freq = 0.0
            return
        if forcar:
            if self.estado in (RODANDO, RECOLHENDO):
                self.motivo = forcar
            self._parar(t, True)
            self.freq = 0.0
            return
        if self.estado == PARADO:
            if quer and permite_partida and self.pode_partir(t):
                self.estado = RODANDO
                self.t_ligou = t
                self.partidas.append(t)
                self.motivo = ""
        elif self.estado == RODANDO:
            if (not quer) and (t - self.t_ligou >= self.min_ligado()):
                self.estado = RECOLHENDO
                self.t_rec = t
        elif self.estado == RECOLHENDO:
            fim = (pt1 is not None and pt1 <= self.cc["recolhimento_fim_bar"])
            if fim or (t - self.t_rec >= self.cc["recolhimento_max_s"]):
                self._parar(t, False)
            elif quer:
                self.estado = RODANDO  # voltou a precisar durante o recolhimento
        self.freq = freq if self.estado in (RODANDO, RECOLHENDO) else 0.0

    def ligado(self):
        return self.estado in (RODANDO, RECOLHENDO)


class Controlador:
    def __init__(self, cfg, t0=0.0):
        self.cfg = cfg
        self.sp = cfg["sp"]
        self.r = cfg["rota"]
        self.arq = cfg["arq"]
        self.cc = cfg["comp"]
        n = self.r["n_comp"]
        self.comps = [Compressor(i, self.cc, t0) for i in range(n)]
        self.t_ant = None
        self.integral = 0.0
        self.agua_extra = 0.0
        self.p2_on = True
        self.ar_alto = False
        self.t_botao = -1e9
        self.ultima_partida = -1e9
        self.precisa_carga = True
        self.t_cond_partida = [None] * n
        self.t_cond_queda = [None] * n
        self.t_cond_baixa = [None] * n
        self.t_succao_baixa = [None] * n
        self.t_deficit = None
        self.bat_comp = False
        # recepcao
        self.dia = None
        self.e_g_dia = 0.0        # Wh/m2 acumulado hoje
        self.e_g_valido = True
        self.nublados = 0
        self.aviso = AV_NORMAL
        self.feito_aviso_ini = False
        self.feito_9h = False
        self.feito_10h = False
        # alarmes
        self.alarmes = {}
        self.t_cond = {}
        self.eventos = []
        self.wd = False
        self.falhas = {}

    # ------------------------------------------------------------------
    def _valida(self, e):
        v = {}
        self.falhas = {}
        for k in FAIXAS:
            x = e.get(k)
            if x is None:
                v[k] = None
                if k in e:
                    self.falhas[k] = True
                continue
            a, b = FAIXAS[k]
            try:
                xf = float(x)
            except (TypeError, ValueError):
                xf = None
            if xf is None or xf != xf or xf < a or xf > b:
                v[k] = None
                self.falhas[k] = True
            else:
                v[k] = xf
        return v

    def _alarme(self, t, cod, cond, sev, msg, atraso=0):
        """Liga/desliga alarme com atraso; gera evento na mudanca."""
        if cond:
            if cod not in self.t_cond:
                self.t_cond[cod] = t
            if (t - self.t_cond[cod] >= atraso) and cod not in self.alarmes:
                self.alarmes[cod] = (sev, msg, t)
                self.eventos.append({"t": t, "cod": cod, "sev": sev,
                                     "msg": msg, "ativo": True})
        else:
            if cod in self.t_cond:
                del self.t_cond[cod]
            if cod in self.alarmes:
                sev0, msg0, _ = self.alarmes.pop(cod)
                self.eventos.append({"t": t, "cod": cod, "sev": sev0,
                                     "msg": msg0, "ativo": False})

    # ------------------------------------------------------------------
    def _recepcao(self, t, hora, dia, v, dt):
        sp = self.sp
        if self.dia is None:
            self.dia = dia
        if dia != self.dia:
            if self.e_g_valido:
                if self.e_g_dia / 1000.0 < sp["dia_nublado_kwh_m2"]:
                    self.nublados += 1
                else:
                    self.nublados = 0
            self.dia = dia
            self.e_g_dia = 0.0
            self.e_g_valido = True
            self.feito_aviso_ini = False
            self.feito_9h = False
            self.feito_10h = False
        if v["G"] is None:
            self.e_g_valido = False
        else:
            self.e_g_dia += v["G"] * dt / 3600.0
        lt1 = v["LT1"]
        if (not self.feito_aviso_ini) and hora >= sp["aviso_inicial_h"]:
            self.feito_aviso_ini = True
            if lt1 is None:
                self.aviso = AV_MEIA
            elif lt1 < sp["lt1_nao_receber"] or self.nublados >= 2:
                self.aviso = AV_NAO
            elif self.nublados == 1:
                self.aviso = AV_MEIA
            else:
                self.aviso = AV_NORMAL
        if (not self.feito_9h) and hora >= 9.0:
            self.feito_9h = True
            if self.aviso == AV_NORMAL and (lt1 is None or lt1 < sp["lt1_meia_carga_9h"]):
                self.aviso = AV_MEIA
        if (not self.feito_10h) and hora >= sp["aviso_revisao_h"]:
            self.feito_10h = True
            if self.e_g_valido:
                kwh = self.e_g_dia / 1000.0 * self.cfg["kwp"] * self.r["pr"]
                ruim = kwh < sp["kwh_kwp_ate_10h_min"] * self.cfg["kwp"]
            else:
                ruim = True
            if self.aviso == AV_NORMAL and ruim:
                self.aviso = AV_MEIA
            elif self.aviso == AV_NAO and (not ruim) and lt1 is not None and lt1 >= 30.0:
                self.aviso = AV_MEIA
            elif self.aviso == AV_MEIA and ruim and self.nublados >= 2:
                self.aviso = AV_NAO
        if lt1 is not None and lt1 < sp["lt1_nao_receber"]:
            self.aviso = AV_NAO

    # ------------------------------------------------------------------
    def _serpentina(self, hora, v, dt, lt1):
        sp = self.sp
        tc = v["TT1"]
        if tc is None and v["TT2"] is not None:
            tc = v["TT2"] - 0.8          # polpa do estoque fica ~0,8 K acima do ar
        if tc is None:
            # sem nenhuma temperatura da camara: posicao fixa conservadora
            # sem TT1 e TT2: posicao fixa que nao causa dano por frio
            # (camara pode esquentar ate ~14 C; alarme critico ja ativo)
            return sp["vent_min"], True, 8.0
        err = tc - sp["t_camara"]
        self.integral += sp["vent_kp"] * err * dt / sp["vent_ti_s"]
        self.integral = limitar(self.integral, -0.2, 0.7)
        f = limitar(sp["vent_min"] + sp["vent_kp"] * err + self.integral,
                    sp["vent_min"], 1.0)
        # protecao contra dano por frio: para de tirar calor
        if tc < sp["corte_frio_pump"]:
            self.p2_on = False
        elif tc > sp["corte_frio_pump"] + 1.0:
            self.p2_on = True
        # agua do banco ja mais quente que o ar (gelo acabou): circular so aquece
        # e gasta bateria -> bomba parada, ventilador no minimo
        inutil = v["TT4"] is not None and v["TT4"] > tc - 1.0
        if not self.p2_on or inutil:
            f = sp["vent_min"]
            self.integral = 0.0
            return f, False, sp["agua_dia"]
        noite = hora >= sp["agua_noite_ini_h"] or hora < sp["agua_noite_fim_h"]
        agua = sp["agua_noite"] if noite else sp["agua_dia"]
        # 2o estagio: com o ventilador no minimo e a camara abaixo do setpoint,
        # a valvula misturadora sobe a agua (ate +6 K) para nao esfriar demais
        if f <= sp["vent_min"] + 1e-6 and err < 0:
            self.agua_extra += -err * dt / 600.0
        else:
            self.agua_extra -= max(err, 0.05) * dt / 300.0
        self.agua_extra = limitar(self.agua_extra, 0.0, 6.0)
        agua += self.agua_extra
        if f > 0.9 or (lt1 is not None and lt1 <= 1.0):
            agua = sp["agua_dia"]        # falta frio: maxima descarga (prioridade camara)
            self.agua_extra = 0.0
        return f, self.p2_on, agua

    # ------------------------------------------------------------------
    def _demanda_rota_b(self, t, hora, e, v, lt1):
        r = self.r
        n = r["n_comp"]
        quer = [False] * n
        forcar = [None] * n
        freq = [0.0] * n
        kg = self.cfg["kwp_grupo"]
        aux = e.get("aux_kw")
        if aux is None:
            aux = 0.36
        lider = (self.dia or 0) % n          # rodizio diario
        soc = v["soc"]
        comum = r.get("barramento_comum", True)
        if v["G"] is not None:
            g_ok = True
            p_tot = self.cfg["kwp"] * v["G"] / 1000.0 * r["pr"] - aux
        else:
            g_ok = False
            p_tot = 0.0
        rodando = [i for i in range(n) if self.comps[i].ligado() and not (i == 0 and self.bat_comp)]
        for i in range(n):
            c = self.comps[i]
            if not g_ok:
                # sem irradiancia: janela 9-15 h e deixa o inversor decidir
                p = r["p_partida_kw"] if 9.0 <= hora <= 15.0 else 0.0
            elif comum:
                # um so arranjo para os dois inversores (suposicao S2 do LEIAME)
                outros = [j for j in rodando if j != i]
                if c.ligado():
                    p = p_tot / max(1, len(rodando))
                    if len(rodando) == 2 and i == lider:
                        p = 99.0       # quem cede primeiro e o outro
                else:
                    p = p_tot - len(outros) * r["p_min_kw"]
            else:
                p = kg * v["G"] / 1000.0 * r["pr"]
                if i == r["aux_no_grupo"] - 1:
                    p -= aux
            # condicao de partida sustentada
            if p >= r["p_partida_kw"]:
                if self.t_cond_partida[i] is None:
                    self.t_cond_partida[i] = t
                cond_partida = t - self.t_cond_partida[i] >= self.cc["atraso_partida_s"]
            else:
                self.t_cond_partida[i] = None
                cond_partida = False
            # queda de potencia
            if c.ligado() and g_ok and p < r["p_queda_kw"] and not (i == 0 and self.bat_comp):
                if self.t_cond_queda[i] is None:
                    self.t_cond_queda[i] = t
                if t - self.t_cond_queda[i] >= r["p_queda_atraso_s"]:
                    forcar[i] = "pouca potencia solar"
            else:
                self.t_cond_queda[i] = None
            if p < r["p_min_kw"]:
                if self.t_cond_baixa[i] is None:
                    self.t_cond_baixa[i] = t
                baixa = t - self.t_cond_baixa[i] >= 60
            else:
                self.t_cond_baixa[i] = None
                baixa = False
            q = self.precisa_carga
            if lt1 is not None and lt1 >= self.sp["lt1_so_um"]:
                q = q and (i == lider)        # perto de cheio: so 1 (rodizio)
            c.modo_cheio = lt1 is not None and lt1 >= self.sp["lt1_so_um"]
            if c.ligado():
                quer[i] = q and not baixa
            else:
                quer[i] = q and cond_partida
            pf = p if p < 50 else p_tot / max(1, len(rodando))
            fr = r["f_min_hz"] + (pf - r["p_min_kw"]) / max(0.1, r["p_max_kw"] - r["p_min_kw"]) * (r["f_max_hz"] - r["f_min_hz"])
            fr = limitar(fr, r["f_min_hz"], r["f_max_hz"])
            if c.modo_cheio:
                fr = r["f_min_hz"]
            freq[i] = fr
        # Bateria -> compressor 1 (so com gelo zerado e camara quente; doc 01, 12.3)
        if soc is not None and lt1 is not None:
            if (not self.bat_comp) and lt1 <= 1.0 and v["TT1"] is not None \
                    and v["TT1"] > r["bat_comp_t_camara"] and soc >= r["bat_comp_soc_min_liga"] \
                    and not self.comps[0].ligado():
                self.bat_comp = True
            elif self.bat_comp and (soc < r["bat_comp_soc_desliga"] or lt1 > 10.0
                                    or (v["TT1"] is not None and v["TT1"] < 12.5)):
                self.bat_comp = False
        else:
            self.bat_comp = False
        if self.bat_comp:
            quer[0] = True
            freq[0] = r["f_min_hz"]
            forcar[0] = None
            if soc is not None and soc < self.r["bat_comp_soc_desliga"] - 10:
                forcar[0] = "bateria baixa"
        return quer, forcar, freq

    def _demanda_rota_a(self, t, hora, e, v, lt1):
        r = self.r
        n = r["n_comp"]
        quer = [False] * n
        forcar = [None] * n
        freq = [0.0] * n
        soc = v["soc"]
        pv = e.get("pv_kw")
        if pv is None and v["G"] is not None:
            pv = self.cfg["kwp"] * v["G"] / 1000.0 * r["pr"]
        if pv is None:
            pv = 0.0
        carga = e.get("carga_kw")
        if carga is None:
            carga = 0.5
        pu = r["p_unidade_kw"]
        n_run = sum(1 for c in self.comps if c.ligado())
        sobra = pv - carga - n_run * pu
        camara_quente = (lt1 is not None and lt1 <= 1.0 and v["TT1"] is not None
                         and v["TT1"] > r["bat_comp_t_camara"])
        if soc is None:
            # sem leitura da bateria: so sol forte, 9-15 h
            pode_novo = (9.0 <= hora <= 15.0) and sobra >= pu
            manter = (9.0 <= hora <= 15.5) and sobra >= -0.2 * pu
            soc_ok_novo = pode_novo
            para = not manter
            critico = False
        else:
            ok_sobra = sobra >= r["partida_sobra_frac"] * pu
            ok_cheia = soc >= r["soc_partida_sem_sobra"] and pv > carga + 0.2 * pu
            soc_ok_novo = soc >= r["soc_min_partida"] and (ok_sobra or ok_cheia)
            if camara_quente and soc >= r["soc_para_camara"] + 10:
                soc_ok_novo = soc_ok_novo or n_run == 0
            if sobra < -0.6 * pu and soc < 85.0:
                if self.t_deficit is None:
                    self.t_deficit = t
                deficit = t - self.t_deficit >= r["deficit_para_s"]
            else:
                self.t_deficit = None
                deficit = False
            lim = r["soc_para_camara"] if camara_quente else r["soc_para"]
            para = soc < lim or (deficit and not camara_quente)
            critico = soc < r["soc_para_camara"]
        # condicao de partida sustentada (uma so para a proxima unidade)
        if soc_ok_novo:
            if self.t_cond_partida[0] is None:
                self.t_cond_partida[0] = t
            cond = t - self.t_cond_partida[0] >= self.cc["atraso_partida_s"]
        else:
            self.t_cond_partida[0] = None
            cond = False
        lider = (self.dia or 0) % n
        ordem = [lider] + [i for i in range(n) if i != lider]
        q = self.precisa_carga
        ja_pediu_novo = False
        ligados = [i for i in ordem if self.comps[i].ligado()]
        for i in ligados:
            quer[i] = q
            if critico:
                forcar[i] = "bateria critica"
        if para and ligados:
            quer[ligados[-1]] = False   # desliga uma unidade por vez
        for i in ordem:
            c = self.comps[i]
            if not c.ligado():
                so_um = lt1 is None or lt1 >= self.sp["lt1_so_um"]
                if q and cond and not ja_pediu_novo and not para and not (so_um and n_run >= 1):
                    quer[i] = True
                    ja_pediu_novo = True
            c.modo_cheio = lt1 is not None and lt1 >= self.sp["lt1_so_um"]
            freq[i] = 60.0
        return quer, forcar, freq

    # ------------------------------------------------------------------
    def passo(self, e):
        t = float(e["t"])
        hora = float(e["hora"])
        dia = int(e.get("dia", 0))
        dt = 0.0 if self.t_ant is None else max(0.0, t - self.t_ant)
        self.t_ant = t
        self.eventos = []
        sp = self.sp
        v = self._valida(e)
        lt1 = v["LT1"]
        comp_in = e.get("comp") or [{} for _ in self.comps]

        # ---- banco de gelo: precisa carregar? (histerese)
        ei1 = bool(e.get("EI1", False))
        if lt1 is not None:
            if lt1 >= sp["lt1_cheio"] or ei1:
                self.precisa_carga = False
            elif lt1 < sp["lt1_religa"]:
                self.precisa_carga = True
        else:
            # sem LT1: carrega ate a sonda de espessura EI1 (ou a sucao baixa)
            # indicar gelo grosso; volta a carregar quando EI1 solta
            self.precisa_carga = not ei1

        self._recepcao(t, hora, dia, v, dt)
        f_vent, p2, agua = self._serpentina(hora, v, dt, lt1)

        # ---- demanda por rota
        if self.r["rota"] == "B":
            quer, forcar, freq = self._demanda_rota_b(t, hora, e, v, lt1)
        else:
            quer, forcar, freq = self._demanda_rota_a(t, hora, e, v, lt1)

        # ---- protecoes comuns por compressor
        glicol_baixo = False
        if self.arq.get("glicol"):
            tg = v["T_glicol"]
            glicol_baixo = tg is not None and tg < self.arq["glicol_min_c"]
            if tg is None:
                glicol_baixo = True   # sem sensor de glicol: nao arrisca congelar
        sem_fluxo = self.arq.get("glicol") and (e.get("fluxo_ok") is False)
        gas = bool(e.get("gas", False))
        for i in range(len(self.comps)):
            c = self.comps[i]
            ci = comp_in[i] if i < len(comp_in) else {}
            pt1 = ci.get("PT1")
            pt2 = ci.get("PT2")
            if gas:
                forcar[i] = "gas detectado"
            if ci.get("cadeia_ok") is False:
                forcar[i] = "cadeia de seguranca aberta"
            if ci.get("inversor_falha"):
                forcar[i] = "falha do inversor"
            if glicol_baixo:
                forcar[i] = "glicol frio demais (anticongelamento)"
            if sem_fluxo and c.ligado():
                forcar[i] = "sem fluxo de glicol"
            if c.ligado() and (pt1 is None or pt2 is None):
                c.bloquear(t, "sensor de pressao em falha", 600)
                continue
            if pt2 is not None and pt2 >= self.cc["alta_para_bar"]:
                c.bloquear(t, "alta pressao (software)", self.cc["alta_bloqueio_s"])
                continue
            if pt2 is not None and pt2 >= self.cc["alta_reduz_bar"] and self.r["velocidade_variavel"]:
                freq[i] = max(self.r["f_min_hz"], freq[i] - 10.0)
            if c.ligado() and pt1 is not None and c.estado == RODANDO:
                if tsat_r134a(pt1) < self.cc["succao_sat_min_c"]:
                    if self.t_succao_baixa[i] is None:
                        self.t_succao_baixa[i] = t
                    if t - self.t_succao_baixa[i] >= self.cc["succao_sat_min_atraso_s"]:
                        quer[i] = False
                        if lt1 is None:
                            self.precisa_carga = False
                else:
                    self.t_succao_baixa[i] = None
            # arquitetura (a): a bomba P1 tem de dar fluxo antes da partida
            if self.arq.get("glicol") and not c.ligado() and e.get("fluxo_ok") is not True:
                if quer[i]:
                    pass  # bomba liga abaixo; parte no proximo ciclo com fluxo
            permite = (t - self.ultima_partida >= self.cc["intervalo_entre_partidas_s"])
            if self.arq.get("glicol") and e.get("fluxo_ok") is not True:
                permite = False
            antes = c.ligado()
            c.atualizar(t, quer[i], forcar[i], freq[i], pt1, permite)
            if c.ligado() and not antes:
                self.ultima_partida = t

        algum_quer = any(quer)
        bomba_banco = any(c.ligado() for c in self.comps) or (self.arq.get("glicol") and algum_quer)

        # ---- CO2 e ar novo
        co2 = v["CO2"]
        if e.get("botao_entrada"):
            self.t_botao = t
        if co2 is None:
            ar = sp["ar_novo_max"]
            luz = "VERMELHA"
        else:
            if co2 > sp["co2_luz_verde"]:
                self.ar_alto = True
            elif co2 < sp["co2_luz_verde"] - 0.04:
                self.ar_alto = False
            ar = sp["ar_novo_max"] if self.ar_alto else sp["ar_novo_base"]
            luz = "VERDE" if co2 < sp["co2_luz_verde"] else "VERMELHA"
        if sp["ar_novo_purga_ini_h"] <= hora < sp["ar_novo_purga_fim_h"] or t - self.t_botao < 1800:
            ar = sp["ar_novo_max"]
        if gas:
            ar = sp["ar_novo_max"]

        # ---- carter
        carter = []
        for c in self.comps:
            carter.append((not c.ligado()) and sp["carter_ini_h"] <= hora <= sp["carter_fim_h"])

        # ---- energia: corte de cargas
        soc = v["soc"]
        starlink = not (soc is not None and soc < sp["soc_corta_starlink"])

        # ---- alarmes
        tt1 = v["TT1"]
        A = self._alarme
        A(t, "A01", tt1 is not None and tt1 > sp["alarme_alto"], "CRITICO",
          "Camara acima de 15 C ha 2 h", sp["alarme_alto_atraso_s"])
        A(t, "A02", tt1 is not None and tt1 < sp["alarme_baixo"], "CRITICO",
          "Camara abaixo de 10 C (dano por frio)", sp["alarme_baixo_atraso_s"])
        A(t, "A03", lt1 is not None and lt1 < sp["lt1_nao_receber"], "AVISO", "Gelo abaixo de 20 %")
        A(t, "A04", lt1 is not None and lt1 <= 1.0, "CRITICO", "Gelo esgotado", 300)
        A(t, "A05", co2 is not None and co2 >= sp["co2_alarme"], "AVISO", "CO2 acima de 1 %", 300)
        A(t, "A06", co2 is not None and co2 >= sp["co2_critico"], "CRITICO", "CO2 acima de 2 % - nao entrar", 60)
        A(t, "A07", bool(e.get("porta")), "AVISO", "Porta aberta ha mais de 10 min", sp["porta_aberta_alarme_s"])
        A(t, "A08", bool(e.get("pessoa_presa")), "CRITICO", "BOTAO DE PESSOA PRESA")
        for k in ("TT1", "TT2", "TT5", "LT1", "CO2", "G", "soc", "T_glicol"):
            if k == "T_glicol" and not self.arq.get("glicol"):
                continue
            A(t, "S-" + k, k in self.falhas, "AVISO" if k not in ("TT1", "LT1", "CO2") else "CRITICO",
              "Sensor " + k + " em falha", 30)
        for i, c in enumerate(self.comps):
            A(t, "A09-%d" % (i + 1), c.estado in (BLOQUEADO, TRAVADO), "AVISO" if c.estado == BLOQUEADO else "CRITICO",
              "Compressor %d bloqueado: %s" % (i + 1, c.motivo))
            ci = comp_in[i] if i < len(comp_in) else {}
            A(t, "A10-%d" % (i + 1), ci.get("cadeia_ok") is False, "CRITICO",
              "Cadeia de seguranca aberta no compressor %d (PSH/PSL/termico/fluxo)" % (i + 1), 5)
        A(t, "A11", soc is not None and soc < sp["soc_aviso"], "AVISO", "Bateria abaixo de 30 %")
        A(t, "A12", soc is not None and soc < sp["soc_critico"], "CRITICO", "Bateria abaixo de 15 %")
        A(t, "A13", e.get("com_inversor") is False, "AVISO", "Sem comunicacao com o inversor", 60)
        A(t, "A14", glicol_baixo, "CRITICO", "Glicol frio demais / sensor do glicol", 5)
        A(t, "A15", gas, "CRITICO", "GAS DETECTADO")
        A(t, "A16", v["TT2"] is not None and v["TT2"] > sp["polpa_estoque_alarme"], "AVISO",
          "Polpa do estoque acima de 14 C", 1800)
        A(t, "A17", v["TT5"] is not None and v["TT5"] < self.arq["agua_min_c"], "AVISO",
          "Agua para a serpentina abaixo de 2 C", 300)
        A(t, "A18", self.bat_comp, "AVISO", "Bateria tocando compressor (gelo zerado)")

        sirene = any(k in self.alarmes for k in ("A06", "A08", "A15"))
        self.wd = not self.wd

        rec_hora = sp["recepcao_ini_h"] <= hora < sp["recepcao_fim_h"]
        return {
            "comp": [{"liga": c.ligado(), "freq": c.freq,
                      "solenoide": c.estado == RODANDO, "carter": carter[i],
                      "estado": c.estado} for i, c in enumerate(self.comps)],
            "bat_comp": self.bat_comp,
            "bomba_banco": bomba_banco,
            "bomba_p2": p2,
            "vent_serp": f_vent,
            "agua_sp": agua,
            "ar_novo_m3h": ar,
            "luz_porta": luz,
            "aviso": self.aviso if rec_hora else (self.aviso + "_FORA_DO_HORARIO" if hora >= sp["recepcao_fim_h"] else self.aviso),
            "aviso_base": self.aviso,
            "starlink": starlink,
            "sirene": sirene,
            "alarmes": sorted(self.alarmes.keys()),
            "eventos": self.eventos,
            "watchdog": self.wd,
            "nublados": self.nublados,
        }

    def reset_manual(self, t):
        for c in self.comps:
            c.reset_manual(t)


def saidas_estado_seguro(n_comp=2):
    """O que o HARDWARE faz quando o controlador para (rele de watchdog cai).
    Usado pela simulacao para mostrar o comportamento sem controlador.
    Compressores desligados; bomba P2 e ventiladores ligados em velocidade
    fixa pelo contato NF; ar novo na base; luz da porta vermelha."""
    return {
        "comp": [{"liga": False, "freq": 0.0, "solenoide": False, "carter": False,
                  "estado": "SEM_CONTROLADOR"} for _ in range(n_comp)],
        "bat_comp": False, "bomba_banco": False, "bomba_p2": True,
        "vent_serp": 0.6, "agua_sp": 3.0, "ar_novo_m3h": 30.0,
        "luz_porta": "VERMELHA", "aviso": AV_NAO, "aviso_base": AV_NAO,
        "starlink": True, "sirene": False, "alarmes": ["SEM_CONTROLADOR"],
        "eventos": [], "watchdog": False, "nublados": 0,
    }
