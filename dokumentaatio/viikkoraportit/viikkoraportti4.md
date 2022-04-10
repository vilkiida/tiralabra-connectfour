# Viikkoraportti 4
#### Käytetty aika:
ennen la klo 23.59 noin 6h. (4h sunnuntain puolella)

#### Mitä tein:
Täydensin minimax algoritmia ja lisäsin alpha beta karsintaa. Eniten aikaa kului pelitilanteen arvosanan määrittämisen koodaamiseen. Deadlinen aikaan ohjelmassa oli vielä bugi, jonka takia minimax algoritmi ei toiminut, mutta lisäämällä muutaman testin sain sen nyt sunnuntain puolella korjattua. Lisätty myös testejä ja muutama puuttuva ominaisuus pelistä.

#### Miten ohjelma edistynyt:
Deadlineen mennessä vielä ohjelma ei näytänyt edistyneen paljon sillä minimax algoritmissa oli jokin bugi, minkä takia AI valitsee oudosti siirtonsa. 
Sain sen kuitenkin sunnuntain puolella korjattua ja nyt yksinpeliäkin on mahdollista pelata. Tällä hetkellä minimax algoritmi katsoo binääripuuta alaspäin syvyyteen neljä. Pelissä nyt myös tasapeli tilanne ja ilmoitus siitä. "a"-näppäimellä nykyisen pelin saa aloitettua alusta ja "t"-näppäintä painamalla pääsee takaisin pelivalikkoon (näille tulossa myöhemmin vielä varmaan myös graafiset näppäimet).

#### Puutteita / mitä teen seuraavaksi:
mm.
- Testejä lisää.
- Täydennän dokumentaatiota
- Nopeutan minimax algoritmia vielä enemmän, jotta saan sen katsomaan pidemmälle eteenpäin ja jotta voin luoda vaikeustasot.

