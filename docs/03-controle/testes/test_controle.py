# -*- coding: utf-8 -*-
"""Testes automaticos. Rodar:  python3 -m unittest discover -s docs/03-controle/testes -v"""

import ast
import os
import sys
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..", "controlador"))
sys.path.insert(0, os.path.join(AQUI, "..", "simulacao"))

import config     # noqa: E402
import logica     # noqa: E402
import planta     # noqa: E402
import sim        # noqa: E402

DIA = 86400.0


def ent(t, **kw):
    """Entradas de uma camara normal ao meio-dia de sol forte."""
    e = {"t": t, "hora": kw.pop("hora", 12.0), "dia": kw.pop("dia", 0),
         "TT1": 12.0, "TT2": 12.8, "TT3": 13.0, "UR1": 88.0, "CO2": 0.30,
         "TT4": 0.5, "TT5": 3.0, "LT1": 50.0, "TT6": 34.0, "G": 900.0,
         "EI1": False, "porta": False, "botao_entrada": False,
         "pessoa_presa": False, "gas": False, "fluxo_ok": True,
         "com_inversor": True, "aux_kw": 0.3, "soc": 80.0, "pv_kw": 8.0,
         "carga_kw": 0.5, "T_glicol": -6.0,
         "comp": [{"PT1": 1.28, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False},
                  {"PT1": 1.28, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False}]}
    for k, v in kw.items():
        e[k] = v
    return e


def rodar(ctl, t0, t1, dt=10, **kw):
    s = None
    hist = []
    t = t0
    while t < t1:
        e = ent(t, **kw)
        s = ctl.passo(e)
        hist.append((t, s))
        t += dt
    return s, hist


class TestCompressor(unittest.TestCase):
    def test_espera_minimo_desligado_apos_energizar(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s, hist = rodar(ctl, 0, 600)
        primeira = min(t for t, s in hist if s["comp"][0]["liga"] or s["comp"][1]["liga"])
        self.assertGreaterEqual(primeira, 300)   # 5 min desligado depois da energizacao

    def test_minimo_ligado_e_recolhimento(self):
        cfg = config.montar("B")
        ctl = logica.Controlador(cfg, -1000.0)
        rodar(ctl, 0, 200)
        c = ctl.comps[0]
        self.assertTrue(c.ligado())
        t_on = c.t_ligou
        # banco enche logo depois da partida: o pedido some, mas respeita 3 min
        s, hist = rodar(ctl, 200, 900, LT1=100.0)
        deslig = [t for t, s in hist if s["comp"][0]["estado"] == "RECOLHENDO"]
        self.assertTrue(deslig, "deve passar por recolhimento")
        self.assertGreaterEqual(deslig[0] - t_on, cfg["comp"]["min_ligado_s"])
        rec = [s for t, s in hist if s["comp"][0]["estado"] == "RECOLHENDO"][0]
        self.assertFalse(rec["comp"][0]["solenoide"])   # solenoide fechada no recolhimento

    def test_maximo_partidas_por_hora_com_nuvens(self):
        ctl = logica.Controlador(config.montar("B"), -1000.0)
        t = 0
        while t < 3 * 3600:
            g = 900.0 if (t // 400) % 2 == 0 else 50.0     # nuvem a cada ~7 min
            ctl.passo(ent(t, G=g))
            for c in ctl.comps:
                self.assertLessEqual(c.partidas_ultima_hora(t), 6)
            t += 10

    def test_velocidade_minima_e_pouca_potencia(self):
        cfg = config.montar("B")
        ctl = logica.Controlador(cfg, -1000.0)
        # 1,5 kW disponiveis no arranjo todo: abaixo da partida (1,8 kW) -> nao parte
        g = (1.5 + 0.3) / (12.0 * 0.75) * 1000.0
        s, hist = rodar(ctl, 0, 1200, G=g)
        self.assertFalse(any(s["comp"][0]["liga"] or s["comp"][1]["liga"] for t, s in hist))
        # com sol parte; a frequencia nunca fica abaixo de 30 Hz
        s, hist = rodar(ctl, 1200, 2400, G=500.0)
        fs = [c["freq"] for t, s in hist for c in s["comp"] if c["liga"]]
        self.assertTrue(fs)
        self.assertGreaterEqual(min(fs), 30.0)
        self.assertLessEqual(max(fs), 70.0)
        # o sol cai para quase nada: parada forcada em ~20 s
        s, hist = rodar(ctl, 2400, 2500, G=30.0)
        self.assertFalse(s["comp"][0]["liga"] or s["comp"][1]["liga"])

    def test_alta_pressao_software_bloqueia_e_trava(self):
        cfg = config.montar("B")
        ctl = logica.Controlador(cfg, -1000.0)
        rodar(ctl, 0, 200)
        alta = [{"PT1": 1.28, "PT2": 17.0, "cadeia_ok": True, "inversor_falha": False},
                {"PT1": 1.28, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False}]
        s = ctl.passo(ent(210, comp=alta))
        self.assertEqual(s["comp"][0]["estado"], "BLOQUEADO")
        self.assertFalse(s["comp"][0]["liga"])
        # tres bloqueios em 1 h -> TRAVADO ate reset manual
        ctl.comps[0].bloquear(300, "teste", 10)
        ctl.comps[0].bloquear(400, "teste", 10)
        self.assertEqual(ctl.comps[0].estado, "TRAVADO")
        ctl.reset_manual(500)
        self.assertEqual(ctl.comps[0].estado, "PARADO")

    def test_cadeia_de_seguranca_aberta_desliga_na_hora(self):
        ctl = logica.Controlador(config.montar("B"), -1000.0)
        rodar(ctl, 0, 200)
        self.assertTrue(ctl.comps[0].ligado())
        aberta = [{"PT1": 1.28, "PT2": 12.0, "cadeia_ok": False, "inversor_falha": False},
                  {"PT1": 1.28, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False}]
        s = ctl.passo(ent(201, comp=aberta))
        self.assertFalse(s["comp"][0]["liga"])     # sem esperar o minimo ligado

    def test_sensor_de_pressao_em_falha_bloqueia_so_aquele(self):
        ctl = logica.Controlador(config.montar("B"), -1000.0)
        rodar(ctl, 0, 400)
        falho = [{"PT1": None, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False},
                 {"PT1": 1.28, "PT2": 12.0, "cadeia_ok": True, "inversor_falha": False}]
        s, hist = rodar(ctl, 400, 800, comp=falho)
        self.assertFalse(s["comp"][0]["liga"])
        self.assertTrue(s["comp"][1]["liga"])


class TestGlicolEAgua(unittest.TestCase):
    def test_anticongelamento_glicol(self):
        ctl = logica.Controlador(config.montar("A"), -1000.0)
        rodar(ctl, 0, 400)
        self.assertTrue(any(c.ligado() for c in ctl.comps))
        s = ctl.passo(ent(401, T_glicol=-9.0))
        self.assertFalse(any(c["liga"] for c in s["comp"]))
        s = ctl.passo(ent(411, T_glicol=-9.0))
        self.assertFalse(any(c["liga"] for c in s["comp"]))
        self.assertIn("A14", s["alarmes"])

    def test_sem_sensor_de_glicol_nao_liga(self):
        ctl = logica.Controlador(config.montar("A"), -1000.0)
        s, hist = rodar(ctl, 0, 600, T_glicol=None)
        self.assertFalse(any(c["liga"] for t, s in hist for c in s["comp"]))

    def test_sem_fluxo_nao_parte(self):
        ctl = logica.Controlador(config.montar("A"), -1000.0)
        s, hist = rodar(ctl, 0, 600, fluxo_ok=False)
        self.assertFalse(any(c["liga"] for t, s in hist for c in s["comp"]))
        self.assertTrue(s["bomba_banco"])     # a bomba P1 e pedida para dar fluxo

    def test_protecao_dano_por_frio(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s = ctl.passo(ent(0, TT1=10.2))
        self.assertFalse(s["bomba_p2"])
        self.assertAlmostEqual(s["vent_serp"], 0.30)

    def test_agua_6C_a_noite_e_3C_de_dia(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        self.assertEqual(ctl.passo(ent(0, hora=22.0))["agua_sp"], 6.0)
        ctl = logica.Controlador(config.montar("B"), 0.0)
        self.assertEqual(ctl.passo(ent(0, hora=12.0))["agua_sp"], 3.0)


class TestCO2(unittest.TestCase):
    def test_base_maximo_e_luz(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s = ctl.passo(ent(0, hora=20.0, CO2=0.32))
        self.assertEqual(s["ar_novo_m3h"], 30.0)
        self.assertEqual(s["luz_porta"], "VERDE")
        s = ctl.passo(ent(10, hora=20.0, CO2=0.45))
        self.assertEqual(s["ar_novo_m3h"], 60.0)
        self.assertEqual(s["luz_porta"], "VERMELHA")

    def test_sensor_co2_falho_e_seguro(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s = ctl.passo(ent(0, hora=20.0, CO2=None))
        self.assertEqual(s["ar_novo_m3h"], 60.0)
        self.assertEqual(s["luz_porta"], "VERMELHA")

    def test_purga_antes_da_primeira_entrada(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s = ctl.passo(ent(0, hora=6.0, CO2=0.30))
        self.assertEqual(s["ar_novo_m3h"], 60.0)


class TestRecepcao(unittest.TestCase):
    def _dia(self, ctl, d, G, lt1=60.0):
        for k in range(0, 24 * 60, 10):
            h = k / 60.0
            ctl.passo(ent(d * DIA + k * 60, hora=h, dia=d, G=G if 6 <= h <= 17 else 0.0, LT1=lt1))
        return ctl.aviso

    def test_regra_dia_nublado(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        self.assertEqual(self._dia(ctl, 0, 700.0), logica.AV_NORMAL)
        self.assertEqual(self._dia(ctl, 1, 150.0), logica.AV_MEIA)    # 1o nublado: meia no meio do dia
        self.assertEqual(self._dia(ctl, 2, 150.0), logica.AV_MEIA)    # 2o: meia desde cedo
        self.assertEqual(self._dia(ctl, 3, 150.0), logica.AV_NAO)     # 3o: nao receber
        self.assertEqual(self._dia(ctl, 4, 700.0), logica.AV_MEIA)    # sol voltou: meia
        self.assertEqual(self._dia(ctl, 5, 700.0), logica.AV_NORMAL)

    def test_gelo_baixo_nao_receber(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s = ctl.passo(ent(0, hora=8.0, LT1=15.0))
        self.assertEqual(s["aviso_base"], logica.AV_NAO)


class TestPrioridadeEBateria(unittest.TestCase):
    def test_bateria_so_toca_compressor_com_gelo_zerado_e_camara_quente(self):
        ctl = logica.Controlador(config.montar("B"), -1000.0)
        s, _ = rodar(ctl, 0, 600, hora=22.0, G=0.0, LT1=30.0, TT1=13.5, soc=95.0)
        self.assertFalse(s["bat_comp"])
        ctl = logica.Controlador(config.montar("B"), -1000.0)
        s, _ = rodar(ctl, 0, 600, hora=22.0, G=0.0, LT1=0.0, TT1=13.5, TT4=0.5, soc=95.0)
        self.assertTrue(s["bat_comp"])
        self.assertTrue(s["comp"][0]["liga"])
        self.assertEqual(s["comp"][0]["freq"], 30.0)
        s, _ = rodar(ctl, 600, 1200, hora=22.0, G=0.0, LT1=0.0, TT1=13.5, soc=55.0)
        self.assertFalse(s["bat_comp"])           # guarda a bateria das cargas noturnas

    def test_rota_a_respeita_soc(self):
        ctl = logica.Controlador(config.montar("A"), -1000.0)
        s, hist = rodar(ctl, 0, 900, soc=45.0)
        self.assertFalse(any(c["liga"] for t, s in hist for c in s["comp"]))
        ctl = logica.Controlador(config.montar("A"), -1000.0)
        s, hist = rodar(ctl, 0, 900, soc=80.0, pv_kw=10.0)
        partidas = sorted(c.t_ligou for c in ctl.comps if c.ligado())
        self.assertEqual(len(partidas), 2)
        self.assertGreaterEqual(partidas[1] - partidas[0], 30)  # partidas intertravadas
        s = ctl.passo(ent(901, soc=20.0, pv_kw=10.0))
        self.assertFalse(any(c["liga"] for c in s["comp"]))     # bateria critica

    def test_sensor_fora_da_faixa_vira_falha(self):
        ctl = logica.Controlador(config.montar("B"), 0.0)
        s, _ = rodar(ctl, 0, 100, TT1=85.0)
        self.assertIn("S-TT1", s["alarmes"])


class TestSegurancaIndependente(unittest.TestCase):
    def test_psh_de_hardware_desliga_mesmo_com_software_mandando_ligar(self):
        cfg = config.montar("B")
        pl = planta.Planta(cfg)
        pl.falha_vent_cond = True
        s = logica.saidas_estado_seguro(2)
        s["comp"][0].update({"liga": True, "freq": 70.0, "solenoide": True})  # software "com defeito"
        for k in range(10):
            pl.passo(13 * 3600 + k * 30, 13.0, 30.0, s, sim.RECORDE, True)
        self.assertTrue(pl.psh_aberto[0])
        self.assertFalse(pl._rod[0])

    def test_estado_seguro_sem_controlador(self):
        s = logica.saidas_estado_seguro(2)
        self.assertFalse(any(c["liga"] for c in s["comp"]))
        self.assertTrue(s["bomba_p2"])
        self.assertEqual(s["luz_porta"], "VERMELHA")


class TestPortabilidade(unittest.TestCase):
    def test_logica_so_importa_math(self):
        for nome in ("logica.py", "config.py", "telemetria.py"):
            with open(os.path.join(AQUI, "..", "controlador", nome)) as f:
                src = f.read()
            arv = ast.parse(src)
            for no in ast.walk(arv):
                if isinstance(no, ast.Import):
                    for a in no.names:
                        self.assertIn(a.name, ("math",), nome)
                if isinstance(no, ast.ImportFrom):
                    self.fail("import from em %s" % nome)


class TestSimulacao(unittest.TestCase):
    def test_dia_tipico_referencia(self):
        r = sim.rodar(config.montar("B", kwp=12, gelo_kg=700), [sim.dia(sim.TIPICO)] * 4)
        d = r["dias"][-1]
        self.assertLess(d["ar_max"], 13.0)
        self.assertGreater(d["ar_min"], 10.0)
        self.assertGreater(d["gelo_min"], 10.0)
        self.assertEqual(d["paradas_curtas"], 0)
        self.assertLessEqual(d["partidas_h_max"], 6)
        self.assertEqual(d["recebido_kg"], 1000.0)

    def test_internet_nao_muda_o_controle(self):
        cfg = config.montar("B")
        dias = [sim.dia(sim.TIPICO)] * 2
        a = sim.rodar(cfg, dias, registrar=True)
        b = sim.rodar(cfg, dias, registrar=True, internet_off=[(8 * 3600, 30 * 3600)])
        self.assertEqual(a["saidas"], b["saidas"])
        self.assertEqual(len(b["tel"].fila_reg), 0)          # tudo enviado depois

    def test_controlador_parado_nao_liga_compressor(self):
        cfg = config.montar("B")
        r = sim.rodar(cfg, [sim.dia(sim.TIPICO)] * 2, controlador_off=[(DIA, 2 * DIA)])
        self.assertLess(r["dias"][1]["comp_kwh"], 0.01)


if __name__ == "__main__":
    unittest.main()
