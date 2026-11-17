# -*- coding: utf-8 -*-
"""Configuracao do controlador da camara fria solar.

TUDO o que muda entre a Rota A e a Rota B (e entre as arquiteturas (a) e (b)
do doc 01) fica AQUI. A logica (logica.py) e a mesma nas duas rotas.

Compativel com MicroPython (so dicionarios, sem bibliotecas).
Valores [SUPOSTO] devem ser ajustados no comissionamento; os marcados
[VALIDAR] dependem do fabricante do compressor/inversor ou de engenheiro.
"""

# ---------------------------------------------------------------------------
# Setpoints comuns (doc 01, secao 12.3, versao com a correcao N2/N3)
# ---------------------------------------------------------------------------
SETPOINTS = {
    # Camara
    "t_camara": 12.0,            # C, manga (D1)
    "alarme_alto": 15.0,         # C, por 2 h
    "alarme_alto_atraso_s": 7200,
    "alarme_baixo": 10.0,        # C, dano por frio da manga
    "alarme_baixo_atraso_s": 900,
    "corte_frio_pump": 10.5,     # C: abaixo disso a bomba P2 para (nao resfria mais)
    # Agua/glicol para a serpentina (TT5)
    "agua_dia": 3.0,             # C, 7 h-17 h e sempre que faltar frio
    "agua_noite": 6.0,           # C, 17 h-7 h (correcao N3: umidade)
    "agua_noite_ini_h": 17.0,
    "agua_noite_fim_h": 7.0,
    # Ventiladores da serpentina (PI sobre TT1)
    "vent_min": 0.30,            # fracao (30 %)
    "vent_kp": 0.6,              # fracao por K
    "vent_ti_s": 1800.0,
    # Banco de gelo (LT1, % do gelo util)
    "lt1_cheio": 100.0,
    "lt1_religa": 97.0,
    "lt1_so_um": 95.0,           # acima disso so 1 compressor (rodizio)
    "lt1_meia_carga_9h": 50.0,
    "lt1_nao_receber": 20.0,
    # Recepcao (D2)
    "recepcao_ini_h": 7.0,
    "recepcao_fim_h": 14.0,
    "aviso_inicial_h": 6.5,
    "aviso_revisao_h": 10.0,
    "kwh_kwp_ate_10h_min": 0.5,  # 6 kWh ate 10 h para 12 kWp (doc 01, 12.3)
    "dia_nublado_kwh_m2": 3.5,   # irradiacao diaria abaixo disso = dia nublado [SUPOSTO]
    # CO2 (doc 01, 11.2 apos N2)
    "co2_luz_verde": 0.39,       # % volume: verde abaixo
    "co2_alarme": 1.0,           # %
    "co2_critico": 2.0,          # %
    "ar_novo_base": 30.0,        # m3/h continuos
    "ar_novo_max": 60.0,         # m3/h acima de 0,39 %
    "ar_novo_purga_ini_h": 5.5,  # ventilacao antes da 1a entrada (45 m3)
    "ar_novo_purga_fim_h": 7.0,
    # Porta
    "porta_aberta_alarme_s": 600,
    # Estoque
    "polpa_estoque_alarme": 14.0,
    # Bateria (SOC em %)
    "soc_aviso": 30.0,
    "soc_critico": 15.0,
    "soc_corta_starlink": 12.0,
    # Resistencia de carter: liga 1 h antes do sol e com o compressor parado de dia
    "carter_ini_h": 4.5,
    "carter_fim_h": 17.5,
}

# ---------------------------------------------------------------------------
# Compressor: protecoes (doc 01, 12.3) [VALIDAR com o fabricante]
# ---------------------------------------------------------------------------
COMPRESSOR = {
    "min_ligado_s": 180,
    "min_ligado_banco_cheio_s": 300,
    "min_desligado_s": 300,
    "max_partidas_hora": 6,
    "atraso_partida_s": 120,      # condicao de partida precisa durar 2 min
    "intervalo_entre_partidas_s": 30,  # nunca dois compressores partindo juntos
    "recolhimento_max_s": 90,     # pump-down: fecha solenoide e recolhe
    "recolhimento_fim_bar": 0.9,  # bar relativo
    # Pressoes por software (o pressostato de ALTA e de BAIXA sao hardware,
    # ligados direto na cadeia de seguranca: ver LEIAME)
    "alta_reduz_bar": 15.5,       # bar rel: reduz rotacao
    "alta_para_bar": 16.5,        # bar rel: para e bloqueia
    "alta_bloqueio_s": 900,
    "succao_sat_min_c": -12.0,    # evaporacao abaixo disso por 60 s: para (banco cheio/gelo grosso)
    "succao_sat_min_atraso_s": 60,
    "falhas_para_bloqueio": 3,    # 3 bloqueios em 1 h -> trava ate reset manual
}

# Arquiteturas termicas (doc 01, secao 7)
ARQ_B = {  # R513A, expansao direta no banco, so agua na camara
    "nome": "b",
    "glicol": False,
    "agua_min_c": 2.0,            # alarme de agua fria demais (TT5)
}
ARQ_A = {  # resfriador selado + glicol 35 %
    "nome": "a",
    "glicol": True,
    "glicol_min_c": -8.0,         # software para o resfriador; TSL de hardware tambem a -8
    "agua_min_c": 2.0,
}

# ---------------------------------------------------------------------------
# Rotas de acionamento (doc 01, "As tres rotas")
# ---------------------------------------------------------------------------
ROTA_B = {
    "rota": "B",
    "n_comp": 2,
    "velocidade_variavel": True,
    "f_min_hz": 30.0,
    "f_max_hz": 70.0,
    "p_min_kw": 1.6,              # potencia eletrica do compressor a 30 Hz
    "p_max_kw": 3.7,              # a 70 Hz (0,62 x kWp / 2 com 12 kWp)
    "p_partida_kw": 1.8,          # disponivel no grupo para partir (2,0 kW de geracao com auxiliares)
    "p_queda_kw": 1.3,            # abaixo disso por 20 s o inversor nao sustenta: parada forcada
    "p_queda_atraso_s": 20,
    "pr": 0.75,                   # desempenho global do arranjo (doc 01, secao 4)
    "aux_no_grupo": 1,            # o carregador das cargas 24 h fica no grupo do compressor 1
    "bateria_kwh_util": 4.6,      # 1 modulo de 5,12 kWh
    "bat_comp_soc_min_liga": 50.0,  # bateria so toca compressor com gelo 0 e camara > 13 C
    "bat_comp_soc_desliga": 35.0,
    "bat_comp_t_camara": 13.0,
}

ROTA_A = {
    "rota": "A",
    "n_comp": 2,
    "velocidade_variavel": False,  # unidades condensadoras de rotacao fixa (N4)
    "p_unidade_kw": 3.7,
    "partida_sobra_frac": 0.6,     # parte se a sobra solar >= 60 % da unidade (2 min)
    "soc_min_partida": 50.0,
    "soc_partida_sem_sobra": 95.0, # bateria cheia e sol: pode partir mesmo sem sobra
    "soc_para": 40.0,
    "soc_para_camara": 25.0,       # prioridade da camara: pode descer ate aqui
    "deficit_para_s": 300,
    "pr": 0.75,
    "bateria_kwh_util": 13.5,      # 15 kWh nominais x 0,9 (10 kWh -> 9,0)
    "bat_comp_t_camara": 13.0,
}

ROTAS = {"A": ROTA_A, "B": ROTA_B}
ARQS = {"a": ARQ_A, "b": ARQ_B}


def montar(rota="B", arq=None, kwp=12.0, gelo_kg=700, **extra):
    """Monta a configuracao completa. Rota A usa a arquitetura (a) por padrao."""
    r = dict(ROTAS[rota])
    if arq is None:
        arq = "a" if rota == "A" else "b"
    cfg = {
        "rota": r,
        "arq": dict(ARQS[arq]),
        "sp": dict(SETPOINTS),
        "comp": dict(COMPRESSOR),
        "kwp": float(kwp),
        "kwp_grupo": float(kwp) / r["n_comp"],
        "gelo_kg": gelo_kg,
    }
    if rota == "B":
        # potencia maxima do compressor acompanha o arranjo (0,62 x kWp no total)
        r["p_max_kw"] = min(3.7, 0.62 * kwp / 2.0)
    for k in extra:
        if k in cfg["sp"]:
            cfg["sp"][k] = extra[k]
        elif k in cfg["rota"]:
            cfg["rota"][k] = extra[k]
        elif k in cfg["comp"]:
            cfg["comp"][k] = extra[k]
        else:
            cfg[k] = extra[k]
    return cfg
