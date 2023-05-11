class TremauxSolver:
    """Luokka, joka ratkaisee labyrintin Tremaux'n algoritmilla."""
    def __init__(self, aloitus_x, aloitus_y):
        """Luokan konstruktori.
        Args:
        labyrintti: Lista listoja, joka edustaa sokkeloa.
        """
        self.labyrintti =  [['.', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                            ['#', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
                            ['#', '.', '.', '.', '#', '.', '.', '.', '#', '#'],
                            ['#', '.', '#', '.', '.', '.', '#', '.', '#', '#'],
                            ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
                            ['#', '.', '.', '.', '.', '#', '.', '.', 'L', '#'],
                            ['#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
                            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
                            ]


        self.vierailtu = []
        self.polku = []
        self.aloitus_x = aloitus_x
        self.aloitus_y = aloitus_y
        self.aloitus_koord = aloitus_x, aloitus_y
     
    def ratkaisu(self):
        """Ratkaistaan labyrintti ja palautetaan kuljettu polku."""

        aloitus = self.hae_alku()
        self.polku.append(self.aloitus_koord)
        self.vierailtu.append(aloitus)

        while self.polku:
            nykyinen = self.polku[-1]
            naapurit = self.hae_vierailtavat_naapurit(nykyinen)
            if naapurit:
                seuraava_ruutu = self.hae_seuraava_ruutu(nykyinen, naapurit)
                if seuraava_ruutu:
                    self.vierailtu.append(seuraava_ruutu)
                    self.polku.append(seuraava_ruutu)
                    if self.on_loppu(seuraava_ruutu):
                        #print('polku', self.polku)
                        return self.polku
            else:
                self.polku.pop()
    
    def polun_visualisointi(self):
        """Visualisoidaan polku askel askeleelta

        Returns:
            merkkijono: ruudukko_str
        """
        max_x = max(koordinaatti[0] for koordinaatti in self.polku)
        max_y = max(koordinaatti[1] for koordinaatti in self.polku)
        

        ruudukko = [['#'] * (max_x+2) for _ in range(max_y+2)]
        
        askeleet = 0
        for x, y in self.polku:
            askeleet += 1
            ruudukko[x][y] = '.'
            ruudukko_str = '\n'.join(''.join(rivi) for rivi in ruudukko)
            print(f"Askel {askeleet}:\n{ruudukko_str}")
       
        return ruudukko_str

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
