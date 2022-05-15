"""Moduuli, joka sisältää luokan Game"""
from doctest import ELLIPSIS_MARKER
import pygame
from gamemodules import game_logic
from UI.game_UI import Game_UI

# ensimmäinen pelaaja on keltainen toinen pelaaja on punainen
class Game:
    """Luokka, joka vastaa kaksinpelin toiminnasta.
    Ensimmäinen pelaaja on aina keltainen ja toinen punainen.
    Attributes:
        ui: muutuja joka sisältää pelin käyttöliittymästä vastaavan luokan.
        board: matriisi, joka kuvaa pelilautaa. 0 - tyhjä ruutu,
                                                1 - keltainen ruutu
                                                2 - punainen 
        running: Boolean arvo, joka kertoo onko peli käynnissä vai ei.
        yellow_won: Boolean arvo, joka kertoo onko keltainen voittanut pelin.
        red_won: Boolean arvo, joka kertoo onko punainen voittanut pelin.
        tie_game: Boolean arvo, joka kertoo onko peli päättynyt tasapeliin.
        game_over: Boolean arvo, joka kertoo onko peli päättynyt.
        yellows_turn: Boolean arvo, joka kertoo onko keltaisen (1 pelaajan) vuoro.
        ai: Boolean arvo, joka keroo onko kyseessä peli tekoälyä vastaan.
            Kaksin pelissä tämä on false ja yksin pelissä true.
        mouse_pos: Tuple arvo, joka kertoo hiiren x ja y koordinaatit pikseleinä.
        title: Merkkijono arvo, joka on pelin otsikko.
        """
    def __init__(self):
        """Luokan konstruktori, jolle ei anneta argumentteja."""
        self.ui = Game_UI()
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False
        self.red_won = False
        self.yellow_won = False
        self.tie_game = False
        self.game_over = False
        self.yellows_turn = True
        self.ai = False
        self.mouse_pos = (0,0)
        self.title = "toista pelaajaa vastaan"
    def run_game(self):
        """Funktio, joka käynnistää pelin."""
        while True:
            pygame.init()
            self.ui.game_UI_setup()
            self.running = True
            self.gameloop()
            break
    def restart_game(self):
        """Funktio, joka uudelleenasettaa pelin alkuun."""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = True
        self.red_won = False
        self.yellow_won = False
        self.tie_game = False
        self.game_over = False
        self.yellows_turn = True
    def column_full(self, x):
        """Funktio, kutsuu pelilogiikan funktiota, joka kertoo onko parametrina
        annetun x-arvon mukainen sarake jo täysi. Palauttaa boolean arvon."""
        return game_logic.column_full_check(self.board, x)
    def yellow_wins(self):
        """Funktio, joka käsittelee keltaisen voiton."""
        self.yellow_won = True
        self.game_over = True
    def red_wins(self):
        """Funktio, joka käsittelee punaisen voiton."""
        self.red_won = True
        self.game_over = True
    def check_for_win(self):
        """Funktio, joka tarkistaa onko jommalle kummalle tullut voitto ja kutsuu
        sen mukaisesti tarvittaessa funktiota yellow_wins() tai red_wins()."""
        result = game_logic.win_check(self.board)
        if result == 1:
            self.yellow_wins()
        if result ==2:
            self.red_wins()
    def check_for_tie(self):
        """Funktio, joka tarkistaa onko tullut tasapeli ja kutsuu tarvittaessa
        funktiota tie()."""
        if game_logic.tie_check(self.board):
            self.tie()
    def tie(self):
        """Funktio, joka käsittelee tasapelitilanteen."""
        self.game_over = True
        self.tie_game = True
    def mouse_click(self, position):
        """Funktio, joka käsittelee hiiren klikkauksen eli pelisiirrot ja niihin tarvittavat
        metodit."""
        if not self.game_over:
            (x,y) = position
            y -= 100
            y = y//100
            x = x//100
            if not self.column_full(x):
                for i in range(5,-1,-1):
                    if self.board[i][x] == 0:
                        if self.yellows_turn:
                            self.board[i][x] = 1
                            self.yellows_turn = False
                            break
                        else:
                            self.board[i][x] = 2
                            self.yellows_turn = True
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False
    def check_events(self):
        """Funktio, joka tarkistaa oleelliset tapahtumat."""
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
                    self.mouse_click(position)
            if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = pygame.mouse.get_pos()
    def gameloop(self):
        """Pelisilmukka, joka pelin ollessa käynnissä tarkistaa vuorotellen tapahtumat
        ja piirtää näytön."""
        while self.running:
            self.check_events()
            self.ui.draw_screen(self.board, self.game_over, 
                            self.tie_game, self.yellow_won,
                            self.red_won, self.ai,
                            self.yellows_turn, self.mouse_pos)

