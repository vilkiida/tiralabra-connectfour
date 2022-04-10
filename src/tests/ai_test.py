import unittest
from gamemodules import ai
from gamemodules.slot import Slot


class TestAI(unittest.TestCase):
    def setUp(self):
        self.board = [[Slot() for x in range(7)] for y in range(6)]
        chart = [[0,0,0,0,0,0,0], 
                 [0,0,0,0,0,0,0],
                 [0,0,0,2,0,0,0],
                 [0,0,1,2,1,1,0],
                 [0,0,1,2,1,2,0],
                 [0,2,1,1,2,2,0]]
        for y in range(0,6):
            for x in range(0,7):
                if chart[y][x] == 1:
                    self.board[y][x].mark_yellow()
                if chart[y][x] == 2:
                    self.board[y][x].mark_red()
    def test_lowest_available_gives_right_y_value(self):
        self.assertEqual(1,ai.lowest_available(self.board, 3))

    def test_calculate_board_gives_the_correct_value(self):
        self.assertEqual(-195, ai.calculate_board(self.board))
    
    def test_calculate_board_gives_correct_value_when_AsI_has_4_in_row(self):
        #ensin keltaisen vuoro (huono siirto)
        self.board[5][6].mark_yellow()
        #punainen tekee voittavan siirron
        self.board[1][3].mark_red()
        self.assertEqual(1000, ai.calculate_board(self.board))
    
    def test_calculate_board_gives_correct_value_when_player_has_4_in_row(self):
        #keltainen tekee voittavan siirron
        self.board[2][2].mark_yellow()
        self.assertEqual(-1000, ai.calculate_board(self.board))
    
    def test_horisontal_line_check_gives_right_grade_change_value(self):
        self.assertEqual(0, ai.horisontal_line_check(self.board))
    
    def test_vertical_line_check_give_right_grade_change_value(self):
        self.assertEqual(-95, ai.vertical_line_check(self.board))

    def test_diagonal_upward_check_gives_right_grade_change_value(self):
        self.assertEqual(-95, ai.diagonal_upwards_line_check(self.board))