import datetime

class DeadEndFilling:
    """Luokka, joka löytää reitin labyrintissä Dead-end filling algoritmia käyttäen"""
    def __init__(self, labyrintti):
        """Luokan konstruktori, joka alustaa parametrina saamansa labyrintin
            Args:
                labyrintti: luotu labyrintti
        """
        self.labyrintti = labyrintti


    def naapurit(self, x, y):
        """Metodi, joka etsii ruudun naapurit

        Args:
            x:ruudun x-koordinaatti
            y: ruudun y-koordinaatti

        Returns:
            list: naapureista, jossa on "."
        """
        naapurit = []
        for i, j in [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]:
            if 0 <= i < len(self.labyrintti) and 0 <= j < len(self.labyrintti) and self.labyrintti[i][j] == '.':
                naapurit.append((i, j))
        return naapurit


    def ruudun_koordinaatti(self, ruutu):
        """Metodi, joks joka löytää sen hetkisen ruudun koordinsstit

            Args:
                ruutu: tän hetkinen ruutu
        """

        for i in range(len(self.labyrintti)):
            for j in range(len(self.labyrintti[0])):
                if self.labyrintti[i][j] == ruutu:
                    return i, j


    def dead_endit(self):
        """Metodi, joka löytää kaikki dead endit"""

        for k in self.labyrintti[1:-1]:
            for n in k[1:-1]:
                if n == '.':
                    i, j = self.ruudun_koordinaatti(n)
                    naapurit = self.naapurit(i, j)
                    if len(naapurit) == 1:
                        self.seinien_laitto(i, j)


    def seinien_laitto(self, x, y):
        """Metodi, joka laittaa seinät labyrinttiin, kunnes vastaan tulee polku
            Args:
                x: ruudun rivikoordinaatti
                y: ruudun sarakekoordinaatti
        """
        naapurit = self.naapurit(x, y)
        while len(naapurit) == 1:
            self.labyrintti[x][y] = "#" 
            x, y = naapurit[0]
            naapurit = self.naapurit(x, y)
        



       