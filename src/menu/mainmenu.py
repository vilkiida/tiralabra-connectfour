"""Moduuli, joka sisältää luokan MainMenu
"""
from turtle import pos
import pygame
from gamemodules.multiplayer_game import Game
from gamemodules.singleplayer_game import SinglePlayerGame
EASY = 2
MEDIUM = 4
VERY_HARD = 6
class MainMenu:
    """Luokka, joka vastaa valikon toiminnasta"""
    def __init__(self):
        self.screen_height = 700
        self.screen_width = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.singleplayer_button = pygame.Rect(100, 225, 500, 150)
        self.multiplayer_button = pygame.Rect(100, 450, 500, 150)
        self.background_color = (50, 50, 50)
        self.button_color = (176, 196, 222)
        self.font = None
        self.font2 = None
        self.clicked = False
        self.easy_button = pygame.Rect(50,240,150,120)
        self.medium_button = pygame.Rect(275,240,150,120)
        self.very_hard_button = pygame.Rect(500,240,150,120)
    def run_menu(self):
        pygame.init()
        pygame.display.set_caption("CONNECT 4")
        self.font = pygame.font.SysFont("Arial", 45, 1)
        self.font2 = pygame.font.SysFont("Arial", 25, 1)
        self.menu_loop()
    def mouse_click(self, position):
        if self.multiplayer_button.collidepoint(position):
            multiplayer_game = Game()
            multiplayer_game.run_game()
            self.reset_caption()
        if not self.clicked:
            if self.singleplayer_button.collidepoint(position):
                self.clicked = True
        else:
            if self.easy_button.collidepoint(position):
                singleplayer_game_easy = SinglePlayerGame(EASY)
                singleplayer_game_easy.run_game()
                self.reset_caption()
            if self.medium_button.collidepoint(position):
                singleplayer_game_medium = SinglePlayerGame(MEDIUM)
                singleplayer_game_medium.run_game()
                self.reset_caption()
            if self.very_hard_button.collidepoint(position):
                singleplayer_game_very_hard = SinglePlayerGame(VERY_HARD)
                singleplayer_game_very_hard.run_game()
                self.reset_caption()
    def draw_text(self, text, x_value, y_value, font):
        if font == 1:
            text_area = self.font.render(text, True, (255, 255, 255))
        if font == 2:
            text_area = self.font2.render(text, True, (255, 255, 255))
        self.screen.blit(text_area, (x_value, y_value))
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_screen(self):
        self.screen.fill(self.background_color)
        self.draw_button(self.multiplayer_button)
        self.draw_text("VALITSE VASTUS:", 160, 100, 1)
        self.draw_text("TOINEN PELAAJA", 150, 500, 1)
        if self.clicked:
            self.draw_button(self.easy_button)
            self.draw_text("HELPPO", 73, 285, 2)
            self.draw_button(self.medium_button)
            self.draw_text("VAIKEA", 303, 285, 2)
            self.draw_button(self.very_hard_button)
            self.draw_text("TOSI", 550, 270, 2)
            self.draw_text("VAIKEA", 530, 300, 2)
        else:
            self.draw_button(self.singleplayer_button)
            self.draw_text("TIETOKONE", 225, 275, 1)
        pygame.display.flip()
    def check_events(self):
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
    def menu_loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    def reset_menu(self):
        self.clicked = False
    def reset_caption(self):
        pygame.display.set_caption("CONNECT 4")
    
    