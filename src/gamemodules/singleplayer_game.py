import pygame
from gamemodules.slot import Slot
SLOT_SIZE = 100
SCREEN_HEIGHT = SLOT_SIZE*7
SCREEN_WIDTH = SLOT_SIZE*7
class SinglePlayerGame:
    def __init__(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = False
        self.yellow_won = False
        self.red_won = False
        self.game_over = False
        self.players_turn = True
        self.font = None
    def run_game(self):
        pygame.init()
        pygame.display.set_caption("CONNECT 4 - tietokonetta vastaan")
        self.font = pygame.font.SysFont("Arial", 45, 1)
        self.running = True
        self.gameloop()
        break
    def column_full(self, x_value):
        if not self.board[0][x_value].is_empty():
            return True
        return False
    def check_horisontal(self):
        for y in range(5,2,-1):
            for x in range(6,-1,-1):
                if self.board[y][x].is_yellow() and self.board[y-1][x].is_yellow() and self.board[y-2][x].is_yellow() and self.board[y-3][x].is_yellow():
                    self.yellow_wins()
                if self.board[y][x].is_red() and self.board[y-1][x].is_red() and self.board[y-2][x].is_red() and self.board[y-3][x].is_red():
                    self.red_wins()
    def check_vertical(self):
        for y in range(5,-1,-1):
            for x in range(6,2,-1):
                if self.board[y][x].is_yellow() and self.board[y][x-1].is_yellow() and self.board[y][x-2].is_yellow() and self.board[y][x-3].is_yellow():
                    self.yellow_wins()
                if self.board[y][x].is_red() and self.board[y][x-1].is_red() and self.board[y][x-2].is_red() and self.board[y][x-3].is_red():
                    self.red_wins()
    def check_upwards_diagonal(self):
        #viistot alhaalta ylös (vasemmalta)
        for y in range(5,2,-1):
            for x in range(3,-1,-1):
                if self.board[y][x].is_yellow() and self.board[y-1][x+1].is_yellow() and self.board[y-2][x+2].is_yellow() and self.board[y-3][x+3].is_yellow():
                    self.yellow_wins()
                if self.board[y][x].is_red() and self.board[y-1][x+1].is_red() and self.board[y-2][x+2].is_red() and self.board[y-3][x+3].is_red():
                    self.red_wins()
    def check_downwards_diagonal(self):
        # viistot ylhäältä alas (vasemmalta)
        for y in range(5,2,-1):
            for x in range(6,2,-1):
                if self.board[y][x].is_yellow() and self.board[y-1][x-1].is_yellow() and self.board[y-2][x-2].is_yellow() and self.board[y-3][x-3].is_yellow():
                    self.yellow_wins()
                if self.board[y][x].is_red() and self.board[y-1][x-1].is_red() and self.board[y-2][x-2].is_red() and self.board[y-3][x-3].is_red():
                    self.red_wins()
    def check_for_win(self):
        self.check_horisontal()
        self.check_vertical()
        self.check_upwards_diagonal()
        self.check_downwards_diagonal()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    def draw_screen(self):
        self.screen.fill((22,8,91))
        for y_value in range(6):
            for x_value in range(7):
                slot = self.board[y_value][x_value]
                self.screen.blit(slot.image, (x_value*SLOT_SIZE, y_value*SLOT_SIZE+SLOT_SIZE))
        pygame.display.flip()
    def gameloop(self):
        while self.running:
            self.check_events()
            self.draw_screen()