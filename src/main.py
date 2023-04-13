from labyrintti import Labyrintti
from labyrintin_luonti import Labyrintinluonti
from dead_end_filling import DeadEndFilling
from tremaux import TremauxSolver
import datetime

def main():

    korkeus = int(input("Anna korkeus: "))
    leveys = int(input("Anna leveys: "))
    aloitus_x = int(input("Anna aloitus x-koordinaatti"))
    aloitus_y = int(input("Anna aloitus y-koordinaatti"))

    labyrintti_olio = Labyrintti(leveys, korkeus, aloitus_x, aloitus_y)
    labyrintti = Labyrintinluonti(labyrintti_olio).palauta()

    dead_end_filling_polku = DeadEndFilling(labyrintti)
    tremaux_polku = TremauxSolver(labyrintti, labyrintti_olio)

    for i in labyrintti:
        print(i)

    valinta = int(input("Haluatko ratkaista labyrintti dead-end filling algoritmilla vai Tremaux algoritmilla? (DEF(1),Tremaux(2),molemmat(3)"))
    
    if valinta == 1:

        alku = datetime.datetime.now()
        dead_end_filling_polku.dead_endit()
        loppu = datetime.datetime.now()
        print(f'Aikaa kului dead-end filling algoritmilla: {loppu-alku} sekunttia')
    
    if valinta == 2:

        alku2 = datetime.datetime.now()
        tremaux_polku.ratkaisu()
        loppu2 = datetime.datetime.now()

        print(f'Aikaa kului tremaux algoritmilla: {loppu2-alku2} sekunttia')
    
    if valinta == 3:

        alku = datetime.datetime.now()
        dead_end_filling_polku.dead_endit()
        loppu = datetime.datetime.now()
        print(f'Aikaa kului dead-end filling algoritmilla: {loppu-alku} sekunttia')

        alku2 = datetime.datetime.now()
        tremaux_polku.ratkaisu()
        loppu2 = datetime.datetime.now()

        print(f'Aikaa kului tremaux algoritmilla: {loppu2-alku2} sekunttia')

    
if __name__ == "__main__":
    main()