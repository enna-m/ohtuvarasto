import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def testi_lisays_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        # varaston pitäisi olla täynnä ja ylimääräinen menee "hukkaan"
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def testi_ottaminen_ei_tarpeeksi(self):
        self.varasto.lisaa_varastoon(2)

        # palauttaa paljonko varastosta voi ottaa ja saldo muuttuu 0
        self.assertAlmostEqual(self.varasto.ota_varastosta(3), 2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def testi_virheellinen_tilavuus(self):
        v = Varasto(-2)

        # virheellinen tilavvuus nollataan
        self.assertAlmostEqual(v.tilavuus, 0)

    def testi_virheellinen_alkusaldo(self):
        v = Varasto(10, -2)

        # virheellinen saldo nollataan
        self.assertAlmostEqual(v.saldo, 0)

    def testi_saldo_enemmän_kuin_tilavuus(self):
        v = Varasto(10, 12)

        # saldo täytetään tilavuuteen asti
        self.assertAlmostEqual(v.saldo, v.tilavuus)
    
    def testi_lisays_negatiivinen(self):
        alk_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-3)

        # saldo ei muuttunut
        self.assertAlmostEqual(self.varasto.saldo, alk_saldo)

    def testi_ottaminen_negatiivinen(self):
        alk_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-2)

        # saldo ei muuttunut
        self.assertAlmostEqual(self.varasto.saldo, alk_saldo)

    def testi_str_toimii(self):
        self.varasto.lisaa_varastoon(3)
        s = str(self.varasto)

        # string ja arvot tulostuvat oikein
        #
        self.assertAlmostEqual(s, f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")