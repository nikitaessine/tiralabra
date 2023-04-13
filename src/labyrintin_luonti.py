from labyrintti import Labyrintti
import random

class Labyrintinluonti():
    """Luokka, jossa luodaan labyrintti Primin algoritmia käyttäen"""
    

    def __init__(self, labyrintti:Labyrintti):
        """Luokan konstruktori, joka alustaa labyrintin luontiin tarvittavat tiedot
        ja rakenteet

        Args:
            labyrintti (Labyrintti): Labyrinttiolio, joka antaa labyrintin koon ja 
            aloituspisteen
        """

        self.korkeus = labyrintti.korkeus
        self.leveys = labyrintti.leveys
        self.aloitus_x = labyrintti.aloitus_x
        self.aloitus_y = labyrintti.aloitus_y
        self.ruudukko = []
        self.kaydyt_ruudut = []
        self.seinat = []

        self.ruudukko = [["#" for j in range(self.leveys)] for i in range(self.korkeus)]
        self.kaydyt_ruudut = [[0 for j in range(self.leveys)] for i in range(self.korkeus)]

    def luo(self,x,y):
        """Metodi, joka luo labyrintin

        Args:
            x: ruudun x-koordinaatti
            y: ruudun y-koordinaatti
        """

        

        if self.kaydyt_ruudut[x][y] == 1:
            return
        
        seina = self.naapurit(x,y)
        self.kaydyt_ruudut[x][y] = 1
        self.ruudukko[x][y] = '.'

        for i in seina:
            if i in self.seinat:
                self.seinat.remove(i)
                self.kaydyt_ruudut[i[0]][i[1]] = 1
            else:
                self.seinat.append(i)

        seinien_maara = len(self.seinat)

        if seinien_maara > 0:
            seuraava_seina = random.choice(self.seinat)
            self.seinat.remove(seuraava_seina)
            self.luo(seuraava_seina[0], seuraava_seina[1])
    
    def naapurit(self, x, y):
        """Metodi, joka etsii ruudun naapurit

        Args:
            x:ruudun x-koordinaatti
            y: ruudun y-koordinaatti

        Returns:
            list: oikeista naapureista
        """

        lista_naapureista = [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]
        random.shuffle(lista_naapureista)
        valid_naapurit = []

        for naapuri in lista_naapureista:
            naapuri_x, naapuri_y = naapuri
            if naapuri_x < 0 or naapuri_x >= self.korkeus or naapuri_y < 0 or naapuri_y >= self.leveys:
                continue
            if self.kaydyt_ruudut[naapuri_x][naapuri_y] == 1:
                continue
            valid_naapurit.append(naapuri)

        return valid_naapurit

    def maali_piste(self):
        """Metodi, joka arpoo päätepisteen
        """
        loppu_piste = random.randint(1, self.leveys-2)
        for i in range(self.korkeus-2, 1, -1):
            if self.ruudukko[i][loppu_piste] == ".":
                self.ruudukko[i][loppu_piste+1] = "L"
                return



    def palauta(self):
        """Metodi palauttaa valmiin labyrintin

        Returns:
            list: valmis labyrintti
        """

        self.luo(self.aloitus_x, self.aloitus_y)
        self.maali_piste()

        return self.ruudukko