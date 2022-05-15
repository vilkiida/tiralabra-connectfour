# Toteutusdokumentti

#### Ohjelman yleisrakenne:
Ohjelmalla on graafinen käyttöliittymä. Käynnistettyä aukeaa pelivalikko, josta voi hiireä käyttämällä valita vastuksen ja vaikeustason ja aloittaa siten haluamansa pelin.

#### Saavutetut aika- ja tilavaativuudet:
Alpha beta karsinnalla aikavaativuus pitäisi olla O(sqrt(b^d)), missä b on lukuarvo, joka kuvaa kuinka moneen solmuun haarautuu yksi minimax algoritmin puun solmu (7 koska pelilaudassa on 7 saraketta). D kuvaa syvyyttä. Saavutetut syvyydet ovat: 
vaikeustaso "helppo" --> 3
vaikeustaso "vaikea" --> 5
vaikeustaso "tosi vaikea" --> 6

#### Työn mahdolliset puutteet ja parannusehdotukset:
Minimax algoritmia varten pelilaudan eri tilanteille arvosanoja laskeva funktio voisi olla tehokkaampi ja siten laskentasyvyyttä voitaisiin kasvattaa. Tällä hetkellä se on noin 5-6 ja se voisi olla isompikin. Tekoäly kuitenkin pelaa tälläkin syvyydellä ihan hyvin.

Koska tekoäly käyttää minimax algoritmia, se ei välttämättä toimi niin hyvin kun pelaajan siirrot tehdään randomisti, koska minimax algoritmi olettaa vastapelaajan myös yrittävän tehdä otollisimmat siirrot omalta kannaltaan.

#### Lähteet:
[Minimax algoritmi - Wikipedia](https://en.wikipedia.org/wiki/Minimax)

[Alpha Beta karsinta - Wikipedia](https://en.wikipedia.org/wiki/Alpha_Beta)

[Connect Four - Wikipedia](https://en.wikipedia.org/wiki/Connect_Four)

[Alpha Beta karsinnan ja minimax:in ideaa selventävä youtube-video](https://www.youtube.com/watch?v=l-hh51ncgDI)

##### Kuvien lähteet:
Pelin kaikki viisi kuvaa: [c4_empty.png](https://github.com/vilkiida/tiralabra-connectfour/blob/main/src/assets/c4_empty.png) (tyhjä pelilaudan ruutu), [c4_red.png](https://github.com/vilkiida/tiralabra-connectfour/blob/main/src/assets/c4_red.png) (punainen pelinappula pelaudan ruudussa), 
[c4_yellow.png](https://github.com/vilkiida/tiralabra-connectfour/blob/main/src/assets/c4_yellow.png) (keltainen pelinappula pelaudan ruudussa), [c4_red_piece.png](https://github.com/vilkiida/tiralabra-connectfour/blob/main/src/assets/c4_red_piece.png) (punainen pelinappula), [c4_yellow_piece.png](https://github.com/vilkiida/tiralabra-connectfour/blob/main/src/assets/c4_yellow_piece.png) (keltainen pelinappula) on itse piirrettyjä Procreate-sovelluksella.
