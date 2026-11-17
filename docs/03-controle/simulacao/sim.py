# -*- coding: utf-8 -*-
"""Simulador: roda a MESMA logica do controlador (controlador/logica.py)
contra o modelo da planta (planta.py), passo de 30 s."""

import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "controlador"))
sys.path.insert(0, AQUI)

import config        # noqa: E402
import logica        # noqa: E402
import telemetria    # noqa: E402
import planta        # noqa: E402

DT = 30.0

TIPICO = (23.0, 34.0, 5.8)
RECORDE = (27.0, 41.0, 5.8)
NUBLADO = (22.0, 32.0, 2.0)


def entregas_normais(T=35.0):
    """1 t entre 10 h e 14 h (doc 01, 3.1), em 4 entregas de 250 kg."""
    return [(10.0, 250.0, T), (11.0, 250.0, T), (12.0, 250.0, T), (13.0, 250.0, T)]


def dia(clima, entregas=None, **kw):
    d = {"clima": clima, "entregas": entregas_normais() if entregas is None else entregas}
    d.update(kw)
    return d


def _dentro(janelas, t):
    for a, b in janelas:
        if a <= t < b:
            return True
    return False


def rodar(cfg, dias, gelo_ini=0.8, starlink_w=30.0, bat_ini=0.9,
          falhas_sensor=None, internet_off=None, controlador_off=None,
          falha_vent_cond=None, operador_segue_aviso=True, registrar=False):
    """falhas_sensor: {nome: [(t_ini, t_fim), ...]} em segundos desde o inicio.
    internet_off / controlador_off / falha_vent_cond: lista de (t_ini, t_fim)."""
    falhas_sensor = falhas_sensor or {}
    internet_off = internet_off or []
    controlador_off = controlador_off or []
    falha_vent_cond = falha_vent_cond or []
    pl = planta.Planta(cfg, gelo_ini=gelo_ini, starlink_w=starlink_w, bat_ini=bat_ini)
    ctl = logica.Controlador(cfg, 0.0)
    tel = telemetria.Telemetria()
    passos_dia = int(86400 / DT)
    res_dias = []
    traco = []
    saidas_log = []
    ctl_vivo = True
    todos_eventos = []
    for d_idx, d in enumerate(dias):
        recebido = 0.0
        m = {"ar_max": -99, "ar_min": 99, "estoque_max": -99, "gelo_min": 999,
             "soc_min": 999, "co2_max": 0, "co2_med": 0.0, "partidas_h_max": 0,
             "aviso_0630": None, "aviso_1000": None, "lote_max_24h": None}
        pl.acc = {"_rodando": pl.acc.get("_rodando", 0)}
        entregas = list(d["entregas"])
        lote_t_entrada = None
        if d_idx > 0:
            pl.expedir(res_dias[-1]["recebido_kg"])
        for k in range(passos_dia):
            t = d_idx * 86400.0 + k * DT
            hora = k * DT / 3600.0
            falhos = [n for n, jan in falhas_sensor.items() if _dentro(jan, t)]
            com_inv = not _dentro(falhas_sensor.get("com_inversor", []), t)
            e = pl.entradas(t, hora, d_idx, falhos, com_inv)
            if _dentro(controlador_off, t):
                s = logica.saidas_estado_seguro(cfg["rota"]["n_comp"])
                ctl_vivo = False
            else:
                if not ctl_vivo:
                    # controlador reiniciou: estado novo (como na placa)
                    ctl = logica.Controlador(cfg, t)
                    ctl_vivo = True
                s = ctl.passo(e)
            todos_eventos.extend(s.get("eventos", []))
            pl.falha_vent_cond = _dentro(falha_vent_cond, t)
            net = not _dentro(internet_off, t)
            tel.passo(t, e, s, net)
            if registrar:
                saidas_log.append((t, [c["liga"] for c in s["comp"]],
                                   [round(c["freq"], 3) for c in s["comp"]],
                                   round(s["vent_serp"], 6), s["ar_novo_m3h"], s["aviso_base"]))
            # operador: recebe conforme o aviso
            aviso = s["aviso_base"]
            if abs(hora - 6.5) < DT / 7200:
                m["aviso_0630"] = aviso
            if abs(hora - 9.5) < DT / 7200 and len(pl.lotes) > 1:
                m["lote_ontem_0930"] = pl.tt3()
            if abs(hora - 10.5) < DT / 7200:
                m["aviso_1000"] = aviso
            while entregas and hora >= entregas[0][0]:
                h_e, kg, T = entregas.pop(0)
                if operador_segue_aviso:
                    if aviso == logica.AV_NAO:
                        kg = 0.0
                    elif aviso == logica.AV_MEIA:
                        kg = max(0.0, min(kg, 500.0 - recebido))
                if kg > 0:
                    pl.receber(kg, T, t)
                    recebido += kg
                    lote_t_entrada = t
            rec_ativa = 7.0 <= hora < 14.0
            pl.passo(t, hora, DT, s, d["clima"], rec_ativa)
            if hora >= 6.0 and abs(hora - 6.0) < DT / 7200:
                pl.juntar_lotes(t)
            m["ar_max"] = max(m["ar_max"], pl.Tar)
            m["ar_min"] = min(m["ar_min"], pl.Tar)
            m["estoque_max"] = max(m["estoque_max"], pl.tt2())
            m["gelo_min"] = min(m["gelo_min"], pl.lt1())
            m["soc_min"] = min(m["soc_min"], 100.0 * pl.bat / pl.bat_cap)
            m["co2_max"] = max(m["co2_max"], pl.co2)
            m["co2_med"] += pl.co2 / passos_dia
            for c in ctl.comps:
                m["partidas_h_max"] = max(m["partidas_h_max"], c.partidas_ultima_hora(t))
            if registrar and k % 20 == 0:
                traco.append((t, round(pl.Tar, 2), round(pl.tt2(), 2), round(pl.tt3(), 2),
                              round(pl.lt1(), 1), round(100 * pl.bat / pl.bat_cap, 1), round(pl.co2, 3)))
        # temperatura do lote novo 24 h depois da 1a entrada: medida no inicio do dia seguinte (aprox.)
        m["recebido_kg"] = recebido
        m["lote_fim_dia"] = pl.tt3() if recebido > 0 else None
        m.update({k: v for k, v in pl.acc.items() if not k.startswith("_")})
        m["paradas_curtas"] = sum(c.paradas_curtas for c in ctl.comps)
        m["paradas_forcadas"] = sum(c.paradas_forcadas for c in ctl.comps)
        m["alarmes_fim"] = list(ctl.alarmes.keys())
        m["nublados_ctl"] = ctl.nublados
        res_dias.append(m)
    return {"dias": res_dias, "traco": traco, "tel": tel, "saidas": saidas_log,
            "ctl": ctl, "planta": pl, "eventos": todos_eventos}
