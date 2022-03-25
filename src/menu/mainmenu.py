import pygame

class MainMenu:
    def __init__(self):
        self.screen_height = 700
        self.screen_width = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.singleplayer_button = pygame.Rect(100, 225, 500, 150)
        self.multiplayer_button = pygame.Rect(100, 450, 500, 150)
        self.background_color = (50, 50, 50)
        self.button_color = (176, 196, 222)
        self.font = None
    def run_menu(self):
        pygame.init()
        pygame.display.set_caption("CONNECT 4")
        self.font = pygame.font.SysFont("Arial", 45, 1)
        self.menu_loop()
    def mouse_click(self, position):
        if self.singleplayer_button.collidepoint(position):
            print("Konetta vastaan")
        if self.multiplayer_button.collidepoint(position):
            print("Toista pelaajaa vastaan")
    def draw_text(self, text, x_value, y_value):
        text_area = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_area, (x_value, y_value))
    def draw_button(self, button):
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_screen(self):
        self.screen.fill(self.background_color)
        self.draw_button(self.singleplayer_button)
        self.draw_button(self.multiplayer_button)
        self.draw_text("VALITSE VASTUS:", 160, 100)
        self.draw_text("TIETOKONE", 225, 275)
        self.draw_text("TOINEN PELAAJA", 150, 500)
        pygame.display.flip()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.mouse_click(position)
    def menu_loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    
    