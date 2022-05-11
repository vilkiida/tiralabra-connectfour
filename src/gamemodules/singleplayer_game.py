from gamemodules.multiplayer_game import Game
from gamemodules import ai
class SinglePlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.title = "tietokonetta vastaan"
    def ai_turn(self):
        y, x = ai.find_best_move(self.board)
        self.board[y][x].mark_red()
        self.first_players_turn = True
    def draw_token(self):
        x = self.mouse_pos[0]
        x-=50
        if x < 0:
            x = 0
        if x >= 600:
            x = 600
        if self.first_players_turn:
            self.screen.blit(self.yellow_token, (x,0))
        else:
            ai_text = self.font.render("tietokone laskelmoi ...", True, (255, 0, 0))
            self.screen.blit(ai_text, (135,25))
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
                            self.draw_screen()
                            self.ai_turn()
                            break
                        else:
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False