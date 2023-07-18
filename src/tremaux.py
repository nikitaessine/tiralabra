import time, random

class TremauxSolver:
    """Luokka, joka ratkaisee labyrintin Tremaux'n algoritmilla."""
    def __init__(self, aloitus_x, aloitus_y):
        """Luokan konstruktori.
        Args:
        labyrintti: Lista listoja, joka edustaa sokkeloa.
        """
        self.labyrintti = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
    ['#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', 'L', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]


        self.vierailtu = []
        self.polku = []
        self.aloitus_x = aloitus_x
        self.aloitus_y = aloitus_y
        self.aloitus_koord = aloitus_x, aloitus_y
     

    def polun_isualisointi(self):
        """Askel askeleelta sokkelon visualisointi Tremaux-algoritmilla."""

        for i in range(50):
            print(" ") 

        print("Visualisaatio:")
        for i, row in enumerate(self.labyrintti):
            for j, cell in enumerate(row):
                if (i, j) == self.polku[-1]:
                    print('●', end=' ')  
                elif cell == '.' and (i, j) in self.vierailtu:
                    if self.count_marks(i, j) == 1:
                        print('•', end=' ')  
                    
                    elif self.count_marks(i, j) >= 2:
                        print('x', end=' ')

                    else:
                        print('.', end=' ') 
                else:
                    print(cell, end=' ')
            
            print(" ")

        time.sleep(0.1)

    def ratkaisu(self):
        aloitus = self.hae_alku()
        self.polku.append(self.aloitus_koord)
        self.vierailtu.append(aloitus)
        self.polun_isualisointi()

        while self.polku:
            nykyinen = self.polku[-1]
            naapurit = self.hae_vierailtavat_naapurit(nykyinen)

            if naapurit:
                seuraava_ruutu = self.hae_seuraava_ruutu(nykyinen, naapurit)
                self.vierailtu.append(seuraava_ruutu)
                self.polku.append(seuraava_ruutu)
                self.polun_isualisointi()

                if self.on_loppu(seuraava_ruutu):
                    return self.polku
            else:
                if self.count_marks(nykyinen[0], nykyinen[1]) == 1:
                    self.labyrintti[nykyinen[0]][nykyinen[1]] = 'x'
                    self.polku.pop()
                    self.polun_isualisointi()

        return None


    def count_marks(self, i, j):
        """Laskee kuinka monta kertaa ollaan käyty tietyssä pisteessä."""
        count = 0
        for (x, y) in self.vierailtu:
            if self.labyrintti[x][y] == '.' and x == i and y == j:
                count += 1
        return count

    
    def hae_alku(self):
        """Etsitään aloitusruutu labyrintista."""
        return (self.aloitus_x, self.aloitus_y)

    def hae_vierailtavat_naapurit(self, ruutu):
        """Etsitään nykyisen ruudun vierailtavat naapurit.

        Args: ruutu: nykyinen ruutu
        """
        naapurit = []
        rivi, sarake = ruutu
        for r, s in [(rivi-1, sarake), (rivi+1, sarake), (rivi, sarake-1), (rivi, sarake+1)]:
            if (0 <= r < len(self.labyrintti) and 0 <= s < len(self.labyrintti[0])
                and self.labyrintti[r][s] != '#' and (r, s) not in self.vierailtu):
                naapurit.append((r, s))
        return naapurit

    def hae_seuraava_ruutu(self, nykyinen, naapurit):
        """Palauttaa seuraavan ruudun, jossa vieraillaan.
        
        Args: naapurit: ruudun naapurit

        """
        if len(naapurit) == 1:
            return naapurit[0]
        ei_kayty = [n for n in naapurit if n not in self.vierailtu]
        if len(ei_kayty) == 1:
            return ei_kayty[0]
        return naapurit[0]

    def on_loppu(self, ruutu):
        """Tarkistaa, onko annettu ruutu loppupiste labyrintissa."""
        rivi, sarake = ruutu
        return self.labyrintti[rivi][sarake] == 'L'
