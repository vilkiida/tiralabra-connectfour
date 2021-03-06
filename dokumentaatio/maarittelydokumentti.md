# Määrittelydokumentti

#### Kieli: 
Kaikki dokumentointi ja peli itsessään on suomeksi. Koodi taas on kirjoitettu englanninkielellä.

#### Lyhyesti:
Kyseessä on siis Connect four -peli , jossa vastapuolet laittavat vuorotellen omanvärisensä nappulan 7x6 mittaisen pelilaudan ruutuihin (nappulat putoavat 
aina alimpaan mahdolliseen ruutuun valitulla rivillä). Ensimmäinen, joka saa neljä omaa nappulaansa peräkkäin, joko pystyy, vaakaan tai viistoon voittaa. Peliä voi pelata tekoälyä vastaan. Pelin toteutan Pygamea käyttäen.

#### Lisää:
- Pelaaja voi pelata tietokonetta vastaan.
- Pelaaja voi pelata myös toista pelaajaa vastaan
- Pelaaja voi valita pelaako tietokonetta vai toista pelaajaa vastaan.
- Siirrot tehdään klikkaamalla haluttua pystyriviä ruudukossa, jolloin nappula menee aina pohjimmaiseen ruutuun.
- Ruudukko on 7 ruutua leveä ja 6 ruutua korkea.
- Kummallakin pelaajalla on 21 merkkiä. (eli 21 punaista ja 21 keltaista)
- Ajastin laskee peliin käytettyä aikaa.

#### Opinto-ohjelmani:
Tietojenkäsittelytiede

#### Ohjelmointikieli:
Python 
(Hallitsen kunnolla käytännössä vain pyhtonia, mutta jos esimerkiksi koodikatselmuksessa ei ole tarjolla toista pythonilla tehtyä projektia, voin myös yrittää arvioida, jotakin pythonia läheisesti muistuttavalla kielellä tehtyä projektia.)

#### Käytettävät algoritmit:
Tarkoituksena on luoda tekoäly vastustaja, jotta peliä voi pelata myös ilman toista oikeaa pelaajaa. Tämän tietokone pelaajan ideana on tehdä aina parhain mahdollinen siirto itselleen. Tämä tekoäly luodaan käyttäen minimax algoritmia, jota sitten pyritään tehostamaan alpha-beeta karsinnalla eli jättämällä binääri puun turhia haaroja läpikäymättä. Karsinta tarpeellista! Alustavasti ainakin alpha-beeta karsintaa mutta myös mahdollisesti tehostamista läpikäyntijärjestyksen muuttamisen avulla.

#### Jos jää aikaa:
- voisi luoda tekoälypelaajalle vaikka kolme vaikeustasoa, jolloin mitä vaikeampi taso sen pitemälle tekoäly käy puussa läpi mahdollisia skenaarioita?
--> Tällöin helpommalla vaikeustasolla tekoäly päättää siirtonsa hieman nopeammin kuin vähän vaikeammalla tasolla?
--> Pelaaja voi siis valita haluamansa vaikeustason, jos valitsee pelin tietokonetta vastaan.

#### Aika- ja tilavaativuus arvio: 
aikaarvio: Alpha beta karsinnalla pitäisi olla O(sqrt(b^d)), missä d on minimax algoritmin syvyys ja b lukuarvo joka kuvaa moneenko solmuun jokainen puun solmu haarautuu (eli pääasiassa 7 koska 7 saraketta).

- Tekoälyn siirtoa ei tulisi joutua odotella liian kauaa. 
--> jos on vaikeus tasot niin vaikeimmalla tasolla max. pari sekuntia ja helpommilla tasoilla vähemmän. (Aloitan tekemällä ns. keskivaikean tason ja lisään sitten helpon ja vaikeamman tason)
