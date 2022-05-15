import unittest
from gamemodules import ai
class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,1,2,1,1,0],
                      [0,0,1,2,1,2,0],
                      [0,2,1,1,2,2,0]] 
    def test_lowest_available__gives_right_y_value(self):
        self.assertEqual(1,ai.lowest_available(self.board, 3))

    def test_count_if_4_returns_0_with_wrong_input(self):
        self.assertEqual(0, ai.count_if_4([1,1,1,1,0]))
    
    def test_count_if_4_return_correct_amount_if_yellow_won(self):
        self.assertEqual(-1000, ai.count_if_4([1,1,1,1]))
    
    def test_count_if_4_return_correct_amount_if_red_won(self):
        self.assertEqual(10000, ai.count_if_4([2,2,2,2]))
    
    def test_count_if_3_returns_0_with_wrong_input(self):
        self.assertEqual(0, ai.count_if_3([1,1,1,0,0]))
    
    def test_count_if_3_returns_correct_amount_if_yellow_won(self):
        self.assertEqual(-100, ai.count_if_3([0,1,1,1]))
    
    def test_count_if_3_return_correct_amount_if_yellow_won(self):
        self.assertEqual(10, ai.count_if_3([2,2,2,0]))
    
    def test_find_best_move_wins_when_possible(self):
        self.board[2][4] = 1
        self.assertEqual((1,3), ai.find_best_move(self.board,2))
    
    def test_find_best_move_blocks_if_needed(self):
        self.board[1][3] = 1
        self.assertEqual((2,2), ai.find_best_move(self.board,2))
    
    def test_calculate_board_returns_10000_when_red_has_3_in_row(self):
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0],
                      [1,1,2,2,2,2,1]]
        self.assertEqual(10000, ai.calculate_board(self.board))
    def test_calcute_board_returns_correct_when_yellow_has_3_in_row(self):
        self.board = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,1,2,1,0,0],
                      [0,1,2,1,2,2,0]]
        self.assertEqual(-1000, ai.calculate_board(self.board))
    def test_find_best_move_works(self):
        self.board = [[0,0,0,2,0,0,0], 
                      [0,0,0,1,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,0,1,2,0,0],
                      [0,0,1,2,1,1,0],
                      [0,1,2,1,2,2,1]]
        self.assertEqual((2,4), ai.find_best_move(self.board, 5))