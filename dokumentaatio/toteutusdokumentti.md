# Totetutusdokumentti

## Ohjelman rakenne
Ohjelmassa on 2 luokkaa.

`TremauxSolver` löytää polun ennalta määrätyssä labyrintissa Tremaux algoritmilla.

`DeadEndFilling` löytää ennalta määrätyssä labyrintissa Dead-end filling algoritmilla.

Lisäksi `main.py` vastaa ohjelmannan toiminnasta ja kanssakäy käyttäjän kanssa.

## Saavutetut aika- ja tilavaativuudet

Dead-end filling pseudokoodina: 

![Screenshot from 2023-05-14 14-30-02](https://github.com/nikitaessine/tiralabra/assets/54572118/e845e799-efea-41a7-b558-be189ba2384d)

Dead-end filling ensin löytää kaikki umpikujat labyrintissä. Tämän jälkeen se täyttää kaikki umpukujat kunnes jää vain polku jäljelle. 
Tämän takia Dead-end fillingin aikavaatimuus on O(2n), jossa n on solmujen määrä. Tilavaatimus on O(n), koska se vain muuraa kaikki umpikujat labyrintissa.

Tremaux algortmi toteutuu ajassa O(N x M), jossa N on rivien määrä ja M on sarakkaiden määrä. Aikavaatimus riippuu täysin labyrintin koosta. 
Tilavaatimus on myös O(N x M), koska algoritmi tallentaa kaikki solmut ja mahdolliset reitit.

## Vertailu

Kun annetaan molemmille algoritmeille samat lähtö- ja lopetuspisteet niin huomataan, että Tremaux on nopeampi. Nämä tosiaan käyttävät erilaisia labyrintteja.
Tremauxilla on syklinen labyrintti ja Dead-end fillingilla on umpikujia. Tremauxin tehokkuus johtuu siitä, että se pyrkii minimoiimaan solmujen läpikäynti kertojen määrää. 

Pylint arvosana: 9.07/10

## Parannuksia

Molempien algoritmien kohdalla on mahdollisesti olemassa parempia toteutustapoja, jotka tehostaisivat niiden toimintaa. 
Projektiin myös voisi myös ottaa käyttöön algoritmin, joka generoisi labyrintteja.

## Lähteet

- [DEF pseudo](https://iopscience.iop.org/article/10.1088/1742-6596/1569/2/022059/pdf)
- [Tremaux](https://en.wikipedia.org/wiki/Maze-solving_algorithm#Tr%C3%A9maux's_algorithm)
- [DEF](https://en.wikipedia.org/wiki/Maze-solving_algorithm#Dead-end_filling)
