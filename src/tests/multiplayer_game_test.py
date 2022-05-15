import unittest
from gamemodules.multiplayer_game import Game

class TestMultiplayerGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    def test_after_setup_running_is_False(self):
        self.assertEqual(False, self.game.running)
    def test_after_setup_game_is_not_over(self):
        self.assertEqual(False, self.game.game_over)
    def test_after_setup_red_has_not_won(self):
        self.assertEqual(False, self.game.red_won)
    def test_after_setup_yellow_has_not_won(self):
        self.assertEqual(False, self.game.yellow_won)
    def test_after_setuo_red_has_not_won(self):
        self.assertEqual(False, self.game.red_won)
    def test_after_setup_ai_has_correct_value(self):
        self.assertEqual(False, self.game.ai)
    def test_after_setup_all_slots_are_empty(self):
        all_empty = True
        for y in range(6):
            for x in range(7):
                if self.game.board[y][x] != 0:
                    all_empty = False
        self.assertEqual(True, all_empty)
    def test_red_wins_ends_game(self):
        self.game.red_wins()
        self.assertEqual(True, self.game.game_over)
    def test_yellow_wins_ends_game(self):
        self.game.yellow_wins()
        self.assertEqual(True, self.game.game_over)
    def test_4_horisontal_yellow_wins_game(self):
        self.game.board[2][1] = 1
        self.game.board[2][2] = 1
        self.game.board[2][3] = 1
        self.game.board[2][4] = 1
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_horisontal_red_wins_game(self):
        self.game.board[4][2] = 2
        self.game.board[4][3] = 2
        self.game.board[4][4] = 2
        self.game.board[4][5] = 2
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_horisontal_yellow_ends_game(self):
        self.game.board[3][4] = 1
        self.game.board[3][3] = 1
        self.game.board[3][2] = 1
        self.game.board[3][1] = 1
        self.game.check_for_win()
        self.assertEqual(True, self.game.game_over)
    def test_4_vertical_yellow_wins_game(self):
        self.game.board[2][3] = 1
        self.game.board[3][3] = 1
        self.game.board[4][3] = 1
        self.game.board[5][3] = 1
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_vertical_red_wins_game(self):
        self.game.board[5][5] = 2
        self.game.board[3][5] = 2
        self.game.board[4][5] = 2
        self.game.board[2][5] = 2
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_downwards_diagonal_yellow_wins_game(self):
        self.game.board[1][1] = 1
        self.game.board[2][2] = 1
        self.game.board[3][3] = 1
        self.game.board[4][4] = 1
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_downwards_diagonal_red_wins_game(self):
        self.game.board[2][1] = 2
        self.game.board[3][2] = 2
        self.game.board[4][3] = 2
        self.game.board[5][4] = 2
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_upwards_diagonal_red_wins_game(self):
        self.game.board[4][2] = 2
        self.game.board[3][3] = 2
        self.game.board[2][4] = 2
        self.game.board[1][5] = 2
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_upwards_diagonal_yellow_wins_game(self):
        self.game.board[2][5] = 1
        self.game.board[3][4] = 1
        self.game.board[4][3] = 1
        self.game.board[5][2] = 1
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_restart_game_clears_board(self):
        self.game.board = [[0,0,0,0,0,0,0], 
                           [0,0,0,0,0,0,0],
                           [0,0,0,2,0,0,0],
                           [0,0,1,2,1,1,0],
                           [0,0,1,2,1,2,0],
                           [0,2,1,1,2,2,0]]
        self.game.restart_game()
        restarted = True
        if self.game.game_over:
            restarted = False
        if self.game.red_won:
            restarted = False
        if self.game.yellow_won:
            restarted = False
        if not self.game.running:
            restarted = False
        for y in range(6):
            for x in range(7):
                if self.game.board[y][x] != 0:
                    restarted = False
        self.assertEqual(True, restarted)
    def test_game_ends_in_tie_when_board_full_and_no_win(self):
        #tasapelitilanne:
        self.game.board = [[2,2,1,2,1,1,2], 
                           [1,1,2,1,2,2,1],
                           [2,2,2,1,1,1,2],
                           [1,1,2,1,1,2,1],
                           [2,2,1,2,2,2,1],
                           [1,2,2,1,1,2,1]]
        self.game.check_for_tie()
        self.assertEqual(True, self.game.tie_game)
    
    def test_column_full_returns_correct(self):
        self.game.board = [[2,2,1,2,1,1,2], 
                           [1,1,2,1,2,2,1],
                           [2,2,2,1,1,1,2],
                           [1,1,2,1,1,2,1],
                           [2,2,1,2,2,2,1],
                           [1,2,2,1,1,2,1]]
        self.assertEqual(True, self.game.column_full(2))
    def test_mouse_click_works_on_yellow(self):
        self.game.yellows_turn = True
        self.game.mouse_click((435,250))
        self.assertEqual([[0,0,0,0,0,0,0], 
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,1,0,0]],
                               self.game.board)
    def test_mouse_click_works_changes_turn_and_works_on_red(self):
        self.game.yellows_turn = True
        self.game.mouse_click((435,250))
        self.game.mouse_click((346,577))
        self.assertEqual([[0,0,0,0,0,0,0], 
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,2,1,0,0]],
                        self.game.board)
    def test_game_stops_running_if_clicked_after_game_over(self):
        self.game.game_over = True
        self.game.mouse_click((250,456))
        self.assertEqual(False, self.game.running)
    def test_mouse_clicked_does_nothing_if_full_colum_is_clicked(self):
        self.game.board = [[0,0,2,0,0,0,0], 
                        [0,0,0,1,0,0,0],
                        [0,0,0,2,2,0,0],
                        [0,0,0,1,2,0,0],
                        [0,0,1,2,1,0,0],
                        [0,1,2,1,2,2,0]]
        self.game.yellows_turn = True
        self.game.mouse_click((225, 467))
        self.assertEqual([[0,0,2,0,0,0,0], 
                        [0,0,0,1,0,0,0],
                        [0,0,0,2,2,0,0],
                        [0,0,0,1,2,0,0],
                        [0,0,1,2,1,0,0],
                        [0,1,2,1,2,2,0]], self.game.board)
                
    


            
        
    
