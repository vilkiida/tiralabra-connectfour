"""Moduuli, joka sisältää luokan MainMenu
"""
from turtle import pos
import pygame
from gamemodules.multiplayer_game import Game
from gamemodules.singleplayer_game import SinglePlayerGame
from UI.menu_UI import Menu_UI
EASY = 3
HARD = 5
VERY_HARD = 6
class MainMenu:
    """Luokka, joka vastaa valikon toiminnasta
    Attributes:
        ui: Luokka-olio, joka vastaa menun käyttöliittymästä.
        clicked: Boolean arvo, joka kertoo onko valikosta klikattu "tietokonetta
        vastaan" painiketta, jolloin esillä vaikeustasot.
    """
    def __init__(self):
        """Luokan konstruktori, jolle ei anneta argumentteja."""
        self.ui = Menu_UI()
        self.clicked = False
    def run_menu(self):
        """ Funktio, joka käynnistää pelivalikon."""
        pygame.init()
        self.ui.setup()
        self.menu_loop()
    def mouse_click(self, position):
        """Funktio, joka käsittelee hiiren klikkauksesta aiheutuvat tapahtumat."""
        if self.ui.multiplayer_button.collidepoint(position):
            multiplayer_game = Game()
            multiplayer_game.run_game()
            self.ui.reset_caption()
        if not self.clicked:
            if self.ui.singleplayer_button.collidepoint(position):
                self.clicked = True
        else:
            if self.ui.easy_button.collidepoint(position):
                singleplayer_game_easy = SinglePlayerGame(EASY)
                singleplayer_game_easy.run_game()
                self.ui.reset_caption()
            if self.ui.hard_button.collidepoint(position):
                singleplayer_game_hard = SinglePlayerGame(HARD)
                singleplayer_game_hard.run_game()
                self.ui.reset_caption()
            if self.ui.very_hard_button.collidepoint(position):
                singleplayer_game_very_hard = SinglePlayerGame(VERY_HARD)
                singleplayer_game_very_hard.run_game()
                self.ui.reset_caption()
    def check_events(self):
        """Funktio, joka tarkistaa tapahtumat."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.mouse_click(position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    self.reset_menu()
    def draw_screen(self):
        """Funktio joka piirtää näytön sen mukaan onko vaikeustasot klikattu vai ei."""
        if self.clicked:
            self.ui.draw_screen_if_clicked()
        else:
            self.ui.draw_screen_not_clicked()
    def menu_loop(self):
        """Tarkistaa silmukassa vuorotellen tapahtumat ja piirtää näytön niiden mukaisesti, kunnes ohjelma sammutetaan."""
        while True:
            self.check_events()
            self.draw_screen()
    def reset_menu(self):
        """Palauttaa menun alkuperäiseen muotoon ja piilottaa vaikeustasot osion."""
        self.clicked = False
