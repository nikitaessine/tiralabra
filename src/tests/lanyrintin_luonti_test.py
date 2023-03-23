import unittest
from labyrintin_luonti import Labyrintinluonti
from labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setUp(self):
        self.labyrintti = Labyrintinluonti(Labyrintti(5, 5, 1, 1))

    def test_luo_ruudukko(self):
        self.assertEqual(len(self.labyrintti.ruudukko), 5)