"""Moduuli, joka sisältää Slot luokan
"""
import pygame
from load_image import load_image
class Slot:
    """ Luokka, joka kuvaa yksittäistä pelinappulan koloa pelilaudassa
    
    Attributes:
        empty: Boolean-arvo, joka kertoo onko kyseinen pelilaudan kolo tyhjä
        yellow: Boolean-arvo, joka kertoo onko kyseisessä pelilaudan kolossa keltainen pelimerkki
        red: Boolean-arvo, joka kertoo onko kyseisessä pelilaudan kolossa punainen pelimerkki
        image: Slot olion png-muotoinen kuva
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden pelilaudan ruudun. Konstruktorille ei anneta argumentteja
        """
        self.empty = True
        self.yellow = False
        self.red = False
        self.image = load_image("c4_empty.png")
    def is_empty(self):
        """Funkio, joka palauttaa arvon True, jos kyseinen pelilaudan kolo on tyhjä.
        """
        return self.empty
    def is_red(self):
        """Funktio, joka palauttaa arvon True, jos kyseisessä pelilaudan kolossa on punainen pelimerkki.
        """
        return self.red
    def is_yellow(self):
        """Funktio, joka palauttaa arvon True, jos kyseisessä pelilaudan kolossa on keltainen pelimerkki.
        """
        return self.yellow
    def mark_red(self):
        """Funktio, joka asettaa punaisen pelimerkin kyseiseen ruutuun
        """
        self.empty = False
        self.yellow = False
        self.red = True
        self.image = load_image("c4_red.png")
    def mark_yellow(self):
        """Funktio, joka asettaa keltaisen pelimerkin kyseiseen ruutuun
        """
        self.empty = False
        self.red = False
        self.yellow = True
        self.image = load_image("c4_yellow.png")
    def mark_empty(self):
        """Funktio, joka poistaa pelimerkit ruudusta
        """
        self.empty = True
        self.red = False
        self.yellow = False
        self.image = load_image("c4_empty.png")