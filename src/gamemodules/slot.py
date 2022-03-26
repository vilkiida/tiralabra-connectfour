import pygame
from load_image import load_image
class Slot:
    def __init__(self):
        self.__empty = True
        self.__yellow = False
        self.__red = False
        self.image = load_image("c4_empty.png")
    def is_empty(self):
        return self.__empty
    def is_red(self):
        return self.__red
    def is_yellow(self):
        return self.__yellow
    def mark_red(self):
        self.__empty = False
        self.__yellow = False
        self.__red = True
        self.image = load_image("c4_red.png")
    def mark_yellow(self):
        self.__empty = False
        self.__red = False
        self.__yellow = True
        self.image = load_image("c4_yellow.png")
    def mark_empty(self):
        self.__empty = True
        self.__red = False
        self.__yellow = False
        self.image = load_image("c4_empty.png")