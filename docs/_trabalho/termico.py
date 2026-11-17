#!/usr/bin/env python3
"""
Contas do projeto termico, versao 2 (docs/01-projeto-termico.md), refeitas apos a
revisao e as decisoes do dono D1 a D5:
  D1 so manga, uma zona a 12 C, 5 t        D2 recepcao das 7 h as 14 h, fruta a 30-35 C
  D3 sem propano montado no local          D4 bateria de apoio      D5 um prototipo
Rodar:  python3 docs/_trabalho/termico.py > docs/_trabalho/termico_saida.txt
Depende de CoolProp (pip install CoolProp).

Modelo: passo de 6 min. A serpentina de ar tem potencia limitada; se a carga passa
do que ela entrega, o ar e a polpa esquentam (isso responde o achado 4 da revisao).
SUPOSTO = valor adotado sem fonte aberta; esta marcado igual no documento.
"""
import math
from functools import lru_cache
from CoolProp.CoolProp import PropsSI

DT = 0.1                 # h, passo de calculo
# ------------------------------------------------------------------ camara e fruta
T_SET = 12.0             # C  (D1)
UA_ENV = 33.0            # W/K reefer usado (22 de fabrica x 1,5)            SUPOSTO
M_ESTOQUE = 4000.0       # kg de fruta ja fria (5 t no total, D1)
CP_FRUTA = 3.77          # kJ/kg.K (0,901 kcal/kg.C)
CAIXAS_KJ_K_POR_T = 50 * 1.8 * 1.9   # 50 caixas de 1,8 kg por tonelada, PEAD       SUPOSTO
TAU = 8.0                # h, constante de tempo da fruta em caixa na camara        SUPOSTO
RESP_10 = 83.0           # W/t manga a 10 C: 14 ml CO2/kg.h x 122 kcal/t.dia (UC Davis)
Q10 = 2.5                # SUPOSTO
V_INT = 28.0             # m3
TROCAS_PORTA = 12.0      # trocas de ar por dia pela porta                           SUPOSTO
AR_NOVO_M3H = 30.0       # renovacao continua: CO2 estabiliza em 0,32 % (< 0,39 %)    CALCULADO sobre SUPOSTO
PURGA_M3 = 45.0          # ventilacao antes da primeira entrada do dia               SUPOSTO
FOLGA = 1.10             # folga sobre o frio tirado do banco                        SUPOSTO
# ------------------------------------------------------------------ serpentina de ar e auxiliares
K_COIL = 900.0           # W/K entre ar que entra e agua que entra, ventilador a 100 % SUPOSTO (conta no doc)
T_AGUA = {"b": 3.0, "a": 3.0}     # C, agua/glicol que chega a serpentina das 7 h as 17 h
T_AGUA_NOITE = 6.0       # C, das 17 h as 7 h (preserva a umidade)                  SUPOSTO
P_FAN_MAX, P_FAN_MIN_FRAC = 240.0, 0.30   # W; 6.000 m3/h, 50 Pa, rendimento 0,35  CALCULADO sobre SUPOSTO
PESSOA_W = 272 - 6 * T_SET        # W por pessoa (formula ASHRAE, de memoria)        SUPOSTO
UA_TANQUE = 3.5          # W/K banco de gelo + tubos                                 CALCULADO sobre SUPOSTO
# ------------------------------------------------------------------ frio e solar
PR = 0.75                # desempenho global do arranjo                              SUPOSTO
ETA = 0.60               # eficiencia global de compressao (nao e catalogo)          SUPOSTO
F_R513A = 0.97           # COP do R513A em relacao ao R134a                          SUPOSTO (de memoria)
ARQ = {  # arquitetura: evaporacao, auxiliares de dia (W), perda extra de conversao
    "b": dict(nome="(b) R513A montado no local, banco de gelo de expansao direta + agua gelada",
              tevap=-7.0, aux=300 + 60, conv=1.00, fluido="R134a", fcop=F_R513A),
    "a": dict(nome="(a) chiller de glicol selado de fabrica + banco de gelo a glicol",
              tevap=-10.5, aux=300 + 260, conv=0.94, fluido="R134a", fcop=F_R513A),
}
DT_COND = 10.0           # K                                                         SUPOSTO
L_GELO = 334.0 / 3600    # kWh/kg
PMAX_FRAC, PMIN_FRAC = 0.62, 0.215   # potencia maxima dos 2 compressores / kWp; minimo de 1 compressor

# recepcao da fruta: lista de (hora, kg, temperatura)
RECEP = {
    "ate10h": [(7, 333.0, 30.0), (8, 333.0, 30.0), (9, 334.0, 30.0)],
    "ate14h": [(10, 250.0, 35.0), (11, 250.0, 35.0), (12, 250.0, 35.0), (13, 250.0, 35.0)],
    "tudo13h": [(13, 1000.0, 35.0)],
    "meia": [(10, 250.0, 35.0), (12, 250.0, 35.0)],
    "nada": [],
}
# dias: (irradiacao kWh/m2.dia, Tmax, Tmin)
DIA = {"recorde": (5.8, 41.0, 27.0), "quente": (5.8, 34.0, 23.0), "junho": (4.7, 31.0, 20.0),
       "ruim": (3.0, 33.0, 23.0), "nublado": (2.0, 32.0, 22.0), "recorde-10%": (5.2, 41.0, 27.0)}


def t_amb(h, tmax, tmin):
    return (tmax + tmin) / 2 + (tmax - tmin) / 2 * math.cos(2 * math.pi * (h - 15) / 24)


@lru_cache(maxsize=None)
def irr_hora(h, H, nascer=5.5, por=17.7):
    def f(x):
        return math.sin(math.pi * (x - nascer) / (por - nascer)) ** 1.3 if nascer < x < por else 0.0
    p = 0.05
    tot = sum(f(i * p) * p for i in range(int(24 / p)))
    return H * sum(f(h + i * p) * p for i in range(int(1 / p))) / tot


def entalpia_ar(t, ur, p=97.0):
    ps = 0.61094 * math.exp(17.625 * t / (t + 243.04))
    w = 0.622 * ur * ps / (p - ur * ps)
    return 1.006 * t + w * (2501 + 1.86 * t)


@lru_cache(maxsize=None)
def ciclo(tevap, tamb, fluido="R134a", sh=8.0, sc=3.0):
    te, tc = tevap + 273.15, max(tamb + DT_COND, 30.0) + 273.15
    pe, pc = PropsSI("P", "T", te, "Q", 1, fluido), PropsSI("P", "T", tc, "Q", 0, fluido)
    h1, s1 = PropsSI("H", "T", te + sh, "P", pe, fluido), PropsSI("S", "T", te + sh, "P", pe, fluido)
    h2s, h4 = PropsSI("H", "P", pc, "S", s1, fluido), PropsSI("H", "T", tc - sc, "P", pc, fluido)
    rho = PropsSI("D", "T", te + sh, "P", pe, fluido)
    return (h1 - h4) / (h2s - h1) * ETA, pe / 1e5, pc / 1e5, (h1 - h4) / 1e3, rho


def cop(arq, tamb):
    a = ARQ[arq]
    return ciclo(a["tevap"], round(tamb * 2) / 2, a["fluido"])[0] * a["fcop"] * a["conv"]


def simula(kwp, kg, dias, arq="b", bat=0.0, pmax=None, s0=None, bat0=None, estado=None):
    """dias: lista de (nome_do_dia, nome_da_recepcao). Devolve (lista de resumos por dia, estado final)."""
    a = ARQ[arq]
    cap = kg * L_GELO
    pmax = PMAX_FRAC * kwp if pmax is None else pmax
    pmin = PMIN_FRAC * pmax
    if estado is None:
        estado = dict(s=cap if s0 is None else s0, b=bat if bat0 is None else bat0, t_est=T_SET, lotes=[], tair=T_SET)
    s, b, t_est, lotes, tair = estado["s"], estado["b"], estado["t_est"], list(estado["lotes"]), estado["tair"]
    out = []
    for (nd, nr) in dias:
        H, tmax, tmin = DIA[nd]
        rec = RECEP[nr]
        d = dict(dia=nd, rec=nr, carga=0.0, prod=0.0, fv=0.0, comp=0.0, sobra=0.0, falta=0.0, smin=s, tair_max=tair,
                 test_max=t_est, tnovo_fim=None, aux_noite=0.0, pico_serp=0.0, bat_usada=0.0, horas=[],
                 parc=dict(env=0.0, porta=0.0, arnovo=0.0, campo=0.0, resp=0.0, vent=0.0, gente=0.0, bomba_tanque=0.0))
        acc = None
        for i in range(int(24 / DT)):
            h = i * DT
            hh = int(h)
            ta = t_amb(h, tmax, tmin)
            # entrada de fruta: no inicio da hora
            for (hr, m, tin) in rec:
                if abs(h - hr) < DT / 2:
                    lotes.append([m, tin])
            # lotes quase frios viram estoque (mantem 5 t no total: sai fruta velha)
            for lt in [x for x in lotes if x[1] - t_est < 0.3 and len(lotes) > 8]:
                lotes.remove(lt)
            m_novo = sum(x[0] for x in lotes)
            m_est = max(M_ESTOQUE + 1000.0 - m_novo, 0.0) if m_novo <= 1000.0 else M_ESTOQUE
            # cargas que nao dependem do ar interno
            dh = entalpia_ar(ta, 0.30) - entalpia_ar(T_SET, 0.90)
            recep_horas = sorted({hr for (hr, _, _) in rec})
            q_porta = 0.0
            e_porta = TROCAS_PORTA * V_INT * 1.1 * dh / 3600
            if recep_horas and hh in recep_horas:
                q_porta += 0.6 * e_porta / len(recep_horas)
            if 7 <= hh < 17:
                q_porta += (0.4 if recep_horas else 0.5) * e_porta / 10
            q_arnovo = AR_NOVO_M3H * 1.1 * dh / 3600 + (PURGA_M3 * 1.1 * dh / 3600 if hh == 6 else 0.0)
            gente = (2 * PESSOA_W + 40) / 1000 if hh in recep_horas else ((PESSOA_W + 40) / 2000 if hh in (7, 15) else 0.0)
            sol = 2.0 if 7 <= hh <= 16 else 0.0
            # frutas: G = m.cp/tau
            g_est = (m_est * CP_FRUTA + m_est / 1000 * CAIXAS_KJ_K_POR_T) / 3600 / TAU      # kW/K
            g_lot = [(x[0] * CP_FRUTA + x[0] / 1000 * CAIXAS_KJ_K_POR_T) / 3600 / TAU for x in lotes]
            ua = UA_ENV / 1000
            A = ua * (ta + sol) + q_porta + q_arnovo + gente + g_est * t_est + sum(g * x[1] for g, x in zip(g_lot, lotes))
            B = ua + g_est + sum(g_lot)
            # ventilador: do passo anterior
            tw = T_AGUA_NOITE if (hh >= 17 or hh < 7) else T_AGUA[arq]
            q_req0 = A - B * T_SET
            k_need = max(q_req0, 0.0) * 1000 / max(T_SET - tw, 0.1)
            f = min(1.0, max(P_FAN_MIN_FRAC, k_need / K_COIL))
            p_fan = (10 + P_FAN_MAX * f ** 3) / 1000
            kmax = K_COIL * f / 1000
            q_req = q_req0 + p_fan
            # producao de frio
            p_fv = kwp * irr_hora(hh, H) * PR
            p_disp = p_fv - a["aux"] / 1000
            c = cop(arq, ta)
            p_comp = min(p_disp, pmax) if p_disp >= pmin else 0.0
            q_prod = p_comp * c
            p_bomba = (25 + 10 * max(q_req, 0)) / 1000
            q_tanque = UA_TANQUE * (ta - 0) / 1000
            # serpentina: limitada pela potencia
            q_coil = max(min(q_req, kmax * (T_SET - tw)), 0.0)
            tair = T_SET
            if q_req > q_coil + 1e-9:
                tair = (A + p_fan + kmax * tw) / (B + kmax)
                q_coil = kmax * (tair - tw)
            dreno = (q_coil + p_bomba + q_tanque) * FOLGA
            # banco cheio: compressor so acompanha a carga (liga-desliga no minimo)
            if s + (q_prod - dreno) * DT > cap:
                q_prod = max(0.0, (cap - s) / DT + dreno)
                p_comp = q_prod / c
            s_novo = s + (q_prod - dreno) * DT
            # bateria de apoio: carrega com a sobra, descarrega para evitar falta de gelo
            sobra = max(0.0, p_fv - (p_comp + a["aux"] / 1000 if p_comp > 0 else 0.0))
            if bat > 0 and sobra > 0:
                carga_b = min(sobra * DT * 0.95, bat - b)
                b += carga_b
                sobra -= carga_b / 0.95 / DT
            if s_novo < 0 and bat > 0 and b > 0:
                e = min(b, -s_novo / c / 0.95, pmax * DT)
                b -= e
                s_novo += e * 0.95 * c
                d["bat_usada"] += e
                q_prod += e * 0.95 * c / DT
            falta = 0.0
            if s_novo < 0:
                # sem gelo: a serpentina so entrega o que ha; o resto esquenta o ar e a fruta
                q_ok = max(0.0, q_coil + s_novo / DT / FOLGA)
                falta = (q_coil - q_ok) * DT
                q_coil = q_ok
                tair = (A + p_fan - q_coil) / B
                s_novo = 0.0
            s = s_novo
            # evolucao da fruta
            def resp(t):
                return RESP_10 * Q10 ** ((min(t, 38.0) - 10) / 10) / 1e6      # kW/kg; teto a 38 C (SUPOSTO)
            q_campo = q_resp = 0.0
            cth = (m_est * CP_FRUTA + m_est / 1000 * CAIXAS_KJ_K_POR_T) / 3600
            t_est += (-g_est * (t_est - tair) + resp(t_est) * m_est) / cth * DT if cth > 0 else 0.0
            q_resp += resp(t_est) * m_est
            for g, x in zip(g_lot, lotes):
                cl = g * TAU
                q_campo += g * (x[1] - tair) - resp(x[1]) * x[0]
                q_resp += resp(x[1]) * x[0]
                x[1] += (-g * (x[1] - tair) + resp(x[1]) * x[0]) / cl * DT
            # contabilidade
            p = d["parc"]
            p["env"] += ua * (ta + sol - tair) * DT; p["porta"] += q_porta * DT; p["arnovo"] += q_arnovo * DT
            p["campo"] += max(q_campo, 0) * DT; p["resp"] += q_resp * DT; p["vent"] += p_fan * DT; p["gente"] += gente * DT
            p["bomba_tanque"] += (p_bomba + q_tanque) * DT
            d["carga"] += dreno * DT; d["prod"] += q_prod * DT; d["fv"] += p_fv * DT; d["comp"] += p_comp * DT
            d["sobra"] += sobra * DT; d["falta"] += falta; d["smin"] = min(d["smin"], s)
            d["tair_max"] = max(d["tair_max"], tair); d["test_max"] = max(d["test_max"], t_est)
            d["pico_serp"] = max(d["pico_serp"], q_coil)
            aux_noite_w = (p_fan + p_bomba) * 1000 + 15 + 5
            if hh >= 17 or hh < 7:
                d["aux_noite"] += aux_noite_w * DT / 1000
            if acc is None or acc["h"] != hh:
                if acc:
                    d["horas"].append(acc)
                acc = dict(h=hh, ta=0, fv=0, comp=0, prod=0, serp=0, req=0, tair=0, tnovo=0, test=0, s=0, aux=0, n=0)
            acc["ta"] += ta; acc["fv"] += p_fv; acc["comp"] += p_comp; acc["prod"] += q_prod; acc["serp"] += q_coil
            acc["req"] += q_req; acc["tair"] = max(acc["tair"], tair); acc["test"] = t_est
            acc["tnovo"] = max([x[1] for x in lotes], default=t_est); acc["s"] = s; acc["aux"] += aux_noite_w; acc["n"] += 1
        d["horas"].append(acc)
        d["sfim"] = s; d["bfim"] = b
        d["tnovo_fim"] = max([x[1] for x in lotes], default=t_est)
        out.append(d)
    return out, dict(s=s, b=b, t_est=t_est, lotes=lotes, tair=tair)


def regime(kwp, kg, nd, nr, n=5, **kw):
    r, est = simula(kwp, kg, [(nd, nr)] * n, **kw)
    return r[-1], est


def minimo(nd, nr, arq, criterio=lambda d: d["falta"] < 0.05):
    """menor (kWp, kg) que atende; devolve tambem o par de menor gelo com 12 kWp"""
    achados = []
    for kwp in (8, 9, 10, 11, 12, 13, 14, 16):
        for kg in (300, 400, 500, 600, 700, 800, 1000):
            if criterio(regime(kwp, kg, nd, nr, arq=arq)[0]):
                achados.append((kwp, kg))
                break
    return achados


def cabec(*c):
    print("| " + " | ".join(c) + " |")
    print("|" + "---|" * len(c))


if __name__ == "__main__":
    print("## 0. Ciclo (propriedades do R134a pelo CoolProp %s; COP x %.2f para R513A; eficiencia global %.2f SUPOSTA)"
          % (__import__("CoolProp").__version__, F_R513A, ETA))
    cabec("arquitetura", "T evap C", "T ext C", "T cond C", "p evap bar abs", "p evap bar rel", "p cond bar abs", "p cond bar rel", "COP eletrico")
    for k in ("b", "a"):
        for ta in (27, 34, 41, 43):
            c_, pe, pc, dh, rho = ciclo(ARQ[k]["tevap"], ta)
            print(f"| {k} | {ARQ[k]['tevap']} | {ta} | {ta + DT_COND:.0f} | {pe:.2f} | {pe - 0.97:.2f} | {pc:.2f} | {pc - 0.97:.2f} | {cop(k, ta):.2f} |")
    for tsat in (-18, -12, -7, 51, 60, 65):
        print(f"R134a saturado a {tsat} C: {PropsSI('P', 'T', tsat + 273.15, 'Q', 0.5, 'R134a') / 1e5:.2f} bar abs = {PropsSI('P', 'T', tsat + 273.15, 'Q', 0.5, 'R134a') / 1e5 - 0.97:.2f} bar rel (atm local 0,97 bar)")
    c_, pe, pc, dh, rho = ciclo(-7.0, 41)
    for qf in (6.0, 7.0, 8.0):
        m = qf / dh
        print(f"arquitetura b, Q={qf:.0f} kW a -7/+51 C: {m * 3600:.0f} kg/h; aspirado {m / rho * 3600:.1f} m3/h; deslocamento com rend. vol. 0,75: "
              f"{m / rho * 3600 / 0.75:.1f} m3/h na rotacao maxima = {m / rho * 3600 / 0.75 * 50 / 70:.1f} m3/h a 50 Hz; potencia {qf / cop('b', 41):.2f} kW")

    print("\n## 1. Carga termica diaria em regime (kWh/dia), 12 kWp + 700 kg, arquitetura b")
    cabec("dia", "recepcao", "involucro", "porta", "ar novo (CO2)", "calor de campo", "respiracao", "ventiladores", "pessoas+luz", "bomba+banco", "soma", "tirado do banco c/ folga 10 %", "pico na serpentina kW")
    for nd, nr in (("recorde", "ate14h"), ("recorde", "ate10h"), ("recorde", "tudo13h"), ("quente", "ate14h"), ("junho", "ate14h"), ("recorde", "nada")):
        d, _ = regime(12, 700, nd, nr)
        p = d["parc"]
        soma = sum(p.values())
        print(f"| {nd} | {nr} | {p['env']:.1f} | {p['porta']:.1f} | {p['arnovo']:.1f} | {p['campo']:.1f} | {p['resp']:.1f} | {p['vent']:.1f} | {p['gente']:.1f} | {p['bomba_tanque']:.1f} | {soma:.1f} | {d['carga']:.1f} | {d['pico_serp']:.1f} |")

    print("\n## 2. Os numeros do dono (5 kWp + 200 kg), dia recorde, recepcao ate 14 h")
    for k in ("b", "a"):
        d, _ = regime(5, 200, "recorde", "ate14h", arq=k)
        print(f"arquitetura {k}: FV {d['fv']:.1f} kWh; frio produzido {d['prod']:.1f} kWh; frio pedido {d['carga'] + d['falta'] * FOLGA:.1f} kWh; nao atendido {d['falta']:.1f} kWh/dia; "
              f"ar ate {d['tair_max']:.1f} C; polpa do estoque ate {d['test_max']:.1f} C")

    print("\n## 3. Varredura: frio nao atendido (kWh/dia) em regime, dia recorde (27-41 C; 5,8 kWh/m2)")
    gelos = (300, 400, 500, 600, 700, 800, 1000)
    for k in ("b", "a"):
        for nr in ("ate10h", "ate14h"):
            print(f"\narquitetura {k}, recepcao {nr}:")
            cabec("kWp \\ kg de gelo", *[str(g) for g in gelos])
            for kwp in (5, 8, 9, 10, 11, 12, 13, 14):
                print(f"| {kwp} | " + " | ".join(f"{regime(kwp, g, 'recorde', nr, arq=k)[0]['falta']:.1f}" for g in gelos) + " |")

    print("\n## 3b. Tabela unica de variantes: menor conjunto que fecha (nao atendido < 0,05 kWh/dia) no dia recorde")
    cabec("arquitetura", "recepcao", "frio tirado do banco kWh/dia", "menor kWp (com o gelo que ele pede)", "menor gelo com 12 kWp", "gelo gasto das 17 h as 7 h (kWh)")
    for k in ("b", "a"):
        for nr in ("ate10h", "ate14h", "tudo13h"):
            ach = minimo("recorde", nr, k)
            d12, _ = regime(12, 1000, "recorde", nr, arq=k)
            noite = sum(x["serp"] / x["n"] for x in d12["horas"] if x["h"] >= 17 or x["h"] < 7) * FOLGA
            g12 = [g for (kw_, g) in ach if kw_ == 12]
            print(f"| {k} | {nr} | {d12['carga']:.1f} | {ach[0][0]} kWp + {ach[0][1]} kg | {g12[0] if g12 else 'nao fecha'} kg | {noite:.1f} |")

    KWP, KG, AR = 12, 700, "b"
    print(f"\n## 4. Conjunto de referencia: {KWP} kWp + {KG} kg de gelo ({KG * L_GELO:.1f} kWh), arquitetura {AR}, 2 compressores somando {PMAX_FRAC * KWP:.1f} kW (minimo de 1 compressor: {PMIN_FRAC * PMAX_FRAC * KWP:.1f} kW)")
    for nd, nr in (("recorde", "ate14h"),):
        d, _ = regime(KWP, KG, nd, nr, arq=AR)
        print(f"\n### Hora a hora, dia {nd}, recepcao {nr}, em regime")
        cabec("h", "T ext", "FV kW", "compr. kW", "frio prod. kW", "serpentina kW", "ar C (max)", "polpa lote mais quente C", "polpa estoque C", "gelo kWh", "auxiliares internos W")
        for x in d["horas"]:
            n = x["n"]
            print(f"| {x['h']:02d} | {x['ta'] / n:.1f} | {x['fv'] / n:.2f} | {x['comp'] / n:.2f} | {x['prod'] / n:.2f} | {x['serp'] / n:.2f} | {x['tair']:.1f} | {x['tnovo']:.1f} | {x['test']:.1f} | {x['s']:.1f} | {x['aux'] / n:.0f} |")
        print(f"| dia | | {d['fv']:.1f} kWh | {d['comp']:.1f} kWh | {d['prod']:.1f} kWh | {d['carga'] / FOLGA:.1f} kWh | max {d['tair_max']:.1f} | | max {d['test_max']:.1f} | min {d['smin']:.1f} | noite {d['aux_noite']:.2f} kWh |")
        print(f"COP medio do dia {d['prod'] / d['comp']:.2f}; FV nao aproveitada {d['sobra']:.1f} kWh; consumo dos auxiliares internos das 17 h as 7 h: {d['aux_noite']:.2f} kWh")

    print("\n### Cenarios com o conjunto de referencia (em regime)")
    cabec("dia", "recepcao", "arq.", "frio tirado kWh", "frio produzido kWh", "nao atendido kWh", "gelo minimo kWh", "ar max C", "polpa estoque max C", "FV sobrando kWh", "aux. noite kWh")
    for nd, nr, k in (("recorde", "ate14h", "b"), ("recorde", "ate10h", "b"), ("recorde", "tudo13h", "b"), ("quente", "ate14h", "b"), ("junho", "ate14h", "b"),
                      ("recorde-10%", "ate14h", "b"), ("ruim", "ate14h", "b"), ("ruim", "meia", "b"), ("ruim", "nada", "b"),
                      ("recorde", "ate14h", "a"), ("junho", "ate14h", "a")):
        d, _ = regime(KWP, KG, nd, nr, arq=k)
        print(f"| {nd} | {nr} | {k} | {d['carga']:.1f} | {d['prod']:.1f} | {d['falta']:.1f} | {d['smin']:.1f} | {d['tair_max']:.1f} | {d['test_max']:.1f} | {d['sobra']:.1f} | {d['aux_noite']:.2f} |")

    print("\n### Sensibilidades (dia recorde, ate 14 h, arquitetura b, 12 kWp + 700 kg): nao atendido kWh/dia | gelo minimo kWh")
    base = dict(UA_ENV=UA_ENV, RESP_10=RESP_10, TAU=TAU, PR=PR, ETA=ETA, K_COIL=K_COIL)
    for nome, var, val in (("base", None, None), ("UA 22 W/K (reefer bom ou painel)", "UA_ENV", 22.0), ("UA 40 W/K", "UA_ENV", 40.0),
                           ("respiracao 137 W/t (teto USDA)", "RESP_10", 137.0), ("respiracao 68 W/t", "RESP_10", 68.0),
                           ("constante de tempo 6 h", "TAU", 6.0), ("PR 0,70", "PR", 0.70), ("eficiencia 0,55", "ETA", 0.55),
                           ("eficiencia 0,65", "ETA", 0.65), ("serpentina com metade do K", "K_COIL", 450.0)):
        if var:
            globals()[var] = val
        ciclo.cache_clear()
        d, _ = regime(KWP, KG, "recorde", "ate14h")
        print(f"- {nome}: {d['falta']:.1f} | {d['smin']:.1f} | frio tirado {d['carga']:.1f} | ar max {d['tair_max']:.1f} C | pico serpentina {d['pico_serp']:.1f} kW")
        if var:
            globals()[var] = base[var]
    ciclo.cache_clear()

    print("\n## 5. Dias nublados seguidos (2,0 kWh/m2; 22-32 C) depois de dias quentes tipicos; recepcao normal ate 14 h continua")
    print("Criterio: polpa do estoque nao passa de 14 C e ar nao passa de 15 C.")

    def ok(r):
        return max(x["test_max"] for x in r) <= 14.0 and max(x["tair_max"] for x in r) <= 15.0

    def seq(n, kwp=KWP, kg=KG, bat=0.0, rec="ate14h", pmax=PMAX_FRAC * KWP):
        _, est = simula(kwp, kg, [("quente", "ate14h")] * 4, arq=AR, bat=bat, pmax=pmax)
        r, _ = simula(kwp, kg, [("nublado", rec)] * n, arq=AR, bat=bat, pmax=pmax, estado=est)
        return r

    cabec("dias nublados", "recepcao", "nao atendido total kWh", "polpa estoque max C", "ar max C", "atende?")
    for n in (1, 2, 3):
        for rec in ("ate14h", "meia", "nada"):
            r = seq(n, rec=rec)
            print(f"| {n} | {rec} | {sum(x['falta'] for x in r):.1f} | {max(x['test_max'] for x in r):.1f} | {max(x['tair_max'] for x in r):.1f} | {'sim' if ok(r) else 'NAO'} |")

    print("\n### Quanto falta acrescentar para atender (recepcao normal continuando), partindo de 12 kWp + 700 kg, sem bateria de apoio")
    cabec("dias nublados", "so mais gelo (kg totais)", "so mais bateria (kWh uteis)", "so mais painel (kWp totais)", "combinado: +2 kWp e bateria (kWh)", "combinado: +300 kg e bateria (kWh)")
    for n in (1, 2, 3):
        g = next((kg for kg in range(700, 4001, 100) if ok(seq(n, kg=kg))), None)
        bt = next((bb for bb in range(0, 151, 5) if ok(seq(n, bat=float(bb)))), None)
        pv = next((kw_ for kw_ in range(12, 41, 1) if ok(seq(n, kwp=kw_))), None)
        c1 = next((bb for bb in range(0, 151, 5) if ok(seq(n, kwp=14, bat=float(bb)))), None)
        c2 = next((bb for bb in range(0, 151, 5) if ok(seq(n, kg=1000, bat=float(bb)))), None)
        print(f"| {n} | {g} | {bt} | {pv} | {c1} | {c2} |")
    print("\n### Combinacoes conferidas (atende = polpa do estoque <= 14 C e ar <= 15 C)")
    cabec("kWp", "kg de gelo", "bateria de apoio kWh uteis", "recepcao nos dias nublados", "1 dia", "2 dias", "3 dias", "polpa max em 3 dias C")
    for kw_, kg_, bb, rec in ((10, 500, 0, "ate14h"), (10, 500, 5, "ate14h"), (12, 700, 0, "ate14h"), (12, 700, 5, "ate14h"), (12, 700, 10, "ate14h"),
                              (12, 700, 0, "meia"), (12, 700, 5, "meia"), (12, 700, 10, "meia"), (12, 700, 0, "nada"),
                              (14, 700, 0, "ate14h"), (14, 700, 5, "ate14h"), (14, 700, 15, "ate14h"), (14, 700, 0, "meia"), (14, 700, 5, "meia"),
                              (14, 1000, 0, "ate14h"), (14, 1000, 5, "ate14h"), (12, 1000, 0, "meia")):
        rs = [seq(n, kwp=kw_, kg=kg_, bat=float(bb), rec=rec) for n in (1, 2, 3)]
        print(f"| {kw_} | {kg_} | {bb} | {rec} | " + " | ".join("sim" if ok(r) else "NAO" for r in rs) + f" | {max(x['test_max'] for x in rs[2]):.1f} |")
    print("\nFrio que cada recurso entrega num dia nublado (referencia):")
    cn = cop(AR, 27.0)
    print(f"- 100 kg de gelo: {100 * L_GELO:.1f} kWh de frio, uma vez por sequencia")
    print(f"- 5,12 kWh de bateria (4,6 uteis): {4.6 * 0.95 * cn:.1f} kWh de frio por descarga (COP {cn:.2f} a 27 C)")
    print(f"- 1 kWp a mais: {2.0 * PR:.2f} kWh eletricos = {2.0 * PR * cn:.1f} kWh de frio em cada dia nublado; {5.8 * PR * cop(AR, 34):.1f} kWh em dia de sol (se houver onde guardar)")

    print("\n## 6. Banco de gelo")
    print("### 6.1 arquitetura b: serpentina de cobre com expansao direta, gelo por fora, agua circulando (fusao externa)")
    lam_g = 2.2
    for od, esp in ((0.015875, 0.025), (0.015875, 0.030), (0.0127, 0.025)):
        ro, rg = od / 2, od / 2 + esp
        kgm = math.pi * (rg ** 2 - ro ** 2) * 917
        L = KG / kgm
        R = math.log(rg / ro) / (2 * math.pi * lam_g) + 1 / (1500 * math.pi * (od - 0.0016))
        for dt_ in (6.0, 8.0):
            print(f"tubo {od * 1000:.1f} mm, gelo {esp * 1000:.0f} mm: {kgm:.2f} kg/m -> {L:.0f} m para {KG} kg; fim da carga com evaporacao a -{dt_:.0f} C: {L * dt_ / R / 1000:.1f} kW; "
                  f"volume interno {L * math.pi * (od - 0.0016) ** 2 / 4 * 1000:.1f} L")
    print(f"dilatacao: {KG}/917 - {KG}/1000 = {(KG / 917 - KG / 1000) * 1000:.0f} L; empuxo liquido do gelo: {(KG / 917) * (1000 - 917):.0f} kgf")
    print("### 6.2 arquitetura a: tubo PE-RT 16x2 com glicol por dentro (fusao interna), em espirais")
    r_i, r_o, esp = 0.006, 0.008, 0.010
    rg = r_o + esp
    kgm = math.pi * (rg ** 2 - r_o ** 2) * 917
    L = KG / kgm
    hin = 3.66 * 0.40 / (2 * r_i)
    R = 1 / (hin * 2 * math.pi * r_i) + math.log(r_o / r_i) / (2 * math.pi * 0.40) + math.log(rg / r_o) / (2 * math.pi * lam_g)
    dtlm = (6 - 2) / math.log(6 / 2)
    print(f"{L:.0f} m de tubo para {KG} kg; Nu 3,66 -> h {hin:.0f} W/m2K; R {R:.3f} m.K/W; media logaritmica (glicol -6/-2 C contra 0 C) {dtlm:.2f} K; potencia no fim da carga {L * dtlm / R / 1000:.1f} kW")
    passo = 0.040
    por_camada = math.pi * (0.72 ** 2 - 0.15 ** 2) / passo
    print(f"espiral em tanque redondo de 1,5 m: raio de 0,15 a 0,72 m, passo {passo * 1000:.0f} mm -> {por_camada:.1f} m por camada; {L / por_camada:.0f} camadas; altura do feixe {L / por_camada * passo:.2f} m")

    print("\n## 7. CO2 da respiracao (seguranca) e ar novo")
    for ml in (17.0, 22.0):
        co2 = 5000 * ml / 1e6     # m3/h
        print(f"5 t x {ml:.0f} ml/kg.h = {co2 * 1000:.0f} L/h de CO2; em 14 h fechada: {co2 * 14:.2f} m3 = {co2 * 14 / 15 * 100:.1f} % em 15 m3 de ar livre (sem renovacao)")
        for q in (5.0, 10.0, 20.0, 33.0):
            print(f"   com {q:.0f} m3/h de ar novo: equilibrio em {(co2 / q + 0.0004) * 100:.2f} %")
    dh = entalpia_ar(34, 0.30) - entalpia_ar(T_SET, 0.90)
    print(f"custo termico de 10 m3/h com ar a 34 C: {10 * 1.1 * dh / 3600 * 24:.1f} kWh/dia")

    print("\n## 7b. Umidade: ar a 12 C e 88 por cento tem ponto de orvalho de %.1f C" % (243.04 * (math.log(0.88) + 17.625 * 12 / 255.04) / (17.625 - math.log(0.88) - 17.625 * 12 / 255.04)))
    for tw_ in (3.0, 6.0):
        print(f"agua a {tw_} C, saindo a cerca de {tw_ + 4:.0f} C: superficie media da serpentina cerca de {tw_ + 3:.0f} C -> abaixo do orvalho em {10.0 - tw_ - 3:.0f} K")
    print("\n## 8. Serpentina de ar (agua gelada), conta de efetividade")
    for vaz_ar, ua_s, vaz_ag in ((6000, 2000, 1.4), (3000, 1400, 1.4), (1800, 1000, 0.7)):
        ca, cw = vaz_ar / 3600 * 1.2 * 1006, vaz_ag / 3.6 * 4190
        cmin, cmax = min(ca, cw), max(ca, cw)
        ntu, cr = ua_s / cmin, cmin / cmax
        eff = (1 - math.exp(-ntu * (1 - cr))) / (1 - cr * math.exp(-ntu * (1 - cr)))
        print(f"ar {vaz_ar} m3/h, UA {ua_s} W/K, agua {vaz_ag} m3/h: NTU {ntu:.2f}; efetividade {eff:.2f}; K = {eff * cmin:.0f} W/K; com ar a 12 C e agua a 3 C: {eff * cmin * 9 / 1000:.1f} kW")
    print(f"ventilador a 100 %: 6000 m3/h x 50 Pa / 0,35 = {6000 / 3600 * 50 / 0.35:.0f} W")
