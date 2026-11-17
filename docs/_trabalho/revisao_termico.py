# -*- coding: utf-8 -*-
"""Conta independente do REVISOR (nao reutiliza termico.py do autor).
Escrita ANTES de ler os resultados do autor. Entradas: docs/00-premissas.md
e valores de engenharia do revisor (marcados SUP = suposicao do revisor)."""
import math

print("=== 1. INVOLUCRO: conteiner 20 pes isolado ===")
Lx, Wx, Hx = 6.058, 2.438, 2.591           # externo ISO 20' padrao
A_ext = 2*(Lx*Wx + Lx*Hx + Wx*Hx)
Li, Wi, Hi = 5.45, 2.29, 2.26              # interno tipico de reefer 20' (SUP, catalogos dao 5,44x2,29x2,27)
A_int = 2*(Li*Wi + Li*Hi + Wi*Hi)
A_med = math.sqrt(A_ext*A_int)
V_int = Li*Wi*Hi
print(f"A_ext={A_ext:.1f} m2  A_int={A_int:.1f} m2  A_media={A_med:.1f} m2  V_int={V_int:.1f} m3")
# U: PUR 100 mm lambda envelhecido 0,026 -> 0,26; +30% pontes termicas/envelhecimento/vedacao
for nome, U in (("novo/otimista", 0.26), ("usado realista", 0.35), ("usado ruim", 0.45)):
    print(f"  U={U:.2f} W/m2K ({nome}) -> UA={U*A_med:.1f} W/K")
UA = 0.35*A_med
print(f"UA adotado pelo revisor = {UA:.1f} W/K (reefer 20' novo certifica ~22-27 W/K; usado piora)")

def cargas(T_cam, resp_mW_kg, rotulo):
    print(f"\n=== 2. CARGA DIARIA - {rotulo} (camara {T_cam} C) ===")
    # ambiente: pico 40 C (premissa); noite cai. Dois casos: constante 40 e senoide 40/26
    T_max, T_min = 40.0, 26.0
    Tamb = [ (T_max+T_min)/2 + (T_max-T_min)/2*math.cos(2*math.pi*(h-15)/24) for h in range(24)]
    # cobertura sombreada: sem ganho solar direto no teto; +3 K em paredes ao sol durante o dia (SUP)
    q_tr_h = [UA*((Tamb[h] + (3 if 8 <= h <= 17 else 0)) - T_cam)/1000 for h in range(24)]
    E_tr = sum(q_tr_h)
    E_tr40 = UA*(40-T_cam)*24/1000
    print(f"Transmissao: {E_tr:.1f} kWh/dia (perfil 26-40 C)  | {E_tr40:.1f} kWh/dia (40 C constante, conservador)")
    # calor de campo
    m, cp = 1000.0, 3.7                    # kJ/kgK manga ~3,6-3,8 (84% agua)
    emb = 0.08*m*1.7                       # 8% de caixa plastica cp 1,7 (SUP)
    E_campo = (m*cp + emb)*(30-T_cam)/3600
    print(f"Calor de campo 1 t 30->{T_cam} C: {E_campo:.1f} kWh/dia (fruta {m*cp*(30-T_cam)/3600:.1f} + caixas)")
    # respiracao: 4 t ja frias + 1 t esquentando (media ~3x a taxa fria no dia de entrada)
    P_resp = (4000*resp_mW_kg + 1000*resp_mW_kg*3)/1e6
    E_resp = P_resp*24
    print(f"Respiracao: {resp_mW_kg} mW/kg frio -> {P_resp*1000:.0f} W -> {E_resp:.1f} kWh/dia")
    # infiltracao: psicrometria
    def h_ar(T, UR):
        ps = 610.94*math.exp(17.625*T/(T+243.04)); pv = UR*ps
        w = 0.622*pv/(101325*0.96 - pv)     # ~370 m altitude
        return 1.006*T + w*(2501+1.86*T), w
    ho, wo = h_ar(40, 0.30); hi, wi = h_ar(T_cam, 0.90)
    trocas = 12                            # trocas de ar/dia: 1 t entra + 1 t sai, ~20 aberturas com cortina (SUP)
    E_inf = trocas*V_int*1.15*(ho-hi)/3600
    agua = trocas*V_int*1.15*(wo-wi)
    print(f"Infiltracao: h_ext={ho:.1f} h_int={hi:.1f} kJ/kg, {trocas} trocas/dia -> {E_inf:.1f} kWh/dia; agua condensada {agua:.1f} kg/dia")
    E_vent = 0.20*24                       # ventiladores do evaporador 200 W continuos (SUP)
    E_pes = (2*0.27*1.5) + 0.05*1.5        # 2 pessoas 1,5 h + LED
    E_bomba = 0.08*24                      # bomba do secundario dissipa no fluido (SUP)
    print(f"Ventiladores {E_vent:.1f}  pessoas+luz {E_pes:.1f}  bomba {E_bomba:.1f} kWh/dia")
    tot = E_tr + E_campo + E_resp + E_inf + E_vent + E_pes + E_bomba
    tot40 = tot - E_tr + E_tr40
    print(f"TOTAL sem folga: {tot:.1f} kWh/dia (perfil) | {tot40:.1f} (40 C constante); com folga 10%: {tot*1.1:.1f} | {tot40*1.1:.1f}")
    # pico: campo retirado em ~8 h com decaimento exponencial (tau ~6 h p/ caixas ventiladas): pico inicial = E/tau
    tau = 6.0
    P_campo_pico = E_campo/tau
    P_pico = max(q_tr_h) + P_campo_pico + P_resp + 0.20 + 0.08 + E_inf/8
    print(f"PICO: campo {P_campo_pico:.2f} kW (tau {tau} h) + transm {max(q_tr_h):.2f} + resp {P_resp:.2f} + vent/bomba 0.28 + infiltr {E_inf/8:.2f} = {P_pico:.2f} kW")
    return dict(tot=tot, tot40=tot40, E_campo=E_campo, P_resp=P_resp, q_tr_h=q_tr_h, UA=UA, tau=tau, E_inf=E_inf)

manga = cargas(10, 45, "MANGA")    # manga 10-13 C: ~12-16 mg CO2/kg.h a 10 C -> ~35-50 mW/kg
caju = cargas(5, 60, "CAJU")       # pedunculo de caju a 5 C: taxa moderada-alta (SUP, pouca literatura)

print("\n=== 3. SOLAR E FRIO PRODUZIDO ===")
def cop(Tevap, Tcond, eta):
    return eta*(Tevap+273.15)/(Tcond-Tevap)
Tc = 40+12                                   # condensacao: ar 40 C + 12 K
# com secundario (glicol): camara: glicol ~+2 C -> evap -4 C ; gelo: evap -10 C
cop_cam_dx = cop(0, Tc, 0.55);  cop_cam_gl = cop(-5, Tc, 0.55);  cop_gelo = cop(-10, Tc, 0.52)
aux = 0.90                                   # ventilador do condensador + drive (fracao util)
print(f"COP (compressor) a Tcond {Tc} C: camara DX(0 C)={cop_cam_dx:.2f}  camara via glicol(-5 C)={cop_cam_gl:.2f}  gelo(-10 C)={cop_gelo:.2f}")
print(f"COP de sistema (x{aux} auxiliares): {cop_cam_dx*aux:.2f} / {cop_cam_gl*aux:.2f} / {cop_gelo*aux:.2f}")
PR = 0.80*0.88                               # PR 0,80 x 0,88 aproveitamento do acionamento direto (limiar de partida, sem bateria)
for nome, hsp in (("media anual Petrolina ~5,6", 5.6), ("pior mes (jun) ~4,7", 4.7), ("dia ruim ~2,5", 2.5)):
    for kwp in (5.0,):
        Eel = kwp*hsp*PR
        frio = Eel*(0.5*cop_cam_gl + 0.5*cop_gelo)*aux
        print(f"  {nome}: {kwp} kWp x {hsp} x PR {PR:.2f} = {Eel:.1f} kWh el -> frio ~{frio:.1f} kWh (50% modo camara, 50% modo gelo)")
cop_med = (0.5*cop_cam_gl + 0.5*cop_gelo)*aux
for rot, d in (("manga", manga), ("caju", caju)):
    for hsp in (5.6, 4.7):
        need = d["tot"]*1.1
        print(f"  kWp necessario {rot}, HSP {hsp}: {need:.1f}/( {hsp} x {PR:.2f} x {cop_med:.2f}) = {need/(hsp*PR*cop_med):.1f} kWp")

print("\n=== 4. GELO ===")
L = 334/3.6/1000   # kWh/kg = 0.0928
def gelo(d, T_cam, rot):
    # noite 14 h = 17h..07h ; ambiente do perfil
    noite = list(range(17,24))+list(range(0,7))
    E_tr_n = sum(d["q_tr_h"][h] for h in noite)
    base = E_tr_n + d["P_resp"]*14 + 0.12*14 + 0.08*14   # ventilador reduzido 120 W + bomba 80 W
    # campo: fruta entra 17 h (pior) -> fracao retirada em 14 h = 1-exp(-14/tau); de manha (7 h) -> resto que sobra p/ noite = exp(-10/tau)
    pior = base + d["E_campo"]*(1-math.exp(-14/d["tau"]))
    melhor = base + d["E_campo"]*math.exp(-10/d["tau"])
    fu = 0.80   # fracao util do gelo (nao derrete tudo, ganho do tanque, agua nao volta a 0 C)
    print(f"{rot}: noite 14 h base {base:.1f} kWh (transm {E_tr_n:.1f}); fruta de manha {melhor:.1f}; fruta 17 h {pior:.1f} kWh")
    for nome, E in (("sem fruta nova", base), ("fruta de manha", melhor), ("fruta 17 h", pior)):
        print(f"   {nome}: gelo liquido {E/L:.0f} kg -> a construir (util {fu:.0%}) {E/L/fu:.0f} kg")
    dia_nub = (d["tot"] - d["E_campo"] - d["E_inf"]*0.5)  # dia nublado sem receber fruta
    print(f"   1 dia inteiro sem sol e SEM receber fruta: {dia_nub:.1f} kWh -> {dia_nub/L/fu:.0f} kg; recebendo 1 t: {d['tot']:.1f} kWh -> {d['tot']/L/fu:.0f} kg")
    print(f"   200 kg de gelo = {200*L:.1f} kWh brutos, {200*L*fu:.1f} uteis -> cobre {200*L*fu/(base/14):.1f} h de noite sem fruta nova")
gelo(manga, 10, "MANGA"); gelo(caju, 5, "CAJU")

print("\n=== 5. BANCO DE GELO: executabilidade (conta de ordem de grandeza) ===")
for m in (200, 400, 600):
    # gelo sobre tubo: tubo PE/cobre De 20 mm, espessura de gelo 25 mm -> D=70 mm
    por_m = math.pi/4*(0.070**2-0.020**2)*917
    print(f"  {m} kg de gelo: {por_m:.2f} kg/m de tubo -> {m/por_m:.0f} m de tubo; agua total ~{m/0.6:.0f} L (60% congelado)")
# resistencia do gelo: carga em 6 h de 400 kg = 37 kWh/6 = 6,2 kW
kg_ice=0.070; R = math.log(0.070/0.020)/(2*math.pi*2.2)  # mK/W por metro, gelo cheio
print(f"  resistencia do gelo cheio (25 mm): {R:.3f} m.K/W -> com DT 8 K: {8/R:.0f} W/m no fim da carga (media ~2x)")

print("\n=== 6. LIMITE DE CARGA DE INFLAMAVEL (A3) no conteiner fechado ===")
for gas, LFL in (("R290", 0.038), ("R600a", 0.043)):
    A = Li*Wi
    for nomeV, V in (("vazio", V_int), ("com 5 t de fruta+caixas (~-9 m3)", V_int-9)):
        print(f" {gas} {nomeV}: V={V:.1f} m3 | LFL inteiro {LFL*V*1000:.0f} g | 20% LFL {0.2*LFL*V*1000:.0f} g | 25% LFL {0.25*LFL*V*1000:.0f} g")
    for h0, nm in ((0.6,"piso"),(1.8,"parede"),(2.2,"teto")):
        print(f"   EN378/ISO5149 m_max=2,5*LFL^1,25*h0*sqrt(A): h0={h0} ({nm}) -> {2.5*LFL**1.25*h0*math.sqrt(A)*1000:.0f} g")
    print(f"   IEC 60335-2-89:2019 teto por circuito: 13*LFL = {13*LFL*1000:.0f} g (~500 g), em aparelho de fabrica ensaiado; 150 g sem restricao de sala")
