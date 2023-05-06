import unittest
from labyrintin_luonti import Labyrintinluonti
from labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setUp(self):
        self.labyrintti = Labyrintinluonti(Labyrintti(5, 5, 0, 0))

    def test_luo_ruudukko(self):
        self.assertEqual(len(self.labyrintti.ruudukko), 5)
    
    def test_aloitusruutu_oikein(self):
        self.labyrintti.luo(0, 0)
        self.assertEqual(self.labyrintti.ruudukko[0][0], "A")

    def test_palauta_labyrintti(self):
        self.labyrintti.palauta()
        self.assertEqual(self.labyrintti.ruudukko[0][0], "A")
        