"""Moduuli, joka sisältää luokan Game"""
from doctest import ELLIPSIS_MARKER
import pygame
from gamemodules import game_logic
from gamemodules.slot import Slot
from UI.game_UI import Game_UI

# ensimmäinen pelaaja on keltainen toinen pelaaja on punainen
class Game:
    """Luokka, joka vastaa kaksinpelin toiminnasta"""
    def __init__(self):
        self.ui = Game_UI()
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.running = False
        self.red_won = False
        self.yellow_won = False
        self.tie_game = False
        self.game_over = False
        self.yellows_turn = True
        self.ai = False
        self.mouse_pos = (0,0)
    def run_game(self):
        while True:
            pygame.init()
            self.ui.game_UI_setup()
            self.running = True
            self.gameloop()
            break
    def restart_game(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.running = True
        self.red_won = False
        self.yellow_won = False
        self.tie_game = False
        self.game_over = False
        self.yellows_turn = True
    def column_full(self, x_value):
        return game_logic.column_full_check(self.board, x_value)
    def red_wins(self):
        self.red_won = True
        self.game_over = True
    def yellow_wins(self):
        self.yellow_won = True
        self.game_over = True
    def check_for_win(self):
        result = game_logic.win_check(self.board)
        if result == 1:
            self.yellow_wins()
        if result ==2:
            self.red_wins()
    def check_for_tie(self):
        if game_logic.tie_check(self.board):
            self.tie()
    def tie(self):
        self.game_over = True
        self.tie_game = True
    def left_click(self, position):
        if not self.game_over:
            (x,y) = position
            y -= 100
            y = y//100
            x = x//100
            if not self.column_full(x):
                for i in range(5,-1,-1):
                    if self.board[i][x].is_empty():
                        if self.yellows_turn:
                            self.board[i][x].mark_yellow()
                            self.yellows_turn = False
                            break
                        else:
                            self.board[i][x].mark_red()
                            self.yellows_turn = True
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.restart_game()
                if event.key == pygame.K_t:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.left_click(position)
            if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = pygame.mouse.get_pos()
    def gameloop(self):
        while self.running:
            self.check_events()
            self.ui.draw_screen(self.board, self.game_over, 
                            self.tie_game, self.yellow_won,
                            self.red_won, self.ai,
                            self.yellows_turn, self.mouse_pos)

