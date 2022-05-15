"""Moduuli, joka sisältää luotan Menu_UI"""
import pygame
class Menu_UI:
    """Luokka, joka huolehtii valikon käyttöliittymästä
    Attributes:
        screen_height: Lukuarvo, joka kertoo näytön korkeuden pikseleinä.
        screen_width: Lukuarvo, joka kertoo näytön leveyden pikseleinä.
        screen: muuttuja, johon on tallennettuna pelin ikkuna.
        singleplayer_button: Pygamen Rect olio, joka kuvaa tietokonetta vastaan painiketta.
        multiplayer_button: Pygamen Rect olio, joka kuvaa toista pelaajaa vastaan painiketta.
        easy_bytton: Pygamen Rect olio, joka kuvaa vaikeustason "helppo" painiketta.
        hard_button: Pygamen Rect olio, joka kuvaa vaikeustason "vaikea" painiketta.
        very_hard_button: Pygamen Rect olio, joka kuvaa vaikeustason "tosi vaikea" painiketta.
        background_color: Tuple, joka kuvaa taustaväriä värikoodia.
        button_color: Tuple, joka kuvaa painikkeiden väriä värikoodina."""
    def __init__(self):
        self.screen_height = 700
        self.screen_width = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.singleplayer_button = pygame.Rect(100, 225, 500, 150)
        self.multiplayer_button = pygame.Rect(100, 450, 500, 150)
        self.easy_button = pygame.Rect(50,240,150,120)
        self.hard_button = pygame.Rect(275,240,150,120)
        self.very_hard_button = pygame.Rect(500,240,150,120)
        self.background_color = (50, 50, 50)
        self.button_color = (176, 196, 222)
    def setup(self):
        """Funktio, joka tekee tarvittavat alkutoimenpiteet käyttöliittymän kannalta.
        Se merkitsee ikkunan otsikon ja määrittää fontit."""
        pygame.display.set_caption("CONNECT 4")
        self.font = pygame.font.SysFont("Arial", 45, 1)
        self.font2 = pygame.font.SysFont("Arial", 25, 1)
    def reset_caption(self):
        """Funktio, joka uudelleen asettaa ikkunan otsikon."""
        pygame.display.set_caption("CONNECT 4")
    def draw_text(self, text, x_value, y_value, font):
        """Funktio, jolla piirretään tekstiä"""
        if font == 1:
            text_area = self.font.render(text, True, (255, 255, 255))
        if font == 2:
            text_area = self.font2.render(text, True, (255, 255, 255))
        self.screen.blit(text_area, (x_value, y_value))
    def draw_button(self, button):
        """Funktio, jolla piirretään painikkeet."""
        pygame.draw.rect(self.screen, self.button_color, button)
    def draw_screen_if_clicked(self):
        """Funktio, joka piirtää näytön, kun vaikeustasot on klikattu näkyviin."""
        self.screen.fill(self.background_color)
        self.draw_text("VALITSE VASTUS:", 160, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("TOINEN PELAAJA", 150, 500, 1)
        self.draw_levels()
        pygame.display.flip()
    def draw_screen_not_clicked(self):
        """Funktio, joka piirtää näytön, kun vaikeustasot ei ole klikattu näkyviin."""
        self.screen.fill(self.background_color)
        self.draw_text("VALITSE VASTUS:", 160, 100, 1)
        self.draw_button(self.multiplayer_button)
        self.draw_text("TOINEN PELAAJA", 150, 500, 1)
        self.draw_button(self.singleplayer_button)
        self.draw_text("TIETOKONE", 225, 275, 1)
        pygame.display.flip()
    def draw_levels(self):
        """Funktio, joka piirtää vaikeustasojen painikkeet ja niiden tekstit."""
        self.draw_button(self.easy_button)
        self.draw_text("HELPPO", 73, 285, 2)
        self.draw_button(self.hard_button)
        self.draw_text("VAIKEA", 303, 285, 2)
        self.draw_button(self.very_hard_button)
        self.draw_text("TOSI", 550, 270, 2)
        self.draw_text("VAIKEA", 530, 300, 2)
        