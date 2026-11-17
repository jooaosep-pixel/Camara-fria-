# -*- coding: utf-8 -*-
"""Programa principal da placa (MicroPython, ESP32 industrial).

NAO FOI TESTADO EM PLACA (nao ha placa neste ambiente). A logica que ele
chama (logica.py) e a mesma testada na simulacao. Este arquivo so liga a
logica aos pinos, ao Modbus e a internet; os nomes dos pinos seguem o mapa
de entradas e saidas do LEIAME (secao 4) e devem ser conferidos contra o
manual da placa comprada.

Gravacao: ver LEIAME, secao 10 (mpremote cp *.py :).
"""

import time

try:
    import machine          # so existe na placa
    import network
    import urequests as requests
    import ujson as json
    NA_PLACA = True
except ImportError:          # no PC: permite importar sem erro
    NA_PLACA = False

import config
import logica
import telemetria

# ---------------- ajustes do local (editar no comissionamento) -------------
ROTA = "B"          # "A" ou "B"
KWP = 12.0
GELO_KG = 700
WIFI_SSID = "STARLINK"
WIFI_SENHA = ""             # preencher no local; nunca publicar
TELEGRAM_TOKEN = ""         # bot criado no Telegram; nunca publicar
TELEGRAM_CHAT = ""
BATIMENTO_URL = ""          # URL do servico de vigilancia (ver LEIAME 8.3)
PERIODO_S = 1.0             # ciclo de controle

# ---------------- mapa de E/S (LEIAME secao 4) ----------------------------
# Saidas digitais a rele (24 V): todas "ligado = energizado".
DO = {
    "PERM_C1": 0,     # permissao do compressor 1 (entra NA cadeia de seguranca, apos o watchdog)
    "PERM_C2": 1,
    "SOL_C1": 2,      # solenoide de liquido (recolhimento)
    "SOL_C2": 3,
    "BOMBA_BANCO": 4, # agitacao (b) ou P1 (a)
    "K_BAT_COMP": 5,  # Rota B: liga o inversor da bateria ao compressor 1
    "SIRENE": 6,
    "LUZ_VERDE": 7,   # luz da porta: verde energizada; sem energia = vermelha (falha segura)
    "WATCHDOG": 8,    # pulso para o rele de watchdog externo
    "STARLINK": 9,    # contato NF: desenergizado = Starlink LIGADA
    "CARTER_C1": 10,
    "CARTER_C2": 11,
}
AO = {"FREQ_C1": 0, "FREQ_C2": 1, "VENT_SERP": 2, "AR_NOVO": 3, "AGUA_SP": 4}  # 0-10 V
DI = {"CADEIA_C1": 0, "CADEIA_C2": 1, "PORTA": 2, "PESSOA_PRESA": 3,
      "BOTAO_ENTRADA": 4, "EI1": 5, "FLUXO": 6, "GAS": 7,
      "FALHA_INV1": 8, "FALHA_INV2": 9, "RESET": 10}


def ler_entradas(io, t, hora, dia):
    """Le tudo e devolve o dicionario de entradas da logica.
    Leitura que falhar volta como None (a logica trata como sensor em falha)."""
    e = {"t": t, "hora": hora, "dia": dia}
    for nome in ("TT1", "TT2", "TT3", "TT4", "TT5", "TT6", "UR1", "CO2", "LT1", "G", "T_glicol"):
        e[nome] = io.ler_analogico(nome)
    e["soc"] = io.ler_modbus("SOC")
    e["pv_kw"] = io.ler_modbus("PV_KW")
    e["carga_kw"] = io.ler_modbus("CARGA_KW")
    e["aux_kw"] = io.ler_modbus("AUX_KW")
    e["com_inversor"] = e["soc"] is not None
    e["EI1"] = io.ler_di(DI["EI1"])
    e["porta"] = io.ler_di(DI["PORTA"])
    e["pessoa_presa"] = io.ler_di(DI["PESSOA_PRESA"])
    e["botao_entrada"] = io.ler_di(DI["BOTAO_ENTRADA"])
    e["fluxo_ok"] = io.ler_di(DI["FLUXO"])
    e["gas"] = io.ler_di(DI["GAS"])
    e["comp"] = []
    for i in (1, 2):
        e["comp"].append({
            "PT1": io.ler_analogico("PT1_C%d" % i),
            "PT2": io.ler_analogico("PT2_C%d" % i),
            "cadeia_ok": io.ler_di(DI["CADEIA_C%d" % i]),
            "inversor_falha": io.ler_di(DI["FALHA_INV%d" % i]),
        })
    return e


def escrever_saidas(io, s):
    for i, c in enumerate(s["comp"]):
        io.do(DO["PERM_C%d" % (i + 1)], c["liga"])
        io.do(DO["SOL_C%d" % (i + 1)], c["solenoide"])
        io.do(DO["CARTER_C%d" % (i + 1)], c["carter"])
        io.ao(AO["FREQ_C%d" % (i + 1)], c["freq"] / 70.0 * 10.0)
    io.do(DO["BOMBA_BANCO"], s["bomba_banco"])
    io.do(DO["K_BAT_COMP"], s["bat_comp"])
    io.do(DO["SIRENE"], s["sirene"])
    io.do(DO["LUZ_VERDE"], s["luz_porta"] == "VERDE")
    io.do(DO["WATCHDOG"], s["watchdog"])
    io.do(DO["STARLINK"], not s["starlink"])
    io.ao(AO["VENT_SERP"], s["vent_serp"] * 10.0 if s["bomba_p2"] else 3.0)
    io.ao(AO["AR_NOVO"], s["ar_novo_m3h"] / 60.0 * 10.0)
    io.ao(AO["AGUA_SP"], s["agua_sp"])  # 0-10 V = 0-10 C na valvula misturadora


def principal(io, relogio):
    cfg = config.montar(ROTA, kwp=KWP, gelo_kg=GELO_KG)
    t0 = time.time()
    ctl = logica.Controlador(cfg, t0)
    tel = telemetria.Telemetria()
    if NA_PLACA:
        wdt = machine.WDT(timeout=10000)  # watchdog interno: reinicia a placa travada
    while True:
        t = time.time()
        hora, dia = relogio()
        e = ler_entradas(io, t, hora, dia)
        if io.ler_di(DI["RESET"]):
            ctl.reset_manual(t)
        s = ctl.passo(e)
        escrever_saidas(io, s)
        tel.passo(t, e, s, io.internet_ok(), io.enviar)
        if NA_PLACA:
            wdt.feed()
        time.sleep(PERIODO_S)
