# -*- coding: utf-8 -*-
"""Roda todos os cenarios e imprime as tabelas que vao para o LEIAME.

Uso:  python3 cenarios.py            (imprime e grava resultados.txt)
"""

import os
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import sim       # noqa: E402
import config    # noqa: E402

H = 3600.0
DIA = 86400.0

CONFIGS = [
    ("B 12 kWp + 700 kg + 5 kWh", dict(rota="B", kwp=12, gelo_kg=700)),
    ("B 10 kWp + 500 kg + 5 kWh", dict(rota="B", kwp=10, gelo_kg=500)),
    ("B 11 kWp + 500 kg + 5 kWh", dict(rota="B", kwp=11, gelo_kg=500)),
    ("B 12 kWp + 700 kg + 10 kWh (5 aux + 5 apoio)", dict(rota="B", kwp=12, gelo_kg=700, bateria_kwh_util=9.2)),
    ("A 12 kWp + 700 kg + 15 kWh", dict(rota="A", kwp=12, gelo_kg=700)),
    ("A 10 kWp + 500 kg + 10 kWh", dict(rota="A", kwp=10, gelo_kg=500, bateria_kwh_util=9.0)),
]

AQUEC = [sim.dia(sim.TIPICO)] * 3


def cfg_de(p):
    p = dict(p)
    return config.montar(p.pop("rota"), kwp=p.pop("kwp"), gelo_kg=p.pop("gelo_kg"), **p)


def f1(x):
    return "-" if x is None else ("%.1f" % x)


def linha(cols):
    return "| " + " | ".join(str(c) for c in cols) + " |"


def cab(cols):
    return linha(cols) + "\n" + linha(["---"] * len(cols))


def cen_tipico(out):
    out.append("### C1 - Dia tipico (23-34 C, 5,8 kWh/m2, 1 t a 35 C entre 10 h e 14 h); 4o dia de uma sequencia\n")
    out.append(cab(["Conjunto", "Ar max/min (C)", "Polpa estoque max (C)", "Lote de ontem as 9h30 (C)",
                    "Gelo min (%)", "Bateria min (%)", "CO2 max (%)", "Frio produzido (kWh)",
                    "Serpentina (kWh)", "FV disp./usada (kWh)", "Partidas/h max", "Paradas curtas", "Recebido (kg)"]))
    for nome, p in CONFIGS:
        r = sim.rodar(cfg_de(p), AQUEC + [sim.dia(sim.TIPICO)])
        d = r["dias"][-1]
        out.append(linha([nome, "%s / %s" % (f1(d["ar_max"]), f1(d["ar_min"])), f1(d["estoque_max"]),
                          f1(d.get("lote_ontem_0930")), f1(d["gelo_min"]), f1(d["soc_min"]), "%.2f" % d["co2_max"],
                          f1(d["frio_kwh"]), f1(d["serp_kwh"]),
                          "%s / %s" % (f1(d["pv_disp_kwh"]), f1(d["pv_usado_kwh"])),
                          d["partidas_h_max"], d["paradas_curtas"], int(d["recebido_kg"])]))
    cfg = config.montar("B", kwp=12, gelo_kg=700, barramento_comum=False)
    r = sim.rodar(cfg, AQUEC + [sim.dia(sim.TIPICO)])
    d = r["dias"][-1]
    out.append(linha(["B 12+700, sensibilidade: 2 grupos de 6 kWp separados", "%s / %s" % (f1(d["ar_max"]), f1(d["ar_min"])),
                      f1(d["estoque_max"]), f1(d.get("lote_ontem_0930")), f1(d["gelo_min"]), f1(d["soc_min"]),
                      "%.2f" % d["co2_max"], f1(d["frio_kwh"]), f1(d["serp_kwh"]),
                      "%s / %s" % (f1(d["pv_disp_kwh"]), f1(d["pv_usado_kwh"])), d["partidas_h_max"],
                      d["paradas_curtas"], int(d["recebido_kg"])]))
    out.append("")


def cen_recorde(out):
    out.append("### C2 - Dia de 41 C (27-41 C) com 1 t de uma vez as 13 h, e o dia seguinte (41 C, entrega normal)\n")
    out.append(cab(["Conjunto", "Ar max (C)", "Polpa estoque max (C)", "Lote das 13 h no fim do dia (C)",
                    "Lote das 13 h as 9h30 do dia seguinte (C)", "Gelo min dia 1 / dia 2 (%)",
                    "Bateria min (%)", "Frio produzido dia 1 (kWh)", "Serpentina dia 1 (kWh)", "Alarmes"]))
    for nome, p in CONFIGS:
        r = sim.rodar(cfg_de(p), AQUEC + [sim.dia(sim.RECORDE, [(13.0, 1000.0, 35.0)]), sim.dia(sim.RECORDE)])
        d1, d2 = r["dias"][-2], r["dias"][-1]
        out.append(linha([nome, f1(max(d1["ar_max"], d2["ar_max"])), f1(max(d1["estoque_max"], d2["estoque_max"])),
                          f1(d1["lote_fim_dia"]), f1(d2.get("lote_ontem_0930")),
                          "%s / %s" % (f1(d1["gelo_min"]), f1(d2["gelo_min"])),
                          f1(min(d1["soc_min"], d2["soc_min"])), f1(d1["frio_kwh"]), f1(d1["serp_kwh"]),
                          ",".join(d1["alarmes_fim"] + d2["alarmes_fim"]) or "nenhum"]))
    out.append("")


def cen_nublados(out):
    out.append("### C3 - 1, 2 e 3 dias nublados seguidos (22-32 C, 2,0 kWh/m2), depois 2 dias tipicos; "
               "o operador segue o aviso de recepcao\n")
    out.append(cab(["Conjunto", "Dias nublados", "Avisos 6h30/10h30 por dia (N=normal, M=meia, X=nao receber)",
                    "Recebido por dia (kg)", "Ar max (C)", "Polpa estoque max (C)", "Gelo min (%)",
                    "Bateria min (%)", "Apagoes", "Atende? (polpa <= 14 C e ar <= 15 C)"]))
    ab = {"RECEBER_NORMAL": "N", "MEIA_CARGA": "M", "NAO_RECEBER": "X", None: "-"}
    for nome, p in CONFIGS:
        for n in (1, 2, 3):
            dias = AQUEC + [sim.dia(sim.NUBLADO)] * n + [sim.dia(sim.TIPICO)] * 2
            r = sim.rodar(cfg_de(p), dias)
            ds = r["dias"][3:]
            av = " ".join("%s%s" % (ab[d["aviso_0630"]], ab[d["aviso_1000"]]) for d in ds)
            rec = "/".join(str(int(d["recebido_kg"])) for d in ds)
            arx = max(d["ar_max"] for d in ds)
            ex = max(d["estoque_max"] for d in ds)
            out.append(linha([nome, n, av, rec, f1(arx), f1(ex), f1(min(d["gelo_min"] for d in ds)),
                              f1(min(d["soc_min"] for d in ds)), int(sum(d.get("apagoes", 0) for d in ds)),
                              "sim" if (ex <= 14.0 and arx <= 15.0) else "NAO"]))
    out.append("")
    out.append("#### C3b - Mesmo cenario, mas o operador IGNORA o aviso e recebe 1 t todo dia (efeito da regra)\n")
    out.append(cab(["Conjunto", "Dias nublados", "Recebido por dia (kg)", "Ar max (C)", "Polpa estoque max (C)",
                    "Gelo min (%)", "Atende?"]))
    for nome, p in CONFIGS[:1] + CONFIGS[4:5]:
        for n in (2, 3):
            dias = AQUEC + [sim.dia(sim.NUBLADO)] * n + [sim.dia(sim.TIPICO)] * 2
            r = sim.rodar(cfg_de(p), dias, operador_segue_aviso=False)
            ds = r["dias"][3:]
            arx = max(d["ar_max"] for d in ds)
            ex = max(d["estoque_max"] for d in ds)
            out.append(linha([nome, n, "/".join(str(int(d["recebido_kg"])) for d in ds), f1(arx), f1(ex),
                              f1(min(d["gelo_min"] for d in ds)), "sim" if (ex <= 14.0 and arx <= 15.0) else "NAO"]))
    out.append("")


def cen_falhas(out):
    out.append("### C4 - Falhas de sensor e de comunicacao (Rota B 12 kWp + 700 kg, salvo indicacao); "
               "falha do 4o dia (tipico) as 10 h ate o fim do 5o dia\n")
    out.append(cab(["Falha", "Ar max/min (C)", "Polpa estoque max (C)", "Gelo min (%)", "Alarmes gerados",
                    "Comportamento observado"]))
    base = [sim.dia(sim.TIPICO)] * 5
    j = [(3 * DIA + 10 * H, 5 * DIA)]
    casos = [
        ("Nenhuma (referencia)", "B", {}, ""),
        ("TT1 (ar da camara)", "B", {"TT1": j}, "controla pela polpa TT2 - 0,8 K"),
        ("TT1 e TT2 juntos", "B", {"TT1": j, "TT2": j}, "ventilador no minimo, agua 8 C (sem risco de dano por frio)"),
        ("LT1 (nivel do gelo)", "B", {"LT1": j}, "carga ate a sonda de espessura EI1 (ou sucao baixa); aviso meia carga"),
        ("CO2", "B", {"CO2": j}, "ar novo no maximo (60 m3/h), luz vermelha"),
        ("G (irradiancia)", "B", {"G": j}, "partida so na janela 9-15 h; o inversor desarma se faltar sol"),
        ("PT1 do compressor 1", "B", {"PT1": j}, "compressor 1 bloqueado; o 2 continua"),
        ("Comunicacao com o inversor hibrido (Rota A)", "A", {"com_inversor": j}, "sem SOC: so com sol forte 9-15 h"),
    ]
    for nome, rota, fs, desc in casos:
        p = dict(CONFIGS[0][1] if rota == "B" else CONFIGS[4][1])
        cfg = cfg_de(p)
        if "PT1" in fs:
            r = _rodar_pt1(cfg, base, j)
        else:
            r = sim.rodar(cfg, base, falhas_sensor=fs)
        ds = r["dias"][3:]
        cods = sorted(set(ev["cod"] for ev in _eventos(r)))
        out.append(linha([nome, "%s / %s" % (f1(max(d["ar_max"] for d in ds)), f1(min(d["ar_min"] for d in ds))),
                          f1(max(d["estoque_max"] for d in ds)), f1(min(d["gelo_min"] for d in ds)),
                          ", ".join(cods) or "nenhum", desc]))
    out.append("")


def _eventos(r):
    return r["eventos"]


def _rodar_pt1(cfg, base, j):
    """PT1 do compressor 1 em falha: injeta None so nesse sensor."""
    import planta
    orig = planta.Planta.entradas

    def ent(self, t, hora, dia, falhos=(), com=True):
        e = orig(self, t, hora, dia, falhos, com)
        if j[0][0] <= t < j[0][1]:
            e["comp"][0]["PT1"] = None
        return e
    planta.Planta.entradas = ent
    try:
        return sim.rodar(cfg, base)
    finally:
        planta.Planta.entradas = orig


def cen_internet(out):
    out.append("### C5 - Queda de internet por 24 h (do 2o dia 8 h ao 3o dia 8 h), Rota B 12 kWp + 700 kg\n")
    cfg = cfg_de(CONFIGS[0][1])
    dias = [sim.dia(sim.TIPICO)] * 4
    fs = {"CO2": [(1 * DIA + 12 * H, 1 * DIA + 13 * H)]}   # um alarme durante a queda
    r0 = sim.rodar(cfg, dias, registrar=True, falhas_sensor=fs)
    r1 = sim.rodar(cfg, dias, registrar=True, falhas_sensor=fs, internet_off=[(1 * DIA + 8 * H, 2 * DIA + 8 * H)])
    iguais = r0["saidas"] == r1["saidas"]
    t1 = r1["tel"]
    out.append(cab(["Item", "Resultado"]))
    out.append(linha(["Saidas do controlador identicas com e sem internet (%d passos comparados)" % len(r0["saidas"]),
                      "SIM" if iguais else "NAO"]))
    out.append(linha(["Registros de 5 min gerados / enviados ao fim", "%d / %d" % (t1.enviados_reg + len(t1.fila_reg), t1.enviados_reg)]))
    out.append(linha(["Alertas gerados / enviados ao fim", "%d / %d" % (t1.enviados_evt + len(t1.fila_evt), t1.enviados_evt)]))
    out.append(linha(["Registros descartados por fila cheia", t1.descartados]))
    out.append(linha(["Alertas recebidos no celular (hora do envio -> texto)",
                      "; ".join("%02d:%02d dia %d -> %s" % (int(t % DIA // H), int(t % H // 60), int(t // DIA) + 1, x)
                                for t, x in t1.mensagens)]))
    out.append(linha(["Temperatura do ar max nos 4 dias (com / sem internet)",
                      "%s / %s C" % (f1(max(d["ar_max"] for d in r0["dias"])), f1(max(d["ar_max"] for d in r1["dias"])))]))
    out.append("")


def cen_extra(out):
    out.append("### C6 - Outras falhas (Rota B 12 kWp + 700 kg salvo indicacao)\n")
    out.append(cab(["Caso", "Ar max (C)", "Polpa estoque max (C)", "Gelo min (%)", "Bateria min (%)",
                    "Apagoes", "Observacao"]))
    cfg = cfg_de(CONFIGS[0][1])
    dias = [sim.dia(sim.TIPICO)] * 5
    # controlador parado 24 h (watchdog -> estado seguro de hardware)
    r = sim.rodar(cfg, dias, controlador_off=[(3 * DIA, 4 * DIA)])
    ds = r["dias"][3:]
    out.append(linha(["Controlador parado 24 h no 4o dia (rele de watchdog cai)",
                      f1(max(d["ar_max"] for d in ds)), f1(max(d["estoque_max"] for d in ds)),
                      f1(min(d["gelo_min"] for d in ds)), f1(min(d["soc_min"] for d in ds)),
                      int(sum(d.get("apagoes", 0) for d in ds)),
                      "compressores parados; bomba e ventiladores fixos pelo contato NF; fruta recebida normalmente"]))
    # ventilador do condensador queimado num dia de 41 C
    dias41 = [sim.dia(sim.TIPICO)] * 3 + [sim.dia(sim.RECORDE)] * 2
    r = sim.rodar(cfg, dias41, falha_vent_cond=[(3 * DIA + 9 * H, 4 * DIA + 18 * H)])
    ds = r["dias"][3:]
    psh = r["planta"].psh_aberto
    bloq = [c.estado for c in r["ctl"].comps]
    out.append(linha(["Ventilador do condensador parado (41 C, 9 h do 4o dia ao fim do 5o)",
                      f1(max(d["ar_max"] for d in ds)), f1(max(d["estoque_max"] for d in ds)),
                      f1(min(d["gelo_min"] for d in ds)), f1(min(d["soc_min"] for d in ds)), 0,
                      "software bloqueia por alta (16,5 bar) antes do PSH de hardware (18 bar): PSH aberto=%s; estado final=%s" % (psh, bloq)]))
    # Starlink Standard x Mini em 3 dias nublados, so com a bateria de 5 kWh
    for nome_s, w in (("Mini (30 W)", 30.0), ("Standard V4 (87 W)", 87.0)):
        dn = [sim.dia(sim.TIPICO)] * 3 + [sim.dia(sim.NUBLADO)] * 3 + [sim.dia(sim.TIPICO)]
        r = sim.rodar(cfg, dn, starlink_w=w)
        ds = r["dias"][3:]
        out.append(linha(["3 dias nublados com Starlink %s, bateria 5 kWh" % nome_s,
                          f1(max(d["ar_max"] for d in ds)), f1(max(d["estoque_max"] for d in ds)),
                          f1(min(d["gelo_min"] for d in ds)), f1(min(d["soc_min"] for d in ds)),
                          int(sum(d.get("apagoes", 0) for d in ds)),
                          "auxiliares a noite: %s kWh (media dos dias)" % f1(sum(d["aux_noite_kwh"] for d in ds) / len(ds))]))
    out.append("")


def main():
    t0 = time.time()
    out = ["Resultados da simulacao (gerado por simulacao/cenarios.py, passo de 30 s)", ""]
    cen_tipico(out)
    cen_recorde(out)
    cen_nublados(out)
    cen_falhas(out)
    cen_internet(out)
    cen_extra(out)
    out.append("Tempo de execucao: %.0f s" % (time.time() - t0))
    txt = "\n".join(out)
    print(txt)
    with open(os.path.join(AQUI, "resultados.txt"), "w") as f:
        f.write(txt + "\n")


if __name__ == "__main__":
    main()
