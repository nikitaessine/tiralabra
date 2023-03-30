from labyrintti import Labyrintti
from labyrintin_luonti import Labyrintinluonti
from dead_end_filling import DeadEndFilling
import datetime

def main():

    korkeus = int(input("Anna korkeus: "))
    leveys = int(input("Anna leveys: "))
    aloitus_x = int(input("Anna aloitus x-koordinaatti"))
    aloitus_y = int(input("Anna aloitus y-koordinaatti"))

    labyrintti_olio = Labyrintti(leveys, korkeus, aloitus_x, aloitus_y)
    labyrintti = Labyrintinluonti(labyrintti_olio).palauta()

    dead_end_filling_polku = DeadEndFilling(labyrintti)

    for i in labyrintti:
        print(i)

    alku = datetime.datetime.now()
    dead_end_filling_polku.dead_endit()
    loppu = datetime.datetime.now()

    print(f'Aikaa kului dead-end filling algoritmilla: {loppu-alku} sekunttia')
    
if __name__ == "__main__":
    main()