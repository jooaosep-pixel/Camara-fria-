#!/usr/bin/env python3
"""
Contas hora a hora do projeto termico (docs/01-projeto-termico.md).
Rodar:  python3 docs/_trabalho/termico.py
Depende de: CoolProp (pip install CoolProp) para as propriedades do R290.

Tudo que esta marcado SUPOSTO aqui esta marcado [SUPOSTO] no documento.
"""
import math
from functools import lru_cache
from CoolProp.CoolProp import PropsSI

# ----------------------------------------------------------------- premissas
T_CAM = 10.0            # C  setpoint da camara (manga)            [premissa]
M_ESTOQUE = 4000.0      # kg fruta ja fria                          [premissa: 5 t total]
M_ENTRA = 1000.0        # kg/dia entrando                           [premissa]
T_FRUTA_IN = 30.0       # C                                         [premissa]
CP_FRUTA = 3.77         # kJ/kg.K (0,901 kcal/kg.C, fonte no doc)
CAIXAS_KG = 50 * 1.8    # 50 caixas plasticas de 1,8 kg             SUPOSTO
CP_CAIXA = 1.9          # kJ/kg.K (PEAD)                            SUPOSTO
TAU_FRUTA = 8.0         # h  constante de tempo do resfriamento em camara  SUPOSTO
RESP_10 = 77.0          # W/t MANGA a 10 C (14 ml CO2/kg.h, UC Davis; conversao no doc)
RESP_CAJU_5 = 60.0      # W/t CAJU a 5 C (20 mg CO2/kg.h)  SUPOSTO - nao achei dado medido
Q10 = 2.5               # fator por 10 K                            SUPOSTO

# CASOS: lista de zonas (fracao do involucro/volume, setpoint C, estoque frio kg, respiracao W/t no setpoint, fracao da fruta nova)
CASOS = {
    "manga10": [(1.0, 10.0, 4000.0, RESP_10, 1.0)],
    "manga12": [(1.0, 12.5, 4000.0, RESP_10 * Q10 ** 0.25, 1.0)],
    "caju5": [(1.0, 5.0, 4000.0, RESP_CAJU_5, 1.0)],
    "compromisso8": [(1.0, 8.0, 4000.0, 0.5 * RESP_10 * Q10 ** -0.2 + 0.5 * RESP_CAJU_5 * Q10 ** 0.3, 1.0)],
    # duas zonas: frente 60 % manga a 10 C (2,4 t paradas), fundo 40 % caju a 5 C (1,6 t paradas + 1 t nova de caju)
    "duas_zonas_caju_entra": [(0.6, 10.0, 2400.0, RESP_10, 0.0), (0.4, 5.0, 1600.0, RESP_CAJU_5, 1.0)],
    "duas_zonas_manga_entra": [(0.6, 10.0, 2400.0, RESP_10, 1.0), (0.4, 5.0, 1600.0, RESP_CAJU_5, 0.0)],
}

# involucros: UA total em W/K (ver secao 1 do doc)
UA = {"reefer_usado": 33.0, "reefer_novo": 22.0, "seco_isolado": 22.0, "painel_PIR100": 16.6}

V_INT = 28.0            # m3 volume interno (reefer 20')
TROCAS_DIA = 12.0       # trocas de ar/dia por abertura de porta    SUPOSTO
VENT_DIA_W, VENT_NOITE_W = 150.0, 50.0   # ventiladores EC do resfriador de ar  SUPOSTO
BOMBA_P2_W = 50.0       # bomba do circuito da camara (24 h)        SUPOSTO
BOMBA_P1_W = 260.0      # bomba de carga (so com compressor)        CALCULADO no doc
VENT_COND_W = 300.0     # ventiladores dos 2 condensadores                SUPOSTO
PESSOAS_W = 2 * 212.0   # 2 pessoas, 272-6*T W cada (ASHRAE)
LUZ_W = 40.0
GANHO_TANQUE_UA = 3.5   # W/K tanque de gelo + tubos isolados       CALCULADO no doc
FOLGA = 1.10            # fator de seguranca sobre a carga          SUPOSTO

PR = 0.75               # desempenho global FV (temperatura, sujeira, cabos, drive)  SUPOSTO
ETA_GLOBAL = 0.60       # eficiencia isentropica global (eletrica) do compressor+inversor SUPOSTO
DT_COND = 10.0          # K  condensacao acima do ar                SUPOSTO
T_EVAP_GELO = -10.0     # C  modo gelo (glicol -6/-3 C)
T_EVAP_CAM = -4.0       # C  modo so camara (glicol +1/+4 C)
L_GELO = 334.0 / 3600   # kWh/kg (334 kJ/kg)

HORAS = list(range(24))


# ------------------------------------------------------------------ funcoes
def t_amb(h, tmax=40.0, tmin=26.0):
    """Senoide: maxima as 15 h, minima as 3 h. SUPOSTO."""
    return (tmax + tmin) / 2 + (tmax - tmin) / 2 * math.cos(2 * math.pi * (h + 0.5 - 15) / 24)


@lru_cache(maxsize=None)
def irradiancia(h, H_dia, nascer=5.5, por=17.7):
    """kW/m2 medio na hora h, forma senoidal^1.3 normalizada para H_dia (kWh/m2.dia)."""
    def forma(x):
        return math.sin(math.pi * (x - nascer) / (por - nascer)) ** 1.3 if nascer < x < por else 0.0
    passo = 0.05
    tot = sum(forma(i * passo) * passo for i in range(int(24 / passo)))
    return H_dia * sum(forma(h + i * passo) * passo for i in range(int(1 / passo))) / tot


def entalpia_ar(t, ur, p=97.0):
    """kJ/kg ar seco. p = 97 kPa (Petrolina ~380 m)."""
    psat = 0.61094 * math.exp(17.625 * t / (t + 243.04))
    w = 0.622 * ur * psat / (p - ur * psat)
    return 1.006 * t + w * (2501 + 1.86 * t)


def cop_r290(t_evap, t_amb_c, sh=8.0, sc=3.0):
    return _cop(t_evap, round(t_amb_c, 1), sh, sc)


@lru_cache(maxsize=None)
def _cop(t_evap, t_amb_c, sh, sc):
    """COP eletrico do ciclo simples R290."""
    te, tc = t_evap + 273.15, max(t_amb_c + DT_COND, 30.0) + 273.15
    pe, pc = PropsSI("P", "T", te, "Q", 1, "R290"), PropsSI("P", "T", tc, "Q", 0, "R290")
    h1 = PropsSI("H", "T", te + sh, "P", pe, "R290")
    s1 = PropsSI("S", "T", te + sh, "P", pe, "R290")
    h2s = PropsSI("H", "P", pc, "S", s1, "R290")
    h4 = PropsSI("H", "T", tc - sc, "P", pc, "R290")
    rho1 = PropsSI("D", "T", te + sh, "P", pe, "R290")
    cop = (h1 - h4) / (h2s - h1) * ETA_GLOBAL
    return cop, pe / 1e5, pc / 1e5, (h1 - h4) / 1e3, rho1


def _zona(ua, frac, t_cam, estoque, resp_set, entra, h_entrada, tmax, tmin, dias_ant=3):
    out = []
    dh_ar = entalpia_ar(tmax - 3, 0.30) - entalpia_ar(t_cam, 0.90)   # kJ/kg
    e_infil = TROCAS_DIA * V_INT * frac * 1.1 * dh_ar / 3600          # kWh/dia
    for h in HORAS:
        ta = t_amb(h, tmax, tmin)
        sol = 2.0 if 7 <= h <= 16 else 0.0      # K: paredes ao sol, teto sombreado pelos paineis SUPOSTO
        q_trans = ua * frac * (ta + sol - t_cam) / 1000
        q_inf = 0.0
        if entra > 0 and h in (h_entrada, (h_entrada + 1) % 24):
            q_inf += 0.5 * e_infil / 2
        if 6 <= h < 18:
            q_inf += 0.5 * e_infil / 12
        q_campo = q_resp_extra = 0.0
        for d in range(dias_ant + 1):
            dt0 = h - h_entrada + 24 * d
            if dt0 < 0 or entra == 0:
                continue
            e0 = math.exp(-dt0 / TAU_FRUTA)
            e1 = math.exp(-(dt0 + 1) / TAU_FRUTA)
            cap = (entra * CP_FRUTA + CAIXAS_KG * CP_CAIXA) * (T_FRUTA_IN - t_cam) / 3600  # kWh
            q_campo += cap * (e0 - e1)
            t_med = t_cam + (T_FRUTA_IN - t_cam) * (e0 + e1) / 2
            q_resp_extra += entra / 1000 * resp_set * (Q10 ** ((t_med - t_cam) / 10) - 1) / 1000
        q_resp = (estoque + entra) / 1000 * resp_set / 1000 + q_resp_extra
        dia = 6 <= h < 18
        q_vent = frac * (VENT_DIA_W if dia else VENT_NOITE_W) / 1000
        q_pes = PESSOAS_W / 1000 if (entra > 0 and h == h_entrada) else (frac * PESSOAS_W / 2000 if h in (8, 14) else 0)
        q_luz = frac * LUZ_W / 1000 if (h == h_entrada or h in (8, 14)) else 0
        q_bomba = frac * BOMBA_P2_W / 1000
        q_tanque = frac * GANHO_TANQUE_UA * (ta - 0) / 1000
        out.append(dict(trans=q_trans, infil=q_inf, campo=q_campo, resp=q_resp, vent=q_vent,
                        pessoas=q_pes, luz=q_luz, bomba=q_bomba, tanque=q_tanque))
    return out


@lru_cache(maxsize=None)
def _carga(inv, h_entrada, tmax, tmin, caso, entra):
    zonas = [_zona(UA[inv], f, tc, est, rs, entra * fe, h_entrada, tmax, tmin) for (f, tc, est, rs, fe) in CASOS[caso]]
    out = []
    for h in HORAS:
        parc = {k: sum(z[h][k] for z in zonas) for k in zonas[0][h]}
        parc["total"] = sum(parc.values()) * FOLGA
        parc["tamb"] = t_amb(h, tmax, tmin)
        out.append(parc)
    return out


def carga_horaria(inv, h_entrada, tmax, tmin, caso="manga10", entra=M_ENTRA):
    """24 dicts com as parcelas da carga em kW, em regime periodico (soma a fruta dos dias anteriores)."""
    return _carga(inv, h_entrada, tmax, tmin, caso, entra)


def simula(kwp, kg_gelo, cenarios, inv="reefer_usado", h_entrada=17, pmax_frac=0.62,
           pmin_frac=0.215, s0=None, caso="manga10"):
    """cenarios: lista de (H_dia, tmax, tmin, entra_kg) - um por dia, em sequencia.
    Devolve resumo por dia. Estoque S em kWh de frio (0 = sem gelo)."""
    cap = kg_gelo * L_GELO
    s = cap if s0 is None else s0
    pmax, pmin = pmax_frac * kwp, pmin_frac * pmax_frac * kwp
    res = []
    for (H, tmax, tmin, entra) in cenarios:
        cargas = carga_horaria(inv, h_entrada, tmax, tmin, caso, entra)
        d = dict(H=H, carga=0, prod=0, e_fv=0, e_comp=0, corte=0, deficit=0, smin=s, linhas=[])
        for h in HORAS:
            c = cargas[h]
            p_fv = kwp * irradiancia(h, H) * PR
            p_disp = p_fv - (VENT_COND_W + BOMBA_P1_W) / 1000
            cop = cop_r290(T_EVAP_GELO, c["tamb"])[0]
            p_comp = min(p_disp, pmax) if p_disp >= pmin else 0.0
            q_prod = p_comp * cop
            # tanque cheio: compressor modula para so atender a camara
            if s + q_prod - c["total"] > cap:
                q_prod = max(0.0, cap - s + c["total"])
                p_comp = q_prod / cop
            s_novo = s + q_prod - c["total"]
            deficit = 0.0
            if s_novo < 0:
                deficit, s_novo = -s_novo, 0.0
            d["carga"] += c["total"]; d["prod"] += q_prod; d["e_fv"] += p_fv
            d["e_comp"] += p_comp; d["corte"] += max(0, p_disp - p_comp) if p_disp > 0 else 0
            d["deficit"] += deficit
            s = s_novo
            d["smin"] = min(d["smin"], s)
            d["linhas"].append((h, c["tamb"], p_fv, p_comp, cop, q_prod, c["total"], s, deficit))
        d["sfim"] = s
        res.append(d)
    return res


def tabela_carga(inv, h_entrada, tmax=40, tmin=26, caso="manga10", titulo=""):
    cargas = carga_horaria(inv, h_entrada, tmax, tmin, caso)
    print(f"\n### Carga hora a hora - {titulo} (kW)")
    print("| h | Tamb | transm | infiltr | campo | respir | ventil | pessoas+luz | bomba+tanque | TOTAL c/ folga |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    tot = {k: 0.0 for k in cargas[0]}
    for h, c in enumerate(cargas):
        for k in c:
            tot[k] += c[k]
        print(f"| {h:02d} | {c['tamb']:.1f} | {c['trans']:.2f} | {c['infil']:.2f} | {c['campo']:.2f} | "
              f"{c['resp']:.2f} | {c['vent']:.2f} | {c['pessoas'] + c['luz']:.2f} | "
              f"{c['bomba'] + c['tanque']:.2f} | {c['total']:.2f} |")
    print(f"| **kWh/dia** | | {tot['trans']:.1f} | {tot['infil']:.1f} | {tot['campo']:.1f} | {tot['resp']:.1f} | "
          f"{tot['vent']:.1f} | {tot['pessoas'] + tot['luz']:.1f} | {tot['bomba'] + tot['tanque']:.1f} | "
          f"**{tot['total']:.1f}** |")
    noite = sum(cargas[h]["total"] for h in HORAS if h >= 17 or h < 7)
    print(f"\nCarga das 17 h as 7 h (14 h sem sol util): {noite:.1f} kWh  -> gelo equivalente {noite / L_GELO:.0f} kg")
    return tot, noite


def periodico(kwp, kg, cen, n=6, **kw):
    """repete o mesmo dia n vezes e devolve o ultimo (regime)."""
    return simula(kwp, kg, [cen] * n, **kw)[-1]


if __name__ == "__main__":
    print("## 0. Ciclo R290 (CoolProp %s)" % __import__("CoolProp").__version__)
    print("| modo | Tevap C | Tamb C | Tcond C | p_evap bar | p_cond bar | efeito frig. kJ/kg | dens. succao kg/m3 | COP eletrico |")
    print("|---|---|---|---|---|---|---|---|---|")
    for modo, te in (("gelo", T_EVAP_GELO), ("camara", T_EVAP_CAM)):
        for ta in (26, 33, 40, 43):
            cop, pe, pc, dh, rho = cop_r290(te, ta)
            print(f"| {modo} | {te:.0f} | {ta} | {max(ta + DT_COND, 30):.0f} | {pe:.2f} | {pc:.2f} | {dh:.0f} | {rho:.2f} | {cop:.2f} |")
    cop, pe, pc, dh, rho = cop_r290(T_EVAP_GELO, 40)
    for qf in (8.0, 10.0, 12.0):
        m = qf / dh
        print(f"Q={qf:.0f} kW a -10/+50: vazao massica {m * 3600:.0f} kg/h; volume aspirado {m / rho * 3600:.1f} m3/h; "
              f"deslocamento necessario com rend. vol. 0,75: {m / rho * 3600 / 0.75:.1f} m3/h; potencia {qf / cop:.2f} kW")

    print("\n## 1. Cargas")
    tabela_carga("reefer_usado", 17, caso="manga10", titulo="reefer usado, tudo manga a 10 C, fruta entra as 17 h")
    tabela_carga("reefer_usado", 17, caso="caju5", titulo="CASO DE DIMENSIONAMENTO: reefer usado, tudo a 5 C (caju), fruta entra as 17 h (pior horario)")
    tabela_carga("reefer_usado", 7, caso="caju5", titulo="CASO DE DIMENSIONAMENTO: reefer usado, tudo a 5 C (caju), fruta entra as 7 h (melhor horario)")

    def noite(c):
        return sum(c[h]["total"] for h in HORAS if h >= 17 or h < 7)

    print("\n### Carga diaria por caso de fruta e involucro (kWh/dia; Tamb 26-40 C; 1 t/dia a 30 C)")
    print("| caso | reefer usado 33 W/K | reefer novo ou seco isolado 22 W/K | painel PIR 100 mm 16,6 W/K | noite 17-7 h, entrada 17 h (reefer usado) | noite 17-7 h, entrada 7 h (reefer usado) |")
    print("|---|---|---|---|---|---|")
    for caso in CASOS:
        l = [sum(c["total"] for c in carga_horaria(inv, 17, 40, 26, caso)) for inv in ("reefer_usado", "reefer_novo", "painel_PIR100")]
        print(f"| {caso} | {l[0]:.1f} | {l[1]:.1f} | {l[2]:.1f} | {noite(carga_horaria('reefer_usado', 17, 40, 26, caso)):.1f} | {noite(carga_horaria('reefer_usado', 7, 40, 26, caso)):.1f} |")

    PROJ = (5.8, 40, 26, M_ENTRA)
    print("\n## 2. Os numeros do dono: 5 kWp + 200 kg de gelo (reefer usado, dia de projeto H=5,8, 26-40 C)")
    for caso in ("manga10", "caju5"):
        for he in (17, 7):
            d = periodico(5, 200, PROJ, h_entrada=he, caso=caso)
            print(f"{caso}, entrada {he:02d} h: carga {d['carga']:.1f} kWh | frio produzido {d['prod']:.1f} kWh | "
                  f"FV {d['e_fv']:.1f} kWh | deficit {d['deficit']:.1f} kWh/dia")

    gelos = (200, 400, 500, 600, 700, 800, 900, 1000, 1200)
    kwps = (5, 8, 10, 11, 12, 13, 14, 16)
    for caso, inv in (("caju5", "reefer_usado"), ("caju5", "painel_PIR100"), ("manga10", "reefer_usado")):
        for he in (17, 7):
            print(f"\n## 3. Varredura: deficit (kWh/dia) em regime - {caso}, {inv}, dia de projeto, entrada as {he} h")
            print("| kWp \\ kg gelo | " + " | ".join(str(g) for g in gelos) + " |")
            print("|---|" + "---|" * len(gelos))
            for kwp in kwps:
                print(f"| {kwp} | " + " | ".join(f"{periodico(kwp, g, PROJ, h_entrada=he, caso=caso, inv=inv)['deficit']:.1f}" for g in gelos) + " |")

    KWP, KG, CASO = 12, 800, "caju5"
    print(f"\n## 4. Projeto escolhido: {KWP} kWp + {KG} kg de gelo ({KG * L_GELO:.1f} kWh), 2 compressores somando ate {0.62 * KWP:.1f} kW eletricos (minimo de partida {0.215 * 0.62 * KWP:.1f} kW), caso {CASO}")
    for he in (17, 7):
        d = periodico(KWP, KG, PROJ, caso=CASO, h_entrada=he)
        print(f"\n### Balanco hora a hora, dia de projeto em regime, fruta as {he} h")
        print("| h | Tamb | FV kW | compressor kW | COP | frio produzido kW | carga kW | estoque de gelo kWh (fim da hora) | falta kWh |")
        print("|---|---|---|---|---|---|---|---|---|")
        for (h, ta, pfv, pc_, cop, qp, ct, s_, df) in d["linhas"]:
            print(f"| {h:02d} | {ta:.1f} | {pfv:.2f} | {pc_:.2f} | {cop:.2f} | {qp:.2f} | {ct:.2f} | {s_:.1f} | {df:.1f} |")
        print(f"| **dia** | | {d['e_fv']:.1f} kWh | {d['e_comp']:.1f} kWh | {d['prod'] / max(d['e_comp'], 1e-9):.2f} | {d['prod']:.1f} kWh | {d['carga']:.1f} kWh | min {d['smin']:.1f} | {d['deficit']:.1f} |")
        print(f"energia FV nao aproveitada (tanque cheio, acima do maximo ou abaixo do minimo do compressor): {d['corte']:.1f} kWh")

    print("\n### Cenarios com o projeto escolhido (em regime, mesmo dia repetido)")
    print("| cenario | caso | H kWh/m2 | Tmax | entrada | carga kWh | frio produzido kWh | falta kWh/dia | estoque min kWh | estoque fim kWh |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    cen = [("projeto, pior horario", "caju5", (5.8, 40, 26, 1000), 17), ("projeto, melhor horario", "caju5", (5.8, 40, 26, 1000), 7),
           ("duas zonas, entra caju", "duas_zonas_caju_entra", (5.8, 40, 26, 1000), 17),
           ("duas zonas, entra manga", "duas_zonas_manga_entra", (5.8, 40, 26, 1000), 17),
           ("so manga 10 C", "manga10", (5.8, 40, 26, 1000), 17),
           ("junho medio", "caju5", (4.7, 32, 20, 1000), 17), ("junho medio, manha", "caju5", (4.7, 32, 20, 1000), 7),
           ("irradiacao -10 %", "caju5", (5.2, 40, 26, 1000), 17), ("irradiacao -10 %, manha", "caju5", (5.2, 40, 26, 1000), 7),
           ("irradiacao +10 %", "caju5", (6.4, 40, 26, 1000), 17),
           ("dia ruim repetido, 17 h", "caju5", (3.0, 36, 24, 1000), 17),
           ("dia ruim repetido", "caju5", (3.0, 36, 24, 1000), 7), ("dia ruim repetido, meia carga 0,5 t", "caju5", (3.0, 36, 24, 500), 7),
           ("dia ruim repetido, sem fruta nova", "caju5", (3.0, 36, 24, 0), 7)]
    for nome, caso, c, he in cen:
        d = periodico(KWP, KG, c, h_entrada=he, caso=caso)
        print(f"| {nome} | {caso} | {c[0]} | {c[1]} | {he} h | {d['carga']:.1f} | {d['prod']:.1f} | {d['deficit']:.1f} | {d['smin']:.1f} | {d['sfim']:.1f} |")

    print("\n### Sequencia: 2 dias de projeto, 3 dias nublados (H=2,0; 24-34 C), 2 dias de projeto - caso caju5")
    for rot, entra_nub, he in (("fruta continua entrando as 17 h", 1000, 17), ("fruta entra as 7 h e continua nos nublados", 1000, 7),
                               ("fruta entra as 7 h, suspensa nos nublados", 0, 7)):
        seq = [(5.8, 40, 26, 1000)] * 2 + [(2.0, 34, 24, entra_nub)] * 3 + [(5.8, 40, 26, 1000)] * 2
        r = simula(KWP, KG, seq, h_entrada=he, caso=CASO)
        print(f"\n{rot}:")
        print("| dia | H | carga kWh | frio produzido kWh | falta kWh | estoque min kWh | estoque fim kWh |")
        print("|---|---|---|---|---|---|---|")
        for i, d in enumerate(r, 1):
            print(f"| {i} | {d['H']} | {d['carga']:.1f} | {d['prod']:.1f} | {d['deficit']:.1f} | {d['smin']:.1f} | {d['sfim']:.1f} |")

    print("\n### Autonomia real do tanque cheio, sem sol nenhum, sem fruta nova (Tamb 24-36 C)")
    for caso in ("caju5", "manga10", "duas_zonas_caju_entra"):
        c = carga_horaria("reefer_usado", 17, 36, 24, caso, 0)
        med = sum(x["total"] for x in c) / 24
        print(f"- {caso}: carga media {med:.2f} kW -> {KG * L_GELO / med:.0f} h com {KG} kg; 200 kg dariam {200 * L_GELO / med:.0f} h")
    print(f"- inercia da fruta: 5 t x {CP_FRUTA} kJ/kg.K = {5000 * CP_FRUTA / 3600:.1f} kWh por K de subida")

    print("\n### Pico de carga do resfriador de ar (kW) e respiracao do caju em dobro")
    for caso in ("caju5", "manga10"):
        print(f"- {caso}: pico horario {max(c['total'] for c in carga_horaria('reefer_usado', 17, 40, 26, caso)):.1f} kW")
    c = carga_horaria("reefer_usado", 17, 40, 26, "caju5")
    print(f"- se a respiracao do caju for o dobro do suposto: +{sum(x['resp'] for x in c) * FOLGA:.1f} kWh/dia")

    print("\n## 5. Serpentina do tanque (PE-RT/PEX 16x2 mm, gelo crescendo por fora, glicol por dentro)")
    lam_pe, lam_gelo = 0.40, 2.2
    r_i, r_o = 0.006, 0.008
    vaz = 3.2 / 3600          # m3/s total na carga (14 kW, dT 4 K)
    nu_glicol, k_glicol, rho_g = 8e-6, 0.40, 1040.0   # propilenoglicol 35 % a -5 C  SUPOSTO (valores tipicos)
    for esp, ncirc in ((0.010, 22), (0.015, 12), (0.020, 8)):
        r_g = r_o + esp
        kg_m = math.pi * (r_g ** 2 - r_o ** 2) * 917
        comp = KG / kg_m
        v = vaz / ncirc / (math.pi * r_i ** 2)
        re = v * 2 * r_i / nu_glicol
        nu = 4.36 if re < 2300 else 0.023 * re ** 0.8 * 50 ** 0.4
        h_int = nu * k_glicol / (2 * r_i)
        R = 1 / (h_int * 2 * math.pi * r_i) + math.log(r_o / r_i) / (2 * math.pi * lam_pe) + math.log(r_g / r_o) / (2 * math.pi * lam_gelo)
        lc = comp / ncirc
        dp = (64 / re if re < 2300 else 0.316 / re ** 0.25) * lc / (2 * r_i) * rho_g * v ** 2 / 2 / 1000
        passo = 2 * r_g + 0.004
        print(f"gelo {esp * 1000:.0f} mm, {ncirc} circuitos: {comp:.0f} m no total ({lc:.0f} m/circuito); v={v:.2f} m/s; Re={re:.0f}; "
              f"h_int={h_int:.0f} W/m2K; R={R:.3f} m.K/W; potencia no fim da carga com glicol medio a -4,5 C: {comp * 4.5 / R / 1000:.1f} kW; "
              f"perda de carga {dp:.0f} kPa; passo entre tubos {passo * 1000:.0f} mm; volume do feixe {comp * passo ** 2:.2f} m3")
    print(f"gelo: {KG} kg = {KG / 917:.2f} m3; dilatacao ao congelar (9 %): {KG / 917 * 0.09 * 1000:.0f} L -> subida de nivel que serve de medidor de gelo")
