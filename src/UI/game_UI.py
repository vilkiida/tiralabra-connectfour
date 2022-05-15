"""Moduuli joka sisältää luokan Game_UI"""
import pygame
from load_image import load_image
class Game_UI:
    """Luokka, joka vastaa yksin ja moninpelin käyttöliittymästä.
    Attributes:
        slot_size: Lukuarvo, joka kertoo pelilaudan ruudun koon pikseleinä.
        screen_height: Lukuarvo, joka kertoo ikkunan korkeuden pikseleinä.
        screen_width: Lukuarvo, joka kertoo ikkunan leveyden pikseleinä.
        screen: Muuttuja, johon on tallennettuna peli ikkuna.
        font: Muuttuja, johon tallennetaan fontti. Saa arvon game_UI_setup funktiossa
              ja on sitä ennen None.
        red_token: Muuttuja, johon on tallennettuna kuva punaisesta pelinappulasta.
        yellow_token: Muuttuja, johon on tallennettuna kuva keltaisesta pelinappulasta.
    """
    def __init__(self):
        """Luokan konstruktori, jolle ei anneta argumentteja."""
        self.slot_size = 100
        self.screen_height = self.slot_size * 7
        self.screen_width = self.slot_size * 7
        self.screen = None
        self.red_token = load_image("c4_red_piece.png")
        self.yellow_token = load_image("c4_yellow_piece.png")
        self.yellow_in_slot = load_image("c4_yellow.png")
        self.red_in_slot = load_image("c4_red.png")
        self.empty_slot = load_image("c4_empty.png")
    def game_UI_setup(self, title):
        """Funktio, joka tekee tarvittavat alkutoimenpiteet käyttöliittymään liittyen.
        Se lisää ikkunalle otsikon ja määrittää fontit."""
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(f"CONNECT 4 - {title}")
        self.font = pygame.font.SysFont("Arial", 45, 1)
    def draw_victory(self, yellow_won, red_won):
        """Funktio, joka piirtää ruudulle tekstin, joka kertoo voittajan. Funktio saa argumenteiksi
        yellow_won ja red_won, jotka kertovat onko keltainen vai punainen voittanut."""
        if yellow_won:
            yellow_text = self.font.render("KELTAINEN VOITTI!", True, (255, 255, 0))
            self.screen.blit(yellow_text, (150,25))
        if red_won:
            red_text = self.font.render("PUNAINEN VOITTI!", True, (255, 0, 0))
            self.screen.blit(red_text, (150,25))
    def draw_tie(self):
        """Funktio, joka piirtää ruudulle tekstin, joka kertoo että peli päättyi tasapeliin."""
        tie_text = self.font.render("TASAPELI", True, (255,255,255))
        self.screen.blit(tie_text, (250,25))
    def draw_token(self, ai, yellows_turn, mouse_pos):
        """Funktio, joka piirtää pelinappulan hiiren kohdalle. Nappulan väri riippuu siitä kumman vuoro.
        Jos pelataan tietokonetta vastaan, piirretään nappulan sijasta punainen teksti, joka kertoo tietokoneen
        miettivän siirtoaan."""
        x = mouse_pos[0]
        x-=50
        if x < 0:
            x = 0
        if x >= 600:
            x = 600
        if yellows_turn:
            self.screen.blit(self.yellow_token, (x,0))
        else:
            if ai:
                ai_text = self.font.render("tietokone laskelmoi ...", True, (255, 0, 0))
                self.screen.blit(ai_text, (135,25))
            else:
                self.screen.blit(self.red_token, (x,0))
    def pick_image(self, slot):
        """Funktio, joka valitsee oikean kuvan oikealle ruudukon arvolle."""
        if slot == 0:
            return self.empty_slot
        if slot == 1:
            return self.yellow_in_slot
        if slot == 2:
            return self.red_in_slot
    def draw_screen(self, board, game_over, tie_game, yellow_won,
                    red_won, ai, yellows_turn, mouse_pos):
        """Funktio piirtää näytön. Se saa argumeinteikseen pelilaudan ja tiedot siitä onko
        peli päättynyt, tasapeli, keltainen voittanut, punainen voittanut, 
        onko kyseessä tekoälyä vastaan oleva peli, onko keltaisen vuoro ja mitkä ovat hiiren koordinaatit."""
        self.screen.fill((22,8,91))
        for y_value in range(6):
            for x_value in range(7):
                image = self.pick_image(board[y_value][x_value])
                self.screen.blit(image, (x_value*self.slot_size, y_value*self.slot_size+100))
        if game_over:
            if not tie_game:
                self.draw_victory(yellow_won, red_won)
            else:
                self.draw_tie()
        if not game_over:
            self.draw_token(ai, yellows_turn, mouse_pos)
            pygame.display.update()
        pygame.display.flip()
    
    

    