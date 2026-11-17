#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contas do agente financeiro — docs/12-financeiro.md
RODADA 1 (PRELIMINAR). Rodar:  python3 docs/_trabalho/financeiro.py

Como usar na 2a rodada: trocar SOMENTE os valores do bloco "ENTRADAS" e rodar de novo.
Cada entrada diz de onde veio. Marcação:
  A = preço encontrado (anúncio ou tabela com link, visto em 17/11/2026)
  B = faixa estimada a partir de preço encontrado de item parecido (conta mostrada)
  C = SEM PREÇO: reserva provisória [SUPOSTO] do analista, sem fonte; trocar por cotação
Nenhum valor C deve ser lido como preço.
"""

# =============================================================================
# ENTRADAS
# =============================================================================

# ---- Configuração provisória do protótipo (doc 01 está sendo refeito) --------
CFG = dict(
    kwp=10.0,          # doc 01 secao 5.3/12: "so manga: 10 kWp + 600 kg" (versao antiga) [PROVISORIO]
    gelo_kg=600.0,     # idem [PROVISORIO]
    n_maquinas=2,      # doc 01 secao 8.2: dois circuitos [PROVISORIO]
    bat_modulos=2,     # modulos de 5,12 kWh; ver secao (d) [PROVISORIO]
    capacidade_t=5.0,  # decisao D1
)
W_MODULO = 550.0
KWH_POR_KG_GELO = 334.0 / 3600.0      # 0,0928 kWh de frio por kg de gelo
KWH_MODULO_BAT = 5.12

# ---- Precos unitarios (min, max, grau, origem) --------------------------------
P = dict(
    reefer=(20000, 30000, "A", "MF Rural, anuncios SP, sem frete (doc 01 s.12; doc 11 s.4.8)"),
    modulo=(870, 1350, "A", "Pichau R$ 869,99; Mercado Livre R$ 1.350 (doc 11 s.4.1)"),
    # estrutura: R$ 2,45/Wp (sistema residencial instalado, 1T2026) x 18 % (fatia da estrutura
    # em usina de solo, Canal Solar) = R$ 0,44/Wp; teto = dobro, por ser cobertura elevada [SUPOSTO]
    estrutura_por_kwp=(440, 900, "B", "2,45 R$/Wp x 18 % = 0,44; teto 0,90 [SUPOSTO]"),
    drive=(2814, 3569, "B", "kits de bombeamento solar 5,5 e 7,5 cv, Mercado Livre (doc 11 s.4.3); WEG sem preco"),
    inversor_aux=(3844, 8500, "A", "Deye hibrido 6 kW a partir de R$ 3.844; 5 kW 48 V R$ 7.800-8.500 (Magazine Luiza, pagina de busca)"),
    # bateria: piso = custo posto de importacao do doc 11 (US$ 768 FOB -> R$ 8.331); teto [SUPOSTO]
    bat_modulo=(8331, 13000, "B", "piso: doc 11 s.4.5 (custo posto); teto [SUPOSTO]; preco de loja no Brasil nao encontrado"),
    cond_nacional=(5070, 9883, "B", "Danfoss OP-HJZ019 e HJZ064, velocidade fixa, R22/R404A (doc 11 s.4.2); em R513A: sem preco"),
    cond_importada_posta=(15941, 15941, "B", "doc 11 s.4.2: FOB US$ 1.380 -> R$ 15.941, gas nao confirmado"),
    importacao_fixos=(7714, 7714, "B", "doc 11 s.4.1: custos fixos de um embarque R$ 7.714,50"),
    tubo_por_m=(7.40, 19.13, "B", "PEX multicamada 16 mm, rolo 100 m R$ 739,99 (Mercado Livre) a R$ 1.912,68 (Magazine Luiza); nao e o PE-RT do projeto"),
    caixa_2000l=(1215, 1280, "A", "SINAPI mai/2026 R$ 1.272,45; Telhanorte R$ 1.279,99 (Pix R$ 1.215,90)"),
    painel_pu_m2=(293, 611, "A", "SINAPI mai/2026 70/80 mm R$ 292,61; ORSE 100 mm R$ 610,98 (doc 11 s.4.7)"),
    diaria_frigorista=(380, 450, "A", "Lar Pontual, data-base out/2026 (tecnico de refrigeracao autonomo)"),
    diaria_eletricista=(269, 450, "A", "Lar Pontual out/2026: PE R$ 269,27; faixa Brasil ate R$ 450"),
    starlink_kit=(299, 2400, "A", "Mini em promocao R$ 299; Standard R$ 2.400 (imprensa, nov/2026)"),
    starlink_mes=(189, 249, "A", "Residencial R$ 189/mes; Max R$ 249/mes (imprensa, 08/11/2026)"),
    clp=(1984, 1984, "B", "doc 11 s.4.6: CLP de US$ 200 posto = R$ 1.984 (exemplo)"),
)

# ---- Quantidades supostas (trocar pelas dos projetistas) ----------------------
Q = dict(
    m_tubo_por_kg=1070.0 / 800.0,    # doc 01 s.6.2: 1.070 m para 800 kg -> 1,34 m/kg
    area_isol_tanque_m2=(8.0, 12.0), # doc 01 s.6.2: tanque 1,9x1,0x1,0 -> ~9,6 m2 [CALCULADO pelo financeiro]
    diarias_frigorista=(15, 30),     # [SUPOSTO] pedir ao frigorista
    diarias_eletricista=(10, 20),    # [SUPOSTO] pedir ao integrador
)

# ---- Reservas provisorias para itens SEM PRECO (grau C) -----------------------
C = dict(
    frete_reefer=(8000, 20000, "SP -> Petrolina (~2.200 km) + guindaste; sem cotacao"),
    evap_serpentina=(8000, 25000, "trocador/evaporador + serpentina de ar + ventiladores EC (doc 01 itens 6,7,14,15)"),
    valvulas_gas_tubos=(5000, 15000, "expansao eletronica, solenoides, pressostatos, filtros, gas, cobre, isolamento (itens 8-10, 21)"),
    secundario=(3000, 12000, "bombas + reserva, glicol 80 L, vaso, tubos, valvulas (itens 16-20)"),
    ar_novo_co2=(1500, 5000, "renovacao de ar e sensor de CO2 (parecer do revisor, achado 2)"),
    tanque_estrutura=(3000, 10000, "coletores, suportes do feixe, ancoragem, estrutura e base do tanque (itens 11,13; achado 5)"),
    tanque_montagem=(3000, 8000, "mao de obra de montagem do feixe de tubos"),
    cabos_protecao_cc=(3000, 8000, "cabos CC, string box, DPS, aterramento, protecao contra raio"),
    eletrica_ca=(6000, 15000, "quadros, disjuntores, cabos, iluminacao (doc 02 nao existe)"),
    controle=(5000, 15000, "sensores, quadro, IHM, fonte, programacao (doc 03 nao existe)"),
    civil=(15000, 50000, "bases do conteiner e do tanque, recepcao coberta 40-60 m2, cerca, piso (doc 09 s.5.1)"),
    operacao_equip=(3000, 10000, "balanca, caixas plasticas, mesa de selecao (doc 09 s.6)"),
    frete_outros=(2000, 6000, "fretes dos demais equipamentos"),
    taxas_rt=(5000, 20000, "projeto e ART de profissional habilitado, laudos, licencas (doc 09 s.5.2)"),
)
RESERVA_IMPREVISTOS = (0.15, 0.25)   # [SUPOSTO] prototipo unico

# ---- Entradas de desempenho (TODAS provisorias, do doc 01 antigo e do parecer) -
T = dict(
    carga_dia=68.0,            # kWh frio/dia, so manga: autor 66,6-69,8; revisor 60,9 [PROVISORIO]
    carga_sem_fruta=35.6,      # kWh/dia: 74,2 kWh / 50 h x 24 (doc 01 s.5.6, manga) [CALCULADO sobre PROVISORIO]
    y_autor=7.2,               # kWh frio por kWp.dia, dia de projeto (parecer s.1)
    y_revisor=8.5,             # idem, conta do revisor
    y_nublado=13.3 / 12.0,     # 1,11 kWh frio/kWp num dia de 2,0 kWh/m2 (doc 01 s.5.6)
    gelo_inicio=0.70,          # fracao do tanque no inicio do 1o dia nublado (doc 01 s.5.6: 53,5/74,2)
    inercia_fruta=5.2,         # kWh por grau, 5 t (doc 01 s.5.6)
    cop_noite=2.2,             # COP se a bateria tocar o compressor [SUPOSTO; doc 01 s.8.1 modo camara]
    dod=0.90, ef_bat=0.90,     # [SUPOSTO]
    aux_noite_w=(140, 500),    # W: autor 115 W + Starlink Mini 25 W ... revisor 400 W + Starlink 100 W
    horas_noite=14.0,
    frio_pelo_gelo_dia=40.0,   # kWh/dia que passam pelo gelo [SUPOSTO]; pedir ao engenheiro
    dias_ano=240,              # doc 10 s.6.1, cenario medio (pessimista 150, otimista 330)
    anos=10,
)

# ---- Valor da fruta e receita (doc 10) ----------------------------------------
PRECO_ROCA, PRECO_CANAL = 1.20, 5.06      # R$/kg manga (doc 10 s.4.2)
FRACAO_PERDIDA = 0.30                     # [SUPOSTO, SEM FONTE] fruta perdida num evento sem frio
CEN = {  # doc 10 s.6.1 (versao so manga, 5 t): receitas R$ 4.500 / 32.400 / 115.500 — copiadas, nao refeitas
    "pessimista": dict(ocup=0.20, dias=150, taxa=0.03),
    "medio":      dict(ocup=0.45, dias=240, taxa=0.06),
    "otimista":   dict(ocup=0.70, dias=330, taxa=0.10),
}
# Leitura do revisor (docs/_trabalho/revisao-10-demanda.md), receitas copiadas, nao refeitas
REC_REVISOR = {"rev. pessimista": 3000, "rev. medio": 15000, "rev. otimista": 50000,
               "merenda (min)": 14200, "merenda (max)": 23700}
# D6: o cenario "otimista" do autor depende de frutas complementares (abril a julho)
OPEX_SEM_OPERADOR, OPEX_COM_OPERADOR = 12000, 36000   # doc 10 s.6.3 [SUPOSTO]
JUROS = {"sem juros": 0.0, "Pronaf 2% a.a.": 0.02, "7,5% a.a.": 0.075}

# ---- Parametros das comparacoes (a) e (c) — [SUPOSTO], trocar na 2a rodada -----
A_PAR = dict(manut_art=0.02, manut_com=0.01,           # % do investimento por ano
             p_retrab_art=0.30, f_retrab_art=0.50,     # chance e tamanho do retrabalho no artesanal
             p_retrab_com=0.05, f_retrab_com=0.20,
             preco_comercial=None)                      # SEM PRECO -> calcula-se o preco de empate
C_PAR = dict(margem_importadora=(0.0, 0.25), sobressalentes=0.10,
             diarias_selada=(4, 8), diarias_local=(10, 20),
             extras_local=(3000, 8000),                 # valvula eletronica, recipiente etc. [C]
             gas_r513a_inicial=(1000, 3000),            # [C] sem preco
             vazamento_ano=(0.05, 0.10),                # fracao da carga reposta por ano [SUPOSTO]
             manut_selada=0.02, manut_local=0.03,
             ganho_cop_local=0.10)                      # doc 01 s.6.1: expansao direta ~10 % melhor

# =============================================================================
# FUNCOES
# =============================================================================
def brl(x):
    return ("R$ {:,.0f}".format(x)).replace(",", ".")

def fator(i, n=10):
    return 1.0 / n if i == 0 else i / (1 - (1 + i) ** -n)

def linhas_custo(cfg):
    n_mod = round(cfg["kwp"] * 1000 / W_MODULO)
    kwp_real = n_mod * W_MODULO / 1000
    m_tubo = cfg["gelo_kg"] * Q["m_tubo_por_kg"]
    L = []
    def add(bloco, item, mn, mx, grau, origem):
        L.append((bloco, item, mn, mx, grau, origem))
    add("1 Involucro", "Reefer 20 pes usado (so a caixa)", *P["reefer"][:3], P["reefer"][3])
    add("2 Refrigeracao", f"Maquina de frio, 1 a {cfg['n_maquinas']} un. (nacional fixa ... importada inverter posta)",
        P["cond_nacional"][0], cfg["n_maquinas"] * P["cond_importada_posta"][1] + P["importacao_fixos"][1], "B",
        "piso: 1 condensadora nacional; teto: importadas + custos fixos (doc 11)")
    add("2 Refrigeracao", "Evaporador/trocador, serpentina de ar, ventiladores", *C["evap_serpentina"][:2], "C", C["evap_serpentina"][2])
    add("2 Refrigeracao", "Valvulas, protecoes, gas, tubulacao, isolamento", *C["valvulas_gas_tubos"][:2], "C", C["valvulas_gas_tubos"][2])
    add("2 Refrigeracao", "Circuito secundario (bombas, glicol, tubos)", *C["secundario"][:2], "C", C["secundario"][2])
    add("2 Refrigeracao", "Renovacao de ar e sensor de CO2", *C["ar_novo_co2"][:2], "C", C["ar_novo_co2"][2])
    add("3 Armaz. termico", f"Tubo 16 mm, {m_tubo:.0f} m ({cfg['gelo_kg']:.0f} kg de gelo)",
        m_tubo * P["tubo_por_m"][0], m_tubo * P["tubo_por_m"][1], "B", P["tubo_por_m"][3])
    add("3 Armaz. termico", "Reservatorio (ref.: caixa de 2.000 L)", *P["caixa_2000l"][:3], P["caixa_2000l"][3])
    add("3 Armaz. termico", "Isolamento do tanque, 8 a 12 m2",
        Q["area_isol_tanque_m2"][0] * P["painel_pu_m2"][0], Q["area_isol_tanque_m2"][1] * P["painel_pu_m2"][1], "B", P["painel_pu_m2"][3])
    add("3 Armaz. termico", "Coletores, suportes, estrutura e base do tanque", *C["tanque_estrutura"][:2], "C", C["tanque_estrutura"][2])
    add("3 Armaz. termico", "Montagem do feixe", *C["tanque_montagem"][:2], "C", C["tanque_montagem"][2])
    add("4 Solar", f"Modulos 550 W, {n_mod} un. ({kwp_real:.1f} kWp)", n_mod * P["modulo"][0], n_mod * P["modulo"][1], "A", P["modulo"][3])
    add("4 Solar", "Estrutura dos modulos e fundacao", kwp_real * P["estrutura_por_kwp"][0], kwp_real * P["estrutura_por_kwp"][1], "B", P["estrutura_por_kwp"][3])
    add("4 Solar", f"Drive solar do compressor, 1 a {cfg['n_maquinas']} un.", P["drive"][0], cfg["n_maquinas"] * P["drive"][1], "B", P["drive"][3])
    add("4 Solar", "Cabos CC, protecoes, aterramento, raio", *C["cabos_protecao_cc"][:2], "C", C["cabos_protecao_cc"][2])
    add("5 Bateria", f"LiFePO4 48 V, 1 a {cfg['bat_modulos']} modulos de 5,12 kWh", P["bat_modulo"][0], cfg["bat_modulos"] * P["bat_modulo"][1], "B", P["bat_modulo"][3])
    add("5 Bateria", "Inversor/carregador 48 V das cargas auxiliares", *P["inversor_aux"][:3], P["inversor_aux"][3])
    add("6 Eletrica", "Quadros, cabos, protecoes CA, iluminacao", *C["eletrica_ca"][:2], "C", C["eletrica_ca"][2])
    add("7 Controle e telemetria", "Controlador (ref. CLP)", *P["clp"][:3], P["clp"][3])
    add("7 Controle e telemetria", "Sensores, quadro, IHM, programacao", *C["controle"][:2], "C", C["controle"][2])
    add("7 Controle e telemetria", "Kit Starlink", *P["starlink_kit"][:3], P["starlink_kit"][3])
    add("8 Estrutura e obra civil", "Bases, recepcao coberta, cerca, piso", *C["civil"][:2], "C", C["civil"][2])
    add("8 Estrutura e obra civil", "Balanca, caixas, mesa de selecao", *C["operacao_equip"][:2], "C", C["operacao_equip"][2])
    add("9 Mao de obra", f"Frigorista, {Q['diarias_frigorista'][0]} a {Q['diarias_frigorista'][1]} diarias",
        Q["diarias_frigorista"][0] * P["diaria_frigorista"][0], Q["diarias_frigorista"][1] * P["diaria_frigorista"][1], "B",
        P["diaria_frigorista"][3] + "; quantidade [SUPOSTO]")
    add("9 Mao de obra", f"Eletricista, {Q['diarias_eletricista'][0]} a {Q['diarias_eletricista'][1]} diarias",
        Q["diarias_eletricista"][0] * P["diaria_eletricista"][0], Q["diarias_eletricista"][1] * P["diaria_eletricista"][1], "B",
        P["diaria_eletricista"][3] + "; quantidade [SUPOSTO]")
    add("10 Frete", "Reefer ate o local, com guindaste", *C["frete_reefer"][:2], "C", C["frete_reefer"][2])
    add("10 Frete", "Demais equipamentos", *C["frete_outros"][:2], "C", C["frete_outros"][2])
    add("11 Taxas e resp. tecnico", "Projeto/ART, laudos, licencas", *C["taxas_rt"][:2], "C", C["taxas_rt"][2])
    return L

def total(cfg):
    L = linhas_custo(cfg)
    mn = sum(l[2] for l in L); mx = sum(l[3] for l in L)
    return mn * (1 + RESERVA_IMPREVISTOS[0]), mx * (1 + RESERVA_IMPREVISTOS[1]), mn, mx, L

def custo_kwp():
    """R$ por kWp adicional (modulos + estrutura), min e max."""
    return (P["modulo"][0] / W_MODULO * 1000 + P["estrutura_por_kwp"][0],
            P["modulo"][1] / W_MODULO * 1000 + P["estrutura_por_kwp"][1])

def custo_gelo_marginal_kg():
    """R$ por kg de gelo adicional: so o tubo (tanque e isolamento crescem pouco) x 1,3 [SUPOSTO]."""
    return (Q["m_tubo_por_kg"] * P["tubo_por_m"][0] * 1.3, Q["m_tubo_por_kg"] * P["tubo_por_m"][1] * 1.3)

def meio(par):
    return (par[0] + par[1]) / 2.0

# =============================================================================
# SAIDA
# =============================================================================
def sec(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)

def main():
    print("financeiro.py — RODADA 1, PRELIMINAR — entradas de 17/11/2026")
    print("Configuracao provisoria:", CFG)

    # ---------------------------------------------------------------- 1 quadro
    sec("1. QUADRO DE CUSTOS (R$) — A = preco encontrado; B = faixa estimada; C = sem preco (reserva suposta)")
    tmn, tmx, smn, smx, L = total(CFG)
    print(f"{'Bloco':<26}{'Item':<72}{'Min':>10}{'Max':>10}  Grau")
    bl = {}
    gr = {"A": [0, 0], "B": [0, 0], "C": [0, 0]}
    for b, it, mn, mx, g, o in L:
        print(f"{b:<26}{it[:70]:<72}" + f"{mn:>10,.0f}{mx:>10,.0f}".replace(",", ".") + f"  {g}")
        bl.setdefault(b, [0, 0]); bl[b][0] += mn; bl[b][1] += mx
        gr[g][0] += mn; gr[g][1] += mx
    print("\nSubtotal por bloco:")
    for b, (mn, mx) in bl.items():
        print(f"  {b:<28}{brl(mn):>14} a {brl(mx):>12}   ({mn / smn * 100:4.1f} % a {mx / smx * 100:4.1f} % do subtotal)")
    print(f"  {'SUBTOTAL':<28}{brl(smn):>14} a {brl(smx):>12}")
    print(f"  12 Reserva imprevistos {RESERVA_IMPREVISTOS[0]*100:.0f} a {RESERVA_IMPREVISTOS[1]*100:.0f} %: "
          f"{brl(smn * RESERVA_IMPREVISTOS[0])} a {brl(smx * RESERVA_IMPREVISTOS[1])}")
    print(f"  TOTAL PRELIMINAR: {brl(tmn)} a {brl(tmx)}")
    print("\nQuanto do subtotal tem cada grau de confianca:")
    for g, nome in (("A", "preco encontrado"), ("B", "faixa estimada"), ("C", "sem preco (reserva suposta)")):
        print(f"  {g} {nome:<30}{brl(gr[g][0]):>12} a {brl(gr[g][1]):>12}   ({gr[g][0]/smn*100:4.1f} % a {gr[g][1]/smx*100:4.1f} %)")

    # ---------------------------------------------------------------- custos unitarios
    sec("2. CUSTOS UNITARIOS USADOS NAS COMPARACOES")
    ck = custo_kwp(); cg = custo_gelo_marginal_kg()
    cg_kwh = (cg[0] / KWH_POR_KG_GELO, cg[1] / KWH_POR_KG_GELO)
    cb = (P["bat_modulo"][0] / KWH_MODULO_BAT, P["bat_modulo"][1] / KWH_MODULO_BAT)
    cb_frio = (cb[0] / (T["dod"] * T["ef_bat"] * T["cop_noite"]), cb[1] / (T["dod"] * T["ef_bat"] * T["cop_noite"]))
    print(f"kWp adicional (modulo + estrutura):       {brl(ck[0])} a {brl(ck[1])} por kWp")
    print(f"Gelo adicional (tubo x 1,3):              R$ {cg[0]:.1f} a R$ {cg[1]:.1f} por kg  =  {brl(cg_kwh[0])} a {brl(cg_kwh[1])} por kWh de frio guardado")
    print(f"Bateria:                                  {brl(cb[0])} a {brl(cb[1])} por kWh eletrico nominal")
    print(f"Bateria tocando compressor (COP {T['cop_noite']}, uso {T['dod']*T['ef_bat']*100:.0f} %): {brl(cb_frio[0])} a {brl(cb_frio[1])} por kWh de frio guardado")
    print(f"Razao bateria / gelo, por kWh de frio guardado: {cb_frio[0]/cg_kwh[1]:.1f} a {cb_frio[1]/cg_kwh[0]:.1f} vezes")

    # ---------------------------------------------------------------- (a)
    sec("3(a). TANQUE DE GELO ARTESANAL x BANCO DE GELO COMERCIAL")
    art = [l for l in L if l[0].startswith("3 ")]
    ia = (sum(l[2] for l in art), sum(l[3] for l in art))
    n = T["anos"]; e10 = T["frio_pelo_gelo_dia"] * T["dias_ano"] * n
    fa = 1 + n * A_PAR["manut_art"] + A_PAR["p_retrab_art"] * A_PAR["f_retrab_art"]
    fc = 1 + n * A_PAR["manut_com"] + A_PAR["p_retrab_com"] * A_PAR["f_retrab_com"]
    cap = CFG["gelo_kg"] * KWH_POR_KG_GELO
    print(f"Capacidade: {CFG['gelo_kg']:.0f} kg = {cap:.1f} kWh de frio. Frio que passa pelo gelo em {n} anos: "
          f"{T['frio_pelo_gelo_dia']:.0f} x {T['dias_ano']} x {n} = {e10:,.0f} kWh [SUPOSTO]".replace(",", "."))
    print("Formula: custo em 10 anos = investimento x (1 + 10 x manutencao/ano + chance de retrabalho x fracao refeita)")
    print(f"Artesanal: investimento {brl(ia[0])} a {brl(ia[1])}  ({brl(ia[0]/cap)} a {brl(ia[1]/cap)} por kWh de capacidade)")
    print(f"           fator {fa:.2f}  ->  10 anos: {brl(ia[0]*fa)} a {brl(ia[1]*fa)}  =  R$ {ia[0]*fa/e10:.2f} a R$ {ia[1]*fa/e10:.2f} por kWh de frio entregue")
    if A_PAR["preco_comercial"] is None:
        print(f"Comercial: SEM PRECO. Fator {fc:.2f}. Preco de EMPATE (o comercial custa o mesmo em 10 anos): "
              f"{brl(ia[0]*fa/fc)} a {brl(ia[1]*fa/fc)}")
        eco = (CFG["kwp"] * C_PAR["ganho_cop_local"] * ck[0], CFG["kwp"] * C_PAR["ganho_cop_local"] * ck[1])
        print(f"           Se o comercial for de expansao direta (so com R513A) e render 10 % a mais de COP, vale ainda "
              f"{brl(eco[0])} a {brl(eco[1])} de painel a menos -> empate sobe para {brl(ia[0]*fa/fc+eco[0])} a {brl(ia[1]*fa/fc+eco[1])}")
    else:
        pc = A_PAR["preco_comercial"]
        print(f"Comercial: {brl(pc)}  ->  10 anos: {brl(pc*fc)}  =  R$ {pc*fc/e10:.2f} por kWh de frio entregue")

    # ---------------------------------------------------------------- (b)
    sec("3(b). ARRANJO SOLAR x GELO: dia de projeto e sequencia de dias nublados (sem fruta nova)")
    vr = (CFG["capacidade_t"] * 1000 * PRECO_ROCA, CFG["capacidade_t"] * 1000 * PRECO_CANAL)
    print(f"Carga com 1 t/dia: {T['carga_dia']} kWh/dia; sem fruta nova: {T['carga_sem_fruta']} kWh/dia; "
          f"dia nublado rende {T['y_nublado']:.2f} kWh de frio por kWp [TODOS PROVISORIOS]")
    print(f"Fruta em risco (5 t): {brl(vr[0])} (preco de roca) a {brl(vr[1])} (canal de compra publica)")
    print(f"{'kWp':>4}{'gelo kg':>8}{'sobra/falta dia proj.':>24}{'':>2}{'deficit nubl.':>14}{'dias nubl.':>11}{'aquec. dia seg.':>16}{'custo solar+gelo (meio)':>26}")
    print(f"{'':>4}{'':>8}{'(autor / revisor) kWh':>24}{'':>2}{'kWh/dia':>14}{'cobertos':>11}{'graus/dia':>16}{'R$':>26}")
    res = []
    for kwp in (8, 10, 12):
        for kg in (400, 600, 800):
            fa_, fr_ = kwp * T["y_autor"] - T["carga_dia"], kwp * T["y_revisor"] - T["carga_dia"]
            d = max(0.0, T["carga_sem_fruta"] - kwp * T["y_nublado"])
            dias = kg * KWH_POR_KG_GELO * T["gelo_inicio"] / d if d > 0 else float("inf")
            custo = kwp * meio(ck) + meio(ia) + (kg - CFG["gelo_kg"]) * meio(cg)
            res.append((kwp, kg, dias, custo))
            print(f"{kwp:>4}{kg:>8}{fa_:>+12.1f} /{fr_:>+7.1f}{'':>5}{d:>14.1f}{dias:>11.1f}{d / T['inercia_fruta']:>16.1f}{custo:>26,.0f}".replace(",", "."))
    base = min(res, key=lambda r: r[3])
    print(f"\nCusto de cada dia nublado coberto a mais, contra a combinacao mais barata ({base[0]} kWp, {base[1]} kg):")
    for kwp, kg, dias, custo in res:
        if (kwp, kg) == (base[0], base[1]): continue
        dd = dias - base[2]; dc = custo - base[3]
        ev = dc / (meio(vr) * FRACAO_PERDIDA)
        print(f"  {kwp:>2} kWp + {kg} kg: +{brl(dc)} para +{dd:.1f} dia(s)  ->  {brl(dc/dd) if dd > 0 else 'n/a'} por dia coberto; "
              f"paga-se se evitar {ev:.1f} perda(s) em 10 anos (perda = {FRACAO_PERDIDA*100:.0f} % da fruta [SUPOSTO])")
    print("\nOnde por R$ 1 para atravessar N dias nublados seguidos (R$ por kWh de frio disponivel na sequencia, ponto medio):")
    print(f"{'N dias':>7}{'mais gelo':>12}{'mais painel':>14}{'bateria no compressor':>24}")
    for nd in (1, 2, 3, 5, 10):
        print(f"{nd:>7}{meio(cg_kwh):>12,.0f}{meio(ck) / (T['y_nublado'] * nd):>14,.0f}{meio(cb_frio):>24,.0f}".replace(",", "."))
    print(f"  (o painel adicional so empata com o gelo acima de {meio(ck)/T['y_nublado']/meio(cg_kwh):.1f} dias nublados seguidos; "
          "mas o painel tambem serve nos dias normais e o gelo nao)")

    # ---------------------------------------------------------------- (c)
    sec("3(c). UNIDADE SELADA DE FABRICA x R513A MONTADO NO LOCAL")
    nm = CFG["n_maquinas"]; cp = C_PAR
    def dez(inv, manut): return inv * (1 + n * manut)
    sel = []; loc = []
    for k in (0, 1):
        equip = nm * P["cond_importada_posta"][k] * (1 + cp["margem_importadora"][k]) * (1 + cp["sobressalentes"]) + P["importacao_fixos"][k]
        mo = cp["diarias_selada"][k] * P["diaria_frigorista"][k]
        sel.append((equip + mo, dez(equip, cp["manut_selada"]) + mo))
        equip_l = nm * (P["cond_nacional"][k] + P["drive"][k]) + cp["extras_local"][k] + cp["gas_r513a_inicial"][k]
        mo_l = cp["diarias_local"][k] * P["diaria_frigorista"][k]
        gas10 = cp["gas_r513a_inicial"][k] * cp["vazamento_ano"][k] * n
        loc.append((equip_l + mo_l, dez(equip_l, cp["manut_local"]) + mo_l + gas10))
    cred = (CFG["kwp"] * cp["ganho_cop_local"] * ck[0], CFG["kwp"] * cp["ganho_cop_local"] * ck[1])
    print(f"{nm} maquinas em cada opcao [PROVISORIO].")
    print(f"Selada importada (via importadora): investimento {brl(sel[0][0])} a {brl(sel[1][0])}; em 10 anos {brl(sel[0][1])} a {brl(sel[1][1])}")
    print(f"R513A montado no local:             investimento {brl(loc[0][0])} a {brl(loc[1][0])}; em 10 anos {brl(loc[0][1])} a {brl(loc[1][1])}")
    print(f"Credito possivel do R513A com expansao direta no gelo (+10 % de COP [SUPOSTO] = {CFG['kwp']*cp['ganho_cop_local']:.1f} kWp a menos): {brl(cred[0])} a {brl(cred[1])}")
    print(f"Diferenca em 10 anos (selada - local), sem o credito: {brl(sel[0][1]-loc[1][1])} a {brl(sel[1][1]-loc[0][1])}")
    e_tot = T["carga_dia"] * T["dias_ano"] * n
    print(f"Por kWh de frio em 10 anos ({e_tot:,.0f} kWh): selada R$ {sel[0][1]/e_tot:.3f} a {sel[1][1]/e_tot:.3f}; local R$ {loc[0][1]/e_tot:.3f} a {loc[1][1]/e_tot:.3f}".replace(",", "."))
    print("NAO esta na conta (sem dado): preco e existencia da unidade selada certa; preco do R513A; custo de parada por falta de assistencia; restricao futura a HFC.")

    # ---------------------------------------------------------------- (d)
    sec("3(d). BATERIA DE APOIO: o tamanho que compensa")
    for w in T["aux_noite_w"]:
        e = w * T["horas_noite"] / 1000; nom = e / (0.8 * T["ef_bat"])
        print(f"Cargas da noite {w} W x {T['horas_noite']:.0f} h = {e:.1f} kWh  ->  bateria nominal (80 % de uso, 90 % de rendimento) = {nom:.1f} kWh "
              f"= {nom/KWH_MODULO_BAT:.1f} modulo(s) de 5,12 kWh  ->  {brl(-(-nom//KWH_MODULO_BAT)*P['bat_modulo'][0])} a {brl(-(-nom//KWH_MODULO_BAT)*P['bat_modulo'][1])}")
    ger_nub = CFG["kwp"] * 2.0 * 0.75
    print(f"Dia nublado (2,0 kWh/m2, desempenho 0,75): {CFG['kwp']:.0f} kWp geram cerca de {ger_nub:.0f} kWh eletricos; "
          f"as cargas auxiliares de 24 h pedem {T['aux_noite_w'][0]*24/1000:.1f} a {T['aux_noite_w'][1]*24/1000:.1f} kWh.")
    print("  -> mesmo em dia nublado os paineis recarregam a bateria das cargas auxiliares, SE o arranjo eletrico permitir (pergunta ao integrador).")
    for dias in (1, 2, 3):
        falta = T["carga_sem_fruta"] * dias
        kwh_bat = falta / (T["dod"] * T["ef_bat"] * T["cop_noite"])
        kg = falta / KWH_POR_KG_GELO
        print(f"Cobrir {dias} dia(s) sem sol nenhum e sem fruta nova ({falta:.0f} kWh de frio): "
              f"so bateria = {kwh_bat:.0f} kWh ({brl(kwh_bat*cb[0])} a {brl(kwh_bat*cb[1])}); "
              f"so gelo = {kg:.0f} kg ({brl(kg*cg[0])} a {brl(kg*cg[1])} de tubo, fora tanque maior)")
    print(f"Reposicao: bateria com vida de 10 anos [SUPOSTO; garantias de 5 a 10 anos] -> {brl(P['bat_modulo'][0]/10)} a {brl(P['bat_modulo'][1]/10)} por modulo por ano.")

    # ---------------------------------------------------------------- 4 receita e retorno
    sec("4. RECEITA E RETORNO (receita do doc 10 s.6.2, so manga, 5 t)")
    kgcap = CFG["capacidade_t"] * 1000
    print(f"{'Cenario':<12}{'Receita/ano':>13}{'Sobra s/ operador':>19}{'Sobra c/ operador':>19}{'Retorno simples (anos), custo min / max':>42}")
    rec = {}
    for nome, c in CEN.items():
        r = kgcap * c["ocup"] * c["dias"] * c["taxa"]; rec[nome] = r
        s1, s2 = r - OPEX_SEM_OPERADOR, r - OPEX_COM_OPERADOR
        pb = f"{tmn/s1:.0f} / {tmx/s1:.0f}" if s1 > 0 else "nunca"
        pb2 = f"{tmn/s2:.0f} / {tmx/s2:.0f}" if s2 > 0 else "nunca"
        print(f"{nome:<12}{brl(r):>13}{brl(s1):>19}{brl(s2):>19}{'sem oper.: ' + pb + ' | com oper.: ' + pb2:>42}")
    print("\nMaior custo que cada cenario paga em 10 anos = (receita - operacao) / fator   [mesma conta do doc 10 s.6.3]")
    for nome, r in rec.items():
        for op, rot in ((OPEX_SEM_OPERADOR, "sem operador"), (OPEX_COM_OPERADOR, "com operador")):
            xs = "; ".join(f"{k}: " + (brl((r - op) / fator(i)) if r > op else "nao paga") for k, i in JUROS.items())
            print(f"  {nome:<11}{rot:<13}{xs}")
    print("  -- leitura do revisor (revisao-10-demanda.md) --")
    for nome, r in REC_REVISOR.items():
        xs = "; ".join(f"{k}: " + (brl((r - OPEX_SEM_OPERADOR) / fator(i)) if r > OPEX_SEM_OPERADOR else "nao paga") for k, i in JUROS.items())
        pb = f"{tmn/(r-OPEX_SEM_OPERADOR):.0f} / {tmx/(r-OPEX_SEM_OPERADOR):.0f} anos" if r > OPEX_SEM_OPERADOR else "nunca"
        print(f"  {nome:<16}{brl(r):>10} sem operador: {xs} | retorno simples (custo min/max): {pb}")
    print(f"  Quadro de custos desta rodada: {brl(tmn)} a {brl(tmx)}")
    print("\nReceita anual necessaria para empatar (parcela de 10 anos + operacao):")
    print(f"{'Custo':>12}" + "".join(f"{k + ', op 12k':>24}{k + ', op 36k':>24}" for k in JUROS))
    for x in (tmn, (tmn + tmx) / 2, tmx):
        print(f"{brl(x):>12}" + "".join(f"{brl(x*fator(i)+OPEX_SEM_OPERADOR):>24}{brl(x*fator(i)+OPEX_COM_OPERADOR):>24}" for i in JUROS.values()))
    print("\nTaxa de empate, R$ por kg por dia e por caixa de 20 kg por dia (Pronaf 2 %, sem operador pago):")
    for nome, c in CEN.items():
        for x, rot in ((tmn, "custo min"), (tmx, "custo max")):
            t = (x * fator(0.02) + OPEX_SEM_OPERADOR) / (kgcap * c["ocup"] * c["dias"])
            print(f"  {nome:<11}{rot:<10} R$ {t:.3f}/kg.dia = R$ {t*20:.2f}/caixa.dia  (taxa do cenario: R$ {c['taxa']:.2f}/kg.dia)")
    print("\nOcupacao de empate com a taxa media (R$ 0,06/kg.dia, 240 dias, Pronaf 2 %, sem operador):")
    for x, rot in ((tmn, "custo min"), ((tmn + tmx) / 2, "custo medio"), (tmx, "custo max")):
        oc = (x * fator(0.02) + OPEX_SEM_OPERADOR) / (kgcap * 240 * 0.06)
        print(f"  {rot:<12}{brl(x):>12}: {oc*100:.0f} %" + ("  (acima de 100 %: nao empata)" if oc > 1 else ""))
    print("\nSensibilidade do resultado anual no cenario medio (Pronaf 2 %, sem operador), custo no ponto medio:")
    xm = (tmn + tmx) / 2; c = CEN["medio"]
    def resultado(x=xm, ocup=c["ocup"], taxa=c["taxa"]):
        return kgcap * ocup * c["dias"] * taxa - x * fator(0.02) - OPEX_SEM_OPERADOR
    print(f"  base: {brl(resultado())}")
    for rot, kw in (("ocupacao 45 % -> 70 %", dict(ocup=0.70)), ("ocupacao 45 % -> 20 %", dict(ocup=0.20)),
                    ("taxa 0,06 -> 0,10", dict(taxa=0.10)), ("taxa 0,06 -> 0,03", dict(taxa=0.03)),
                    ("custo no minimo", dict(x=tmn)), ("custo no maximo", dict(x=tmx))):
        print(f"  {rot:<24}: {brl(resultado(**kw))}")
    imp = [l for l in L if l[0][:1] in "45" or "Maquina" in l[1]]
    fmn = sum(l[2] for l in imp) / smn; fmx = sum(l[3] for l in imp) / smx
    print(f"  cambio: itens ligados ao dolar (modulos, bateria, inversores, maquina) = {fmn*100:.0f} % a {fmx*100:.0f} % do subtotal; "
          f"dolar +20 % -> custo total +{fmn*20:.0f} % a +{fmx*20:.0f} %")
    print("\nGanho das familias (nao e receita do dono): fruta que passa por ano x R$ 1,00/kg a mais de preco [doc 10 s.6.4]")
    for nome, cc, perm in (("pessimista", CEN["pessimista"], 6), ("medio", CEN["medio"], 5), ("otimista", CEN["otimista"], 4)):
        tano = kgcap * cc["ocup"] / perm * cc["dias"] / 1000
        print(f"  {nome:<11}: {tano:.0f} t/ano -> {brl(tano*1000)} por ano")

    # ---------------------------------------------------------------- 5 opex
    sec("5. CUSTO DE OPERACAO POR ANO")
    st = (P["starlink_mes"][0] * 12, P["starlink_mes"][1] * 12)
    man = (0.02 * smn, 0.03 * smx)
    bat = (P["bat_modulo"][0] / 10, CFG["bat_modulos"] * P["bat_modulo"][1] / 10)
    print(f"Starlink (A): {brl(st[0])} a {brl(st[1])}")
    print(f"Manutencao e pecas, 2 a 3 % do subtotal [SUPOSTO]: {brl(man[0])} a {brl(man[1])}")
    print(f"Reposicao de bateria (1/10 por ano) [B]: {brl(bat[0])} a {brl(bat[1])}")
    print(f"Operador: R$ 0 (pessoa da associacao) ou {brl(OPEX_COM_OPERADOR - OPEX_SEM_OPERADOR)} (dedicado) [doc 10, SUPOSTO]")
    print("Limpeza, seguro, licencas: SEM DADO")
    print(f"Soma do que tem numero, sem operador: {brl(st[0]+man[0]+bat[0])} a {brl(st[1]+man[1]+bat[1])}  (doc 10 supos R$ 12.000)")

    # ---------------------------------------------------------------- 6 financiamento
    sec("6. FINANCIAMENTO: parcela anual estimada (tabela Price, 10 anos, sem contar carencia)")
    print(f"{'Valor financiado':>18}" + "".join(f"{k:>18}" for k in JUROS))
    for x in (150000, 250000, 450000, tmn, tmx):
        print(f"{brl(x):>18}" + "".join(f"{brl(x*fator(i)):>18}" for i in JUROS.values()))
    print("Limites do Pronaf Mais Alimentos (doc 10 s.7): R$ 250 mil por familia; R$ 450 mil para fruticultura.")

if __name__ == "__main__":
    main()
