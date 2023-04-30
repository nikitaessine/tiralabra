# Testausdokumentti

## Testit luokalle Labyrintti
setUp()

Metodissa setUp() määritellään labyrintti käyttämällä Labyrintinluonti-luokkaa. Labyrintti on 5 x 5 ruudun kokoinen ja sen aloitusruutu on vasemmassa yläkulmassa.

test_luo_ruudukko()

Testissä test_luo_ruudukko() varmistetaan, että labyrintin ruudukon koko on oikea. Tässä tapauksessa ruudukon kooksi on määritelty 5, joten testissä varmistetaan, että ruudukossa on 5 riviä.

test_aloitusruutu_oikein()

Testissä test_aloitusruutu_oikein() varmistetaan, että labyrintin aloitusruutu on oikein. Metodissa luodaan labyrintti, jossa aloitusruutu on vasemmassa yläkulmassa. Tämän jälkeen testataan, että ruudukon ensimmäinen ruutu on piste, joka symboloi aloitusruutua.

test_palauta_labyrintti()

Testissä test_palauta_labyrintti() varmistetaan, että palautetussa labyrintissa aloitusruutu on oikein. Metodissa luodaan labyrintti, jossa aloitusruutu on vasemmassa yläkulmassa. Tämän jälkeen labyrintti palautetaan ja testataan, että ruudukon ensimmäinen ruutu on piste, joka symboloi aloitusruutua.