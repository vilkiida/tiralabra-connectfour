from gamemodules.multiplayer_game import Game
class SinglePlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.title = "tietokonetta vastaan"
    def ai_turn(self):
        for y in range(5,-1,-1):
            for x in range(0,7):
                if self.board[y][x].is_empty():
                    self.board[y][x].mark_red()
                    self.first_players_turn=True
                    return
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
                            self.ai_turn()
                            break
                        else:
                            break
            self.check_for_win()
            self.check_for_draw()
        else:
            self.running = False