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
        self.assertEqual(-185, ai.calculate_board(self.board))
    
    def test_calculate_board_gives_the_correct_value_when_4_in_row(self):
        #ensin keltaisen vuoro (huono siirto)
        self.board[5][6].mark_yellow()
        #punainen tekee voittavan siirron
        self.board[1][3].mark_red()
        self.assertEqual(1000, ai.calculate_board(self.board))