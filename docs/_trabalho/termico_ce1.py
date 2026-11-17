import sys
sys.path.insert(0,'/home/user/Camara-fria-/docs/_trabalho')
import termico as T
def seq(n,kwp,kg,bat,rec):
    _,est=T.simula(kwp,kg,[("quente","ate14h")]*4,arq="b",bat=bat)
    r,_=T.simula(kwp,kg,[("nublado",rec)]*n,arq="b",bat=bat,estado=est)
    return r
def ok(r): return max(x["test_max"] for x in r)<=14.0 and max(x["tair_max"] for x in r)<=15.0
print("| kWp | bateria no compressor | recepcao | 1 dia: menor gelo | 2 dias: menor gelo | 3 dias: menor gelo |")
for kwp,bat in ((13.2,0.0),(13.2,5.0),(13.2,10.0)):
    for rec in ("meia","ate14h"):
        out=[]
        for n in (1,2,3):
            g=next((kg for kg in range(500,3001,100) if ok(seq(n,kwp,kg,bat,rec))),None)
            out.append(f"{g} kg" if g else ">3000")
        print(f"| {kwp} | {bat} | {rec} | "+" | ".join(out)+" |")
d,_=T.regime(13.2,700,"recorde","ate14h"); print("13,2 kWp+700 kg dia recorde: falta",round(d["falta"],1),"gelo min",round(d["smin"],1),"sobra FV",round(d["sobra"],1))
d,_=T.regime(13.2,500,"recorde","ate14h"); print("13,2 kWp+500 kg dia recorde: falta",round(d["falta"],1),"gelo min",round(d["smin"],1))
