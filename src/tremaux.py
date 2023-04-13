from labyrintti import Labyrintti

class TremauxSolver:
    """Luokka, joka ratkaisee sokkelon Tremaux'n algoritmilla."""
    def __init__(self, labyrintti, aloitus:Labyrintti):
        """TremauxRatkaisija-luokan konstruktori.
        Args:
        sokkelo: Lista listoja, joka edustaa sokkeloa.
        """
        self.labyrintti = labyrintti
        self.vierailtu = []
        self.polku = []
        self.aloitus_x = aloitus.aloitus_x
        self.aloitus_y = aloitus.aloitus_y
            
    def ratkaisu(self):
        """Ratkaistaan sokkelo Tremaux'n algoritmilla ja palautetaan kuljettu polku."""

        aloitus = self.hae_alku()
        self.polku.append(aloitus)
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
                        return self.polku
            else:
                self.polku.pop()

    def hae_alku(self):
        """Etsitään aloitusruutu labyrintista."""
        return (self.aloitus_x, self.aloitus_y)

    def hae_vierailtavat_naapurit(self, ruutu):
        """Etsitään labyrintin solmun vierailtavat naapurit.

        Args: ruutu: nykyinen solmu
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
