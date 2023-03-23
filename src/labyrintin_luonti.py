from labyrintti import Labyrintti

class Labyrintinluonti():

    def __init__(self, labyrintti:Labyrintti):

        self.korkeus = labyrintti.korkeus
        self.leveys = labyrintti.leveys

    def luo(self):

        lista = [["#" for j in range(self.leveys)] for i in range(self.korkeus)]

        for i in lista:
            print(i)