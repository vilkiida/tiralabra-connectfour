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
                            self.draw_screen()
                            self.first_players_turn = False
                            self.ai_turn()
                            break
                        else:
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False