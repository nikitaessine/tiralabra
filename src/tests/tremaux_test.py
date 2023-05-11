import unittest
from tremaux import TremauxSolver
class TestTremauxSolver(unittest.TestCase):

    def setUp(self):

        self.labyrintti = [['.', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                     ['#', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
                     ['#', '.', '.', '.', '#', '.', '.', '.', '#', '#'],
                     ['#', '.', '#', '.', '.', '.', '#', '.', '#', '#'],
                     ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
                     ['#', '.', '.', '.', '.', '#', '.', '.', 'L', '#'],
                     ['#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
                     ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.tremaux = TremauxSolver(0, 0)
        self.tremaux.labyrintti = self.labyrintti

        self.tremaux2 = TremauxSolver(3,3)
        self.tremaux2.labyrintti = self.labyrintti

    def test_hae_alku(self):

        self.assertEqual(self.tremaux.hae_alku(), (0, 0))

    def test_hae_vierailtavat_naapurit(self):

        naapurit = self.tremaux.hae_vierailtavat_naapurit((1, 0))
        self.assertEqual(naapurit, [(0, 0),(1, 1)])

    def test_hae_seuraava_ruutu(self):

        seuraava_ruutu = self.tremaux.hae_seuraava_ruutu((1, 0), [(0, 0), (1, 1)])
        self.assertEqual(seuraava_ruutu, (0, 0))

    def test_on_loppu(self):

        self.assertTrue(self.tremaux.on_loppu((6, 8)))

    def test_lopullinen_polku(self):

        self.tremaux.ratkaisu()
        lopullinen_polku = self.tremaux.polku
        self.assertEqual(lopullinen_polku, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (7, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8)] )

    def lopullinen_polku_eri_aloituspisteella(self):

        self.tremaux2.ratkaisu()
        lopullinen_polku = self.tremaux2.polku
        self.assertEqual(lopullinen_polku, [(3, 3), (4, 3), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (7, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8)])