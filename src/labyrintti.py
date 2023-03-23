class Labyrintti:
    """Luokka, joka luo labyrinttiolion """
    def __init__(self,leveys, korkeus, aloitus_x, aloitus_y):
        """Luokan konstruktori

        Args:
            leveys: labyrintin leveys
            korkeus: labyrintin korkeus
            aloitus_x: aloitus x-koordinaatti
            aloitus_y: aloitus y-koordinaatti
        """
        self.leveys = leveys
        self.korkeus = korkeus
        self.aloitus_x = aloitus_x
        self.aloitus_y = aloitus_y