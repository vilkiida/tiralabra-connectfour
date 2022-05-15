import unittest
from gamemodules.singleplayer_game import SinglePlayerGame
EASY = 3
HARD = 5
VERY_HARD = 6
class TestSingleplayerGame(unittest.TestCase):
    def setUp(self):
        self.game = SinglePlayerGame(EASY)
    def test_right_title_after_setup(self):
        self.assertEqual("tietokonetta vastaan", self.game.title)
    def test_ai_variable_correct_after_setup(self):
        self.assertEqual(True, self.game.ai)
    def test_difficulty_variable_is_setup_correct(self):
        self.assertEqual(EASY, self.game.difficulty)
    def test_ai_turn_does_wins_if_possible(self):
        self.game.board = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,1,2,1,0],
                            [0,0,0,1,2,1,0]]
        self.game.ai_turn()
        self.assertEqual([[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,0,2,0,0],
                            [0,0,0,1,2,1,0],
                            [0,0,0,1,2,1,0]], self.game.board)
    def test_ai_turn_blocks_if_possible(self):
        self.game.board = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,1,0,0],
                            [0,0,0,0,2,1,0],
                            [0,0,0,2,2,1,0],
                            [0,0,0,1,2,1,0]]
        self.game.ai_turn()
        self.assertEqual([[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,1,2,0],
                            [0,0,0,0,2,1,0],
                            [0,0,0,2,2,1,0],
                            [0,0,0,1,2,1,0]], self.game.board)