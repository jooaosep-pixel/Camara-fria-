# -*- coding: utf-8 -*-
"""Telemetria e alertas no celular (Starlink/Wi-Fi).

Separada da logica: se a internet cair, o controle nao muda nada (a
simulacao prova isso no cenario "queda de internet").

- A cada 5 min monta um registro com as medidas principais.
- Alertas (eventos de alarme) saem na hora pelo bot do Telegram.
- Sem internet: tudo vai para uma fila circular (7 dias de registros de
  5 min = 2016 registros, mais 200 eventos) e e enviado quando voltar,
  mais antigo primeiro, com a hora original.
- Batimento ("estou vivo") a cada 5 min para um servico externo de
  vigilancia: se ele parar de chegar por 15 min, o SERVICO avisa no celular
  ("camara sem comunicacao"), porque a placa sem internet nao consegue avisar.

O envio real (HTTPS) fica em main_esp32.py; aqui so a fila, o formato e a
regra de envio, para poder testar no PC. Compativel com MicroPython.
"""

PERIODO_REGISTRO_S = 300
MAX_REGISTROS = 2016
MAX_EVENTOS = 200


class Telemetria:
    def __init__(self, nome="camara-01"):
        self.nome = nome
        self.fila_reg = []
        self.fila_evt = []
        self.t_ult_reg = -1e9
        self.enviados_reg = 0
        self.enviados_evt = 0
        self.descartados = 0
        self.mensagens = []   # o que foi "enviado" (para teste/simulacao)

    def registro(self, t, e, s):
        def r1(x):
            return None if x is None else round(x, 2)
        return {
            "t": t, "ar": r1(e.get("TT1")), "polpa": r1(e.get("TT2")),
            "lote": r1(e.get("TT3")), "gelo": r1(e.get("LT1")),
            "co2": r1(e.get("CO2")), "soc": r1(e.get("soc")),
            "G": r1(e.get("G")), "ext": r1(e.get("TT6")),
            "comp": [c["estado"] for c in s["comp"]],
            "hz": [round(c["freq"], 1) for c in s["comp"]],
            "aviso": s["aviso_base"], "alarmes": s["alarmes"],
        }

    def passo(self, t, e, s, internet_ok, enviar=None):
        for ev in s.get("eventos", []):
            self.fila_evt.append(ev)
            if len(self.fila_evt) > MAX_EVENTOS:
                self.fila_evt.pop(0)
                self.descartados += 1
        if t - self.t_ult_reg >= PERIODO_REGISTRO_S:
            self.t_ult_reg = t
            self.fila_reg.append(self.registro(t, e, s))
            if len(self.fila_reg) > MAX_REGISTROS:
                self.fila_reg.pop(0)
                self.descartados += 1
        if not internet_ok:
            return 0
        n = 0
        while self.fila_evt:
            ev = self.fila_evt.pop(0)
            txt = self.texto_alerta(ev)
            if enviar:
                enviar("alerta", txt)
            self.mensagens.append((t, txt))
            self.enviados_evt += 1
            n += 1
        while self.fila_reg:
            reg = self.fila_reg.pop(0)
            if enviar:
                enviar("registro", reg)
            self.enviados_reg += 1
            n += 1
        return n

    def texto_alerta(self, ev):
        h = int(ev["t"] // 3600) % 24
        m = int(ev["t"] % 3600 // 60)
        estado = "ATIVO" if ev["ativo"] else "normalizado"
        return "[%s] %02d:%02d %s %s: %s" % (self.nome, h, m, ev["sev"], estado, ev["msg"])
