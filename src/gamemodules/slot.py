import pygame
from load_image import load_image
class Slot:
    def __init__(self):
        self.empty = True
        self.yellow = False
        self.red = False
        self.image = load_image("c4_empty.png")
    def is_empty(self):
        return self.empty
    def is_red(self):
        return self.red
    def is_yellow(self):
        return self.yellow
    def mark_red(self):
        self.empty = False
        self.yellow = False
        self.red = True
        self.image = load_image("c4_red.png")
    def mark_yellow(self):
        self.empty = False
        self.red = False
        self.yellow = True
        self.image = load_image("c4_yellow.png")
    def mark_empty(self):
        self.empty = True
        self.red = False
        self.yellow = False
        self.image = load_image("c4_empty.png")