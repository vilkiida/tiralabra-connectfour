"""Moduuli, joka sisältää luokan Game perivän luokan SinglePlayerGame."""
from gamemodules.multiplayer_game import Game
from gamemodules import ai
class SinglePlayerGame(Game):
    """Luokka, joka perii luokan Game ja vastaa peleistä tietokone vastusta vastaan.
    Attributes:
        Perii Game luokan attribuutit
        title: Merkkijono arvo, joka on pelin otsikko.
        difficulty: Lukuarvo, joka kertoo syvyyden, jota käytetään minimax algoritmissa.
        ai: Boolean, arvo joka kertoo onko pelissä mukana tekoäly. Asetetaan arvoon True."""
    def __init__(self, difficulty):
        """Luokan konstruktori, joka saa argumentiksi difficulty lukuarvon, joka
        kuvaa siis halutun vaikeus tason minimax algoritmin syvyyttä."""
        super().__init__()
        self.title = "tietokonetta vastaan"
        self.difficulty = difficulty
        self.ai = True
    def ai_turn(self):
        """Funktio, joka vastaa tietokonevastuksen pelivuorosta."""
        y, x = ai.find_best_move(self.board, self.difficulty)
        self.board[y][x] = 2
        self.yellows_turn = True
    def mouse_click(self, position):
        """Funktio, joka käsittelee hiiren klikkauksen eli pelisiirron ja
        kutsuu tarvittavia funktioita ja tekee siirrot."""
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
                            self.ui.draw_screen(self.board, self.game_over, 
                                                self.tie_game, self.yellow_won,
                                                self.red_won, self.ai,
                                                self.yellows_turn, self.mouse_pos)
                            self.ai_turn()
                            break
                        else:
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False