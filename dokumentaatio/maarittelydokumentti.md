# Määrittelydokumentti

#### Kieli: 
Suomi

#### Lyhyesti:
Kyseessä on siis Connect four -peli , jossa vastapuolet laittavat vuorotellen omanvärisensä nappulan 7x6 mittaisen pelilaudan ruutuihin (nappulat putoavat 
aina alimpaan mahdolliseen ruutuun valitulla rivillä). Ensimmäinen, joka saa neljä omaa nappulaansa peräkkäin, joko pystyy, vaakaan tai viistoon voittaa. Peliä voi pelata tekoälyä vastaan. 

#### Lisää:
- Pelaaja voi pelata tietokonetta vastaan.
- Pelaaja voi pelata myös toista pelaajaa vastaan

#### Opinto-ohjelmani:
Tietojenkäsittelytiede

#### Ohjelmointikieli:
Python 
(Hallitsen kunnolla käytännössä vain pyhtonia, mutta jos esimerkiksi koodikatselmuksessa ei ole tarjolla toista pythonilla tehtyä projektia, voin myös yrittää
arvioida, jotakin pythonia läheisesti muistuttavalla kielellä tehtyä projektia.)

#### Käytettävät algoritmit:
Tarkoituksena on luoda tekoäly vastustaja , jotta peliä voi pelata myös ilman toista oikeaa pelaajaa. Tämä tekoäly luodaan käyttäen minimax algoritmia, jota sitten pyritään tehostamaan alpha-beeta karsinnalla eli jättämällä binääri puun turhia haaroja läpikäymättä.
