import unittest
from dead_end_filling import DeadEndFilling

class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.labyrintti = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#'],
            ['#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        self.deadEndFilling = DeadEndFilling(self.labyrintti)

    def test_naapurit(self):
        self.assertEqual(self.deadEndFilling.naapurit(1, 1), [(1, 2), (2, 1)])
        
    def test_ruudun_koordinaatti(self):
        self.assertEqual(self.deadEndFilling.ruudun_koordinaatti('.'), (1, 1))
        self.assertEqual(self.deadEndFilling.ruudun_koordinaatti('#'), (0, 0))

    def test_seinien_laitto(self):
        self.deadEndFilling.seinien_laitto(2,1)
        self.assertEqual(self.labyrintti[2][1], '#')