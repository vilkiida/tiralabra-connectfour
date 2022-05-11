# Käyttöohje

## Sovelluksen käyttäminen:

- Ladattuasi sovelluksen asenna riippuvuudet komennolla **poetry install**
- Peli käynnistyy komennolla **poetry run invoke start**
- Pylint raportin saa komennolla **poetry run invoke pylint**
- Testit voi ajaa komennolla **poetry run invoke test**

## Pelin pelaaminen:

- Haluamansa pelin voi aloittaa pelivalikosta klikkaamalla
- Peliä peletessa "a" - näppäimellä saa nykyisen pelin aloitettua alusta (oli se sitten kesken tai jo voitettu)
- Peliä pelatessa "t" - näppäimellä pääsee nykyisestä pelistä takaisin pelivalikkoon.

## PELIOHJE:
Pelin tavoitteena saada oman värisiä nappuloita 4 vierekkäin joko pystyyn, vaakaan tai viistosti. Pelin voittaa se, joka ensimmäisenä saa 4 vierekkäin.
Peli päättyy tasapeliin, jos ruudukko on täynnä eikä kumpikaan pelaaja ole onnistunut saamaan 4 omaa nappulaa vierekkäin. Pelinappula liikkuu hiiren mukana ja sen saa pudotettua peliruudukkoon klikkaamalla hiirtä, kun nappula on halutun sarakkeen kohdalla.
