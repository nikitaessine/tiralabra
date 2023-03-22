from labyrintti import Labyrintti
from labyrintin_luonti import Labyrintinluonti

def main():

    korkeus = int(input("Anna korkeus: "))
    leveys = int(input("Anna leveys: "))

    labyrintti_olio = Labyrintti(leveys, korkeus)
    Labyrintinluonti.luo(labyrintti_olio)

if __name__ == "__main__":
    main()