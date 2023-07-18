import time

class DeadEndFilling:
    """Luokka, joka hakee reitin labyrintissa Dead-end filling-algoritmilla"""
    def __init__(self):
        """Luokan konstruktori

            Args:
                labyrintti: matriisi ratkaistavasta labyrintista
        """
        self.labyrintti = [['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '#'],
                            ['#', '.', '#', '.', '#', '#', '.', '.', '.', '#', '.', '.', '#', '.', '#'],
                            ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '.', '#'],
                            ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#', '#'],
                            ['#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
                            ['#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '.', '#', '#', '.', '#'],
                            ['#', '#', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '.', '.', '#'],
                            ['#', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '#'],
                            ['#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#'],
                            ['#', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#'],
                            ['#', '.', '.', '#', '#', '.', '.', '.', '#', '.', '#', '.', '#', '#', '#'],
                            ['#', '#', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.'],
                            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


    def naapurit(self, rivi, sarake):
        """Metodi, joka etsii ruudun naapurit

        Args:
            x:ruudun x-koordinaatti
            y: ruudun y-koordinaatti

        Returns:
            list: naapureista, jossa on "."
        """
        viereiset_ruudut = []
        n_rivit, n_sarakkeet = len(self.labyrintti), len(self.labyrintti[0])
        if rivi > 0 and self.labyrintti[rivi-1][sarake] != '#':
            viereiset_ruudut.append((rivi-1, sarake))
        if rivi < n_rivit-1 and self.labyrintti[rivi+1][sarake] != '#':
            viereiset_ruudut.append((rivi+1, sarake))
        if sarake > 0 and self.labyrintti[rivi][sarake-1] != '#':
            viereiset_ruudut.append((rivi, sarake-1))
        if sarake < n_sarakkeet-1 and self.labyrintti[rivi][sarake+1] != '#':
            viereiset_ruudut.append((rivi, sarake+1))
        return viereiset_ruudut

    def polun_visualisointi(self):
        """Visualisoi umikujien täyttöä ja jättää vain polun näkyville."""

        for i in range(40):
            print()

        print("Visualisaatio:")
        for row in self.labyrintti:
            for cell in row:
                print(cell, end=' ', flush=True)  # Add flush=True to force immediate output
            print(' ')
        

    def dead_endit(self):
        """Täyttää kaikki umpikujat kunnes jää vain polku näkyville."""
        while True:
            muutettu = False
            for rivi in range(1, len(self.labyrintti) - 1):
                for sarake in range(1, len(self.labyrintti[0]) - 1):
                    if self.labyrintti[rivi][sarake] == '.':
                        viereiset_ruudut = self.naapurit(rivi, sarake)
                        if len(viereiset_ruudut) == 1:
                            self.labyrintti[rivi][sarake] = '#'
                            muutettu = True
                            self.polun_visualisointi()  
                            time.sleep(0.1)  
            if not muutettu:
                break

    def seinien_laitto(self, rivi, sarake):
        """Täyttää labyrintin umpikujat rekursiivisesti seinillä, kunnes polkuun päästään.

        Args:
            rivi: rivin indeksi aloitusruudulle.
            sarake: sarakkeen indeksi aloitusruudulle.
        """
        viereiset_ruudut = self.naapurit(rivi, sarake)
        if len(viereiset_ruudut) == 1:
            self.labyrintti[rivi][sarake] = '#'
            self.seinien_laitto(viereiset_ruudut[0][0], viereiset_ruudut[0][1])


    
