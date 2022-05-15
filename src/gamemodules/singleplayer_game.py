from gamemodules.multiplayer_game import Game
from gamemodules import ai
class SinglePlayerGame(Game):
    def __init__(self, difficulty):
        super().__init__()
        self.title = "tietokonetta vastaan"
        self.difficulty = difficulty
        self.ai = True
    def ai_turn(self):
        numbered_board = ai.make_numbered(self.board)
        y, x = ai.find_best_move(numbered_board,self.difficulty)
        self.board[y][x].mark_red()
        self.yellows_turn = True
    def left_click(self, position):
        if not self.game_over:
            (x,y) = position
            y -= 100
            y = y//100
            x = x//100
            if not self.column_full(x):
                for i in range(5,-1,-1):
                    if self.board[i][x].is_empty():
                        if self.yellows_turn:
                            self.board[i][x].mark_yellow()
                            self.yellows_turn = False
                            self.ui.draw_screen(self.board,
                                                self.game_over, 
                                                self.tie_game, 
                                                self.yellow_won,
                                                self.red_won, 
                                                self.ai,
                                                self.yellows_turn, 
                                                self.mouse_pos)
                            self.ai_turn()
                            break
                        else:
                            break
            self.check_for_win()
            self.check_for_tie()
        else:
            self.running = False