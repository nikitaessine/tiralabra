from labyrintti import Labyrintti
from labyrintin_luonti import Labyrintinluonti

def main():

    korkeus = int(input("Anna korkeus: "))
    leveys = int(input("Anna leveys: "))
    aloitus_x = int(input("Anna aloitus x-koordinaatti"))
    aloitus_y = int(input("Anna aloitus y-koordinaatti"))

    labyrintti_olio = Labyrintti(leveys, korkeus, aloitus_x, aloitus_y)
    Labyrintinluonti.luo(labyrintti_olio)

if __name__ == "__main__":
    main()