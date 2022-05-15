# Testausdokumentti
#### Codecov:
[![codecov](https://codecov.io/gh/vilkiida/tiralabra-connectfour/branch/main/graph/badge.svg?token=TVFSQDDKZ7)](https://codecov.io/gh/vilkiida/tiralabra-connectfour)

#### Mitä on testattu:
Yksikkö testejä on luokille MainMenu, Game ja sen perivälle SinglePlayerGame. Yksikkötestit testaavat myös ai (tälle omia yksikkötestejä) ja game_logic funktioita.
Käyttöliittymä luokat Menu_UI ja Game_UI on jätetty testauksen ulkopuolelle.

#### Yksikkötesti kattavuusraportti:
(kuva tähän)
Testi kattavuudessa olevat puutteet, johtuvat pitkälti siitä, että en testannut joitakin funktioita, jotka kutsuivat jotakin käyttöliittymä luokan metodia tai niissä oli pygame kirjaston komentoja (esim. en testannut MainMenu luokan tai Game luokan run_game tai run_menu funktioita, sillä niiden kutsuminen käynnistää pelin).

#### Yksikkötestien suorittaminen ja niiden kattavuus raportti:
Yksikkötestit voi suorittaa komennolla **poetry run invoke test**
Testikattavuusraportin saa luotua komennolla **poetry run invoke coverage-report**
ja sen luoma raportti löytyy sovelluksen juurihakemiston htmlcov kansion index.html tiedostosta.




