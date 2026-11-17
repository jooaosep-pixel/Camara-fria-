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

# ====================================================================
# PARTE B - escrita DEPOIS de ler o documento do autor: conferencias pontuais
# ====================================================================
print("\n\n######## PARTE B: conferencias sobre os numeros do autor ########")
print("\n=== B1. Minha conta refeita com as entradas do autor (UA 33 W/K, respiracao 77 W/t manga / 60 caju) ===")
UA = 33.0
m10 = cargas(10, 77, "MANGA com UA=33 e 77 mW/kg (entradas do autor)")
c5 = cargas(5, 60, "CAJU com UA=33 (entradas do autor)")
print(f"-> manga: {m10['tot']*1.1:.1f} kWh/dia com folga (autor 69,8); caju: {c5['tot']*1.1:.1f} (autor 79,5)")
for rot, d, aut in (("manga", m10, 69.8), ("caju", c5, 79.5)):
    print(f"   kWp p/ {rot} (minha producao especifica {5.6*PR*cop_med:.2f} kWh frio/kWp.dia): {d['tot']*1.1/(5.6*PR*cop_med):.1f} kWp ; com a carga do autor {aut}: {aut/(5.6*PR*cop_med):.1f} kWp")
gelo(m10, 10, "MANGA UA=33"); gelo(c5, 5, "CAJU UA=33")

print("\n=== B2. Serpentina do tanque: potencia no fim da carga ===")
r_i, r_o, r_g = 0.006, 0.008, 0.018
for Nu, nome in ((4.36, "Nu 4,36 (autor, fluxo constante)"), (3.66, "Nu 3,66 (parede isotermica = gelo a 0 C)")):
    h = Nu*0.40/(2*r_i)
    R = 1/(h*2*math.pi*r_i) + math.log(r_o/r_i)/(2*math.pi*0.40) + math.log(r_g/r_o)/(2*math.pi*2.2)
    lm = (6-2)/math.log(6/2)
    print(f"  {nome}: R={R:.3f} m.K/W | autor usa DT=4,5 K -> {1070*4.5/R/1000:.1f} kW | media aritmetica 4,0 K -> {1070*4.0/R/1000:.1f} kW | DTML(-6/-2 contra 0)={lm:.2f} K -> {1070*lm/R/1000:.1f} kW")
print(f"  gelo por metro (16->36 mm): {math.pi/4*(0.036**2-0.016**2)*917:.3f} kg/m -> 800 kg = {800/(math.pi/4*(0.036**2-0.016**2)*917):.0f} m ; 500 kg = {500/(math.pi/4*(0.036**2-0.016**2)*917):.0f} m (reducao {1070-500/(math.pi/4*(0.036**2-0.016**2)*917):.0f} m, autor diz 670 m)")
print(f"  dilatacao: 800/917-800/1000 = {(800/917-0.8)*1000:.0f} L (autor 79 L) -> {(800/917-0.8)/1.9*100:.1f} cm em 1,9 m2")
print(f"  passes de tubo na secao: 1070/1,9 = {1070/1.9:.0f} passes; grade 40 mm em 1,0x1,0 m = 625 posicoes; curvas de 180 graus: ~{1070/1.9-22:.0f}; raio de curva exigido 20 mm x raio minimo PEX16 ~5xD = 80 mm")
print(f"  empuxo do gelo preso ao feixe: {800/917*1000-800:.0f} kgf para cima (precisa de ancoragem)")

print("\n=== B3. Hidraulica: P2 e P1 dividem a serpentina do tanque de dia ===")
for q in (0.9, 3.2, 3.2+2.4):
    print(f"  vazao na serpentina {q:.1f} m3/h -> perda (laminar, proporcional) {32*q/3.2:.0f} kPa = {32*q/3.2/10.2:.1f} m de coluna de glicol")
print("  P2 especificada com 4 m: so a serpentina do tanque, de dia (5,6 m3/h), ja pede ~5,4 m, fora serpentinas de ar, VM1 (15 kPa) e tubos")

print("\n=== B4. Descarga noturna no caso de dimensionamento (tudo a 5 C) ===")
ua_caju, ua_manga = 1540, 615
def lmtd(a, b): return (a-b)/math.log(a/b) if abs(a-b) > 1e-6 else a
# ar 5 -> ~3,5 C ; glicol +1 -> +3 C
dt = lmtd(5-3, 3.5-1)
print(f"  DTML ar 5->3,5 C x glicol +1->+3 C = {dt:.2f} K -> caju {ua_caju*dt/1000:.1f} kW + manga {ua_manga*dt/1000:.1f} kW = {(ua_caju+ua_manga)*dt/1000:.1f} kW (UA de vazao cheia de ar)")
carga_noite = [8.34, 6.87, 4.88, 4.41, 3.99, 3.62, 3.29, 3.01, 2.78, 2.58, 2.43, 2.31, 2.23, 2.53]
cap = (ua_caju+ua_manga)*dt/1000
nao = sum(max(0, c-cap) for c in carga_noite)
print(f"  carga do autor 17h-06h: {sum(carga_noite):.1f} kWh; nao atendido na hora com {cap:.1f} kW: {nao:.1f} kWh -> 5 t x 3,77 kJ/kgK = 5,2 kWh/K -> ar/fruta sobem ~{nao/5.2:.1f} K se fosse so inercia")
# ventiladores
for q_kw, dT in ((5.0, 2.5), (4.0, 3.0)):
    vaz = q_kw/(1.25*1.006*dT)
    print(f"  serpentina {q_kw} kW com ar caindo {dT} K: {vaz:.2f} m3/s = {vaz*3600:.0f} m3/h; com 40 Pa e rendimento 35%: {vaz*40/0.35:.0f} W eletricos")
print("  autor: 90 W + 60 W de dia, 50 W a noite (40% de rotacao = ~40% de vazao => capacidade e UA caem junto)")

print("\n=== B5. CO2 no conteiner fechado a noite (seguranca de quem abre a porta de manha) ===")
for nome, ml in (("manga 10 C, 14 ml/kg.h (UC Davis)", 14), ("fruta a 5 C, ~10 ml/kg.h (20 mg, suposicao do autor p/ caju)", 10.7)):
    vco2 = ml*5000/1e6   # m3/h
    for V in (10, 19, 23):
        print(f"  {nome}: {vco2*1000:.0f} L/h; 14 h fechado, ar livre {V} m3 -> {vco2*14/V*100:.1f} % CO2 (limite 8 h 0,5 %; perigo imediato 4 %; limite da manga 5 %)")
    print(f"    ar novo p/ segurar 0,5 %: {vco2/0.005:.0f} m3/h ; p/ 1 %: {vco2/0.01:.0f} m3/h")
ho, _ = (lambda T,UR: (1.006*T + 0.622*UR*610.94*math.exp(17.625*T/(T+243.04))/(97000-UR*610.94*math.exp(17.625*T/(T+243.04)))*(2501+1.86*T), 0))(33, 0.40)
print(f"  carga termica de 10 m3/h de ar novo (33 C/40% medio -> camara ~25 kJ/kg): ~{10*1.12*(ho-25)/3600*24:.1f} kWh/dia")

print("\n=== B6. Pressostato de baixa x congelamento do glicol ===")
print("  PSL do autor: 2,0 bar (evaporacao -25 C). Glicol 35% congela perto de -16 C -> o trocador de placas congela ANTES de o PSL atuar.")
print("  R290 na evaporacao 3,45 bar abs > pressao do circuito de glicol (~1,5-2,5 bar abs): placa rompida => propano entra no glicol e segue para dentro da camara.")

# ====================================================================
# PARTE C - RODADA 2: base nova (D1-D6). Conta independente do revisor,
# escrita antes de comparar com a tabela 5.3 do autor (eu ja tinha lido o texto).
# ====================================================================
print("\n\n######## PARTE C: RODADA 2 - so manga 12 C, 5 t, recepcao ate 14 h ########")
T_SET = 12.0
Tmax, Tmin = 41.0, 27.0
Tamb = [(Tmax+Tmin)/2 + (Tmax-Tmin)/2*math.cos(2*math.pi*(h-15)/24) for h in range(24)]
def resp_wt(T): return 83*2.5**((min(T,38)-10)/10)     # W/t
def h_ar(T, UR, p=97000):
    ps = 610.94*math.exp(17.625*T/(T+243.04)); w = 0.622*UR*ps/(p-UR*ps)
    return 1.006*T + w*(2501+1.86*T)
def dia(UA, tau, arnovo_m3h, t_entrada, T_fruta=35.0, vent_W=110):
    E = dict(env=0, porta=0, arnovo=0, campo=0, resp=0, aux=0)
    noite = 0.0
    # lotes: 250 kg por hora nas horas de entrada; simula 3 dias para regime
    lotes = []
    for d in range(3):
        for h in range(24):
            for th in t_entrada:
                if th == h: lotes.append([1000/len(t_entrada), T_fruta])
            q = {}
            q['env'] = UA*((Tamb[h] + (2 if 8 <= h <= 17 else 0)) - T_SET)/1000
            trocas_h = 12*(0.6/len(t_entrada) if h in t_entrada else 0.4/(24-len(t_entrada)))
            q['porta'] = trocas_h*28*1.15*(h_ar(Tamb[h],0.30)-h_ar(T_SET,0.88))/3600
            q['arnovo'] = arnovo_m3h*1.15*(h_ar(Tamb[h],0.30)-h_ar(T_SET,0.88))/3600
            qc = 0; qr = 4000*resp_wt(T_SET+0.8)/1e6
            novos = []
            for l in lotes:
                m, T = l
                dT = (T-T_SET)*(1-math.exp(-1/tau))
                qc += m*(3.77+0.09*1.9)*dT/3600
                qr += m*resp_wt(T)/1e6 - m*resp_wt(T_SET+0.8)/1e6
                l[1] = T-dT
                if l[1]-T_SET > 0.3: novos.append(l)
            lotes = novos
            q['campo'] = qc; q['resp'] = qr
            q['aux'] = (vent_W + 60 + 3.5*Tamb[h])/1000   # ventiladores + bomba P2 + ganho do banco
            if d == 2:
                for k in E: E[k] += q[k]
                if h >= 17 or h < 7: noite += sum(q.values())
    tot = sum(E.values())
    return tot, E, noite
L = 334/3600
for UA_ in (33, 23):
  for nome, ent in (("ate 14 h (10,11,12,13 h), 35 C", [10,11,12,13]), ("ate 10 h (7,8,9 h), 35 C", [7,8,9])):
    for ar in (10, 25):
        tot, E, noite = dia(UA_, 6.0, ar, ent)
        print(f"UA {UA_} | {nome} | ar novo {ar} m3/h: total {tot:.1f} kWh, com folga 10% {tot*1.1:.1f} | noite 17-7 h {noite:.1f} kWh -> gelo liquido {noite/L:.0f} kg, construido (util 85%) {noite/L/0.85:.0f} kg | " + ", ".join(f"{k} {v:.1f}" for k,v in E.items()))
tot8, _, noite8 = dia(33, 8.0, 10, [10,11,12,13])
print(f"mesma base com tau 8 h (autor): total {tot8:.1f}, com folga {tot8*1.1:.1f}; noite {noite8:.1f}")

print("\n--- C2. COP estimado pelo revisor (eta Carnot 0,55 compressor, x0,90 auxiliares de condensacao) ---")
cop_b = cop(-7, 51, 0.55)*0.90
cop_a = cop(-10.5, 51, 0.53)*0.90*0.94
print(f"(b) R513A DX no banco -7/+51: {cop_b:.2f} (autor 1,98) | (a) resfriador glicol -10,5/+51, x0,94 inversor de rede: {cop_a:.2f} (autor 1,70)")
for arq, c in (("(b)", cop_b), ("(a)", cop_a)):
    for hsp in (5.8, 4.7):
        tot, _, _ = dia(33, 6.0, 10, [10,11,12,13])
        need = tot*1.1
        # PR 0,75 x aproveitamento 0,88 (limiar de partida, banco cheio)
        print(f"  {arq} HSP {hsp}: kWp = {need:.1f}/({hsp} x 0,75 x 0,88 x {c:.2f}) = {need/(hsp*0.75*0.88*c):.1f} kWp")
print("  Obs.: o mes critico nao e junho (carga menor); e o dia quente com irradiacao ainda nao confirmada pelo SunData.")

print("\n--- C3. CO2 com a logica de setpoints do autor ---")
g = 5000*17/1e6   # m3/h
for q in (10, 20, 30):
    print(f"  ar novo {q} m3/h -> equilibrio {g/q*100+0.04:.2f} % CO2 ; carga termica ~{q*1.15*(h_ar(34,0.30)-h_ar(12,0.88))/3600*24:.1f} kWh/dia")
print("  Setpoints do autor: ventilador no maximo acima de 0,39 %. Com 10 m3/h o equilibrio e 0,89 % > 0,39 % -> o ventilador fica no MAXIMO quase sempre (30 m3/h -> 0,32 %). A carga somada (10 m3/h, 2,4 kWh) nao corresponde a logica: ~6 kWh/dia.")

print("\n--- C4. Banco (b): grades de cobre ---")
kgm = math.pi/4*(0.0627**2-0.0127**2)*917
print(f"  gelo por metro (tubo 12,7 -> cilindro 62,7 mm): {kgm:.2f} kg/m x 260 m = {kgm*260:.0f} kg (autor 700)")
print(f"  volume interno 1/2 pol (ID ~10,9 mm) x 258 m = {math.pi/4*0.0109**2*258*1000:.0f} L")
print(f"  13 grades x 90 mm = {13*0.09:.2f} m na largura de 1,25 m; 10 passes x 90 mm = 0,90 m de altura")
print(f"  tanque 2,30x1,25x1,05 = {2.3*1.25*1.05:.2f} m3; agua ~2,6 t; base 3,2 t em 3,0x1,8 m = {3200*9.81/(3.0*1.8)/1000:.1f} kPa no solo")

print("\n--- C5. Bateria de apoio na Rota B ---")
print("  Bateria 48 V (Elgin BAT-48V-5KWH) x inversor solar de bombeamento com entrada CC de 400-750 V: incompativel sem um inversor 48 V -> 220 V CA (ou conversor CC/CC elevador).")
print(f"  5 kWh x 0,92 (inversor) / 1,6-2,0 kW de compressor minimo = {4.6*0.92/1.8:.1f} h de compressor ; frio {4.6*0.92*2.9:.1f} kWh a COP 2,9")
