# Testausdokumentti
#### Codecov:
[![codecov](https://codecov.io/gh/vilkiida/tiralabra-connectfour/branch/main/graph/badge.svg?token=TVFSQDDKZ7)](https://codecov.io/gh/vilkiida/tiralabra-connectfour)

#### Mitä on testattu:
Yksikkö testejä on luokille MainMenu, Game ja sen perivälle SinglePlayerGame. Yksikkötestit testaavat myös ai (tälle omia yksikkötestejä) ja game_logic funktioita.
Käyttöliittymä luokat Menu_UI ja Game_UI on jätetty testauksen ulkopuolelle.
Myös tekoälyn siirron tekemisen nopeutta eri vaikeutasoilla testataan omalla komentokäyttöliittymän testiohjelmalla. Ohjelmalle annetaan haluttu vaikeus taso ja otoksen koko ja se luo keskiarvon ja varianssin tekoälyn siirron tekemiseen kuluvista ajoista halutulla otoksella.

#### Yksikkötesti kattavuusraportti:
![](https://github.com/vilkiida/tiralabra-connectfour/blob/main/dokumentaatio/kuvat/coverage-report.png)

Testi kattavuudessa olevat puutteet, johtuvat pitkälti siitä, että en testannut joitakin funktioita, jotka kutsuivat jotakin käyttöliittymä luokan metodia tai niissä oli pygame kirjaston komentoja (esim. en testannut MainMenu luokan tai Game luokan run_game tai run_menu funktioita, sillä niiden kutsuminen käynnistää pelin).

#### Yksikkötestien suorittaminen ja niiden kattavuus raportti:
Yksikkötestit voi suorittaa komennolla **poetry run invoke test**
Testikattavuusraportin saa luotua komennolla **poetry run invoke coverage-report**
ja sen luoma raportti löytyy sovelluksen juurihakemiston htmlcov kansion index.html tiedostosta.

#### Suorituskykytestaus:
Tekoälyn siirron teon keskimääräistä nopeutta voi testata komentorivi ohjelmalla komennolla **poetry run invoke performance**
##### Ohjelman toiminta:
- Ohjelmalle annetaan komentoriviltä tieto millä vaikeustasolla halutaan testata. **h** - helppo, **v** - vaikea tai **t** - tosi vaikea.
- Sitten ohjelma kysyy halutun otoskoon, joka annetaan lukuarvona.
- Ohjelma tulostaa tämän jälkeen otoksen aikojen keskiarvon ja varianssin.
- Ohjelma kysyy halutaanko tulostaa ajat ja syöttämällä arvon k, ne saa tulostettua.
- Ohjelma sammuu kun vaikeustasoa kysyttäessä syöttää **l**.



