# Testausdokumentti

## Testaus

Tässä testataan, että molemmat algoritmit, Tremaux ja Dead-end filling, toimivat oikein.
Testit testaavat, että algoritmien käyttäytymistä eri läpikäyntivaiheissa.

### Tremaux

Tremaux algoritmia testataan kahdella eri testausobjektilla eri lähtöpisteillä.
Testauksessa käydään läpi onko nykyisen pisteen naapurit ja seuraavat mahdolliset pisteet oikein.
Tarkistetaan myös alku- ja loppupiste. Lopuksi tarkistetaan, että kuljettu polku on oikein. Tämä onnistui vertailemalla algoritmin käytyä polkua ennalta käsin kirjoitettuun polkuun.

### Dead-end filling

Dead-end fillingiä testataan yhdella testausobjektilla. 
Tässä myös tarkistetaan onko nykyisen pisteen naapurit oikein. Testataan, että onnistuuko seinien laitto oikein.
Lopuksi testataan, että jäljellä oleva polku on ainoa mahdollinen.

## Kattavuusraportti

![Screenshot from 2023-05-12 11-19-07](https://github.com/nikitaessine/tiralabra/assets/54572118/13bced1e-ccbb-4296-a1e0-9a5319c96081)

Tremaux algoritmin testauskattavuuden tiputtaa metodi, joka visualisoi polun. Tätä osaa ei testata, koska se ei liity algoritmiin.

## Testaus ohjeet 

Yksikkötestit saa ajettua komennolla:

```bash
 poetry run coverage run --branch -m pytest src
```
Testikattavuusraportin saa:

```bash
poetry run coverage html
```
Komentoriville testikattavuusraportin saa:

```bash
poetry run coverage report -m
```

