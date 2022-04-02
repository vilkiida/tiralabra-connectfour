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
    def test_after_setup_all_slots_are_empty(self):
        all_empty = True
        for y in range(6):
            for x in range(7):
                if not self.game.board[y][x].is_empty():
                    all_empty = False
        self.assertEqual(True, all_empty)
    def test_in_setup_screen_is_correct_size(self):
        correct = True
        if self.game.screen_width != 700:
            correct = False
        if self.game.screen_height != 700:
            correct = False
        self.assertEqual(True, correct)
    def test_red_wins_ends_game(self):
        self.game.red_wins()
        self.assertEqual(True, self.game.game_over)
    def test_yellow_wins_ends_gaem(self):
        self.game.yellow_wins()
        self.assertEqual(True, self.game.game_over)
    def test_4_horisontal_yellow_wins_game(self):
        self.game.board[2][1].mark_yellow()
        self.game.board[2][2].mark_yellow()
        self.game.board[2][3].mark_yellow()
        self.game.board[2][4].mark_yellow()
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_horisontal_red_wins_game(self):
        self.game.board[4][2].mark_red()
        self.game.board[4][3].mark_red()
        self.game.board[4][4].mark_red()
        self.game.board[4][5].mark_red()
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_horisontal_yellow_ends_game(self):
        self.game.board[3][4].mark_yellow()
        self.game.board[3][3].mark_yellow()
        self.game.board[3][2].mark_yellow()
        self.game.board[3][1].mark_yellow()
        self.game.check_for_win()
        self.assertEqual(True, self.game.game_over)
    def test_4_vertical_yellow_wins_game(self):
        self.game.board[2][3].mark_yellow()
        self.game.board[3][3].mark_yellow()
        self.game.board[4][3].mark_yellow()
        self.game.board[5][3].mark_yellow()
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_vertical_red_wins_game(self):
        self.game.board[5][5].mark_red()
        self.game.board[3][5].mark_red()
        self.game.board[4][5].mark_red()
        self.game.board[2][5].mark_red()
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_downwards_diagonal_yellow_wins_game(self):
        self.game.board[1][1].mark_yellow()
        self.game.board[2][2].mark_yellow()
        self.game.board[3][3].mark_yellow()
        self.game.board[4][4].mark_yellow()
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)
    def test_4_downwards_diagonal_red_wins_game(self):
        self.game.board[2][1].mark_red()
        self.game.board[3][2].mark_red()
        self.game.board[4][3].mark_red()
        self.game.board[5][4].mark_red()
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_upwards_diagonal_red_wins_game(self):
        self.game.board[4][2].mark_red()
        self.game.board[3][3].mark_red()
        self.game.board[2][4].mark_red()
        self.game.board[1][5].mark_red()
        self.game.check_for_win()
        self.assertEqual(True, self.game.red_won)
    def test_4_upwards_diagonal_yellow_wins_game(self):
        self.game.board[2][5].mark_yellow()
        self.game.board[3][4].mark_yellow()
        self.game.board[4][3].mark_yellow()
        self.game.board[5][2].mark_yellow()
        self.game.check_for_win()
        self.assertEqual(True, self.game.yellow_won)


    
