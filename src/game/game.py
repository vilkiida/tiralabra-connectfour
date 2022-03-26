import pygame
from game.slot import Slot
class TwoPlayerGame:
    def __init__(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.slot_size = 100
        self.screen_height = self.slot_size * 7
        self.screen_width = self.slot_size * 7
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = False
        self.yellow_wins = False
        self.red_wins = False
    
    def run_game(self):
        while True:
            pygame.init()
            pygame.display.set_caption("CONNECT 4 - toista pelaajaa vastaan")
            self.running = True
            self.gameloop()
            break
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    print(position)
    def draw_screen(self):
        self.screen.fill((22,8,91))
        for y_value in range(6):
            for x_value in range(7):
                slot = self.board[y_value][x_value]
                self.screen.blit(slot.image, (x_value*self.slot_size, y_value*self.slot_size+100))
        pygame.display.flip()
    def gameloop(self):
        while self.running:
            self.check_events()
            self.draw_screen()

