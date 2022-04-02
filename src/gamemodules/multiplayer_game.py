"""Moduuli, joka sisältää luokan Game"""
import pygame
from gamemodules import game_logic
from gamemodules.slot import Slot
# ensimmäinen pelaaja on keltainen toinen pelaaja on punainen
class Game:
    """Luokka, joka vastaa kaksinpelin toiminnasta"""
    def __init__(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.slot_size = 100
        self.screen_height = self.slot_size * 7
        self.screen_width = self.slot_size * 7
        self.screen = None
        self.running = False
        self.red_won = False
        self.yellow_won = False
        self.game_over = False
        self.first_players_turn = True
        self.font = None
        self.title = "toista pelaajaa vastaan"
    def run_game(self):
        while True:
            pygame.init()
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption(f"CONNECT 4 - {self.title}")
            self.font = pygame.font.SysFont("Arial", 45, 1)
            self.running = True
            self.gameloop()
            break
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
    def check_for_draw(self):
        return game_logic.draw_check(self.board)
    def left_click(self, position):
        if not self.game_over:
            (x,y) = position
            y -= 100
            y = y//100
            x = x//100
            if not self.column_full(x):
                for i in range(5,-1,-1):
                    if self.board[i][x].is_empty():
                        if self.first_players_turn:
                            self.board[i][x].mark_yellow()
                            self.first_players_turn = False
                            break
                        else:
                            self.board[i][x].mark_red()
                            self.first_players_turn = True
                            break
            self.check_for_win()
            self.check_for_draw()
        else:
            self.running = False
    def draw_victory(self):
        if self.yellow_won:
            yellow_text = self.font.render("KELTAINEN VOITTI!", True, (255, 255, 0))
            self.screen.blit(yellow_text, (150,25))
        if self.red_won:
            red_text = self.font.render("PUNAINEN VOITTI!", True, (255, 0, 0))
            self.screen.blit(red_text, (150,25))
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.left_click(position)
    def draw_screen(self):
        self.screen.fill((22,8,91))
        for y_value in range(6):
            for x_value in range(7):
                slot = self.board[y_value][x_value]
                self.screen.blit(slot.image, (x_value*self.slot_size, y_value*self.slot_size+100))
        if self.game_over:
            self.draw_victory()
        pygame.display.flip()
    def gameloop(self):
        while self.running:
            self.check_events()
            self.draw_screen()

