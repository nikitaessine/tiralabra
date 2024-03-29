from dead_end_filling import DeadEndFilling
from tremaux import TremauxSolver
import datetime

def main():


    while True:
        valinta = int(input("Haluatko ratkaista labyrintti dead-end filling algoritmilla vai Tremaux algoritmilla? (DEF(1),Tremaux(2), lopeta(0) "))
        
        if valinta == 1:

            dead_end_filling_polku = DeadEndFilling()


            alku = datetime.datetime.now()
            dead_end_filling_polku.dead_endit()
            loppu = datetime.datetime.now()

            print(' ')

            #print(f'Aikaa kului dead-end filling algoritmilla: {loppu-alku} sekunttia')
        
        if valinta == 2:

            aloitus_x = int(input("Anna aloitus x-koordinaatti: "))
            aloitus_y = int(input("Anna aloitus y-koordinaatti: "))

            tremaux_polku = TremauxSolver(aloitus_x,aloitus_y)

            alku2 = datetime.datetime.now()
            tremaux_polku.ratkaisu()
            loppu2 = datetime.datetime.now()

            

            #print(f'Aikaa kului tremaux algoritmilla: {loppu2-alku2} sekunttia')
        
        if valinta == 0:
            break

    
if __name__ == "__main__":
    main()