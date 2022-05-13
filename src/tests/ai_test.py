import unittest
from gamemodules import ai
from gamemodules.slot import Slot


class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        self.chart = [[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,2,0,0,0],
                      [0,0,1,2,1,1,0],
                      [0,0,1,2,1,2,0],
                      [0,2,1,1,2,2,0]]
        for y in range(0,6):
            for x in range(0,7):
                if self.chart[y][x] == 1:
                    self.board[y][x].mark_yellow()
                if self.chart[y][x] == 2:
                    self.board[y][x].mark_red()
    def test_lowest_available_gives_right_y_value(self):
        self.assertEqual(1,ai.lowest_available(self.board, 3))
    
    def test_lowest_available_numbered_gives_right_y_value(self):
        self.assertEqual(1,ai.lowest_available_numbered(self.chart, 3))

    def test_make_numbered_returns_correct(self):
        self.assertEqual(self.chart,ai.make_numbered(self.board))
    
    def test_check_if_4_returns_0_with_wrong_input(self):
        self.assertEqual(0, ai.check_if_4([1,1,1,1,0]))
    
    def test_count_if_3_returns_0_with_wrong_input(self):
        self.assertEqual(0, ai.count_if_3([1,1,1,0,0]))
    
    def test_count_if_2_return_0_with_wrong_input(self):
        self.assertEqual(0, ai.count_if_2([2,2,0,0,0]))
    
    def test_find_best_move_wins_when_possible(self):
        self.chart[2][4] = 1
        self.assertEqual((1,3), ai.find_best_move(self.chart))
    
    def test_find_best_move_blocks_if_needed(self):
        self.chart[1][3] = 1
        self.assertEqual((2,2), ai.find_best_move(self.chart))