import os
import pygame
DIRNAME = os.path.dirname(__file__)
def load_image(filename):
    return pygame.image.load(os.path.join(DIRNAME, "assets", filename))