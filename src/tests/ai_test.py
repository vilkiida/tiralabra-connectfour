# import unittest
# from gamemodules import ai
# from gamemodules.slot import Slot


# class TestAI(unittest.TestCase):
#     def setUp(self):
#         self.board = [[Slot() for x in range(7)] for y in range(6)]
#         chart = [[0,0,0,0,0,0,0], 
#                  [0,0,0,0,0,0,0],
#                  [0,0,0,2,0,0,0],
#                  [0,0,1,2,1,1,0],
#                  [0,0,1,2,1,2,0],
#                  [0,2,1,1,2,2,0]]
#         for y in range(0,6):
#             for x in range(0,7):
#                 if chart[y][x] == 1:
#                     self.board[y][x].mark_yellow()
#                 if chart[y][x] == 2:
#                     self.board[y][x].mark_red()
#     def test_lowest_available_gives_right_y_value(self):
#         self.assertEqual(1,ai.lowest_available(self.board, 3))

#     def test_calculate_board_gives_the_correct_value(self):
#         self.assertEqual(-195, ai.calculate_board(self.board))
    
#     def test_horisontal_line_check_gives_right_grade_change_value(self):
#         self.assertEqual(0, ai.horisontal_line_check(self.board))
    
#     def test_vertical_line_check_give_right_grade_change_value(self):
#         self.assertEqual(-95, ai.vertical_line_check(self.board))

#     def test_diagonal_upward_check_gives_right_grade_change_value(self):
#         self.assertEqual(-95, ai.diagonal_upwards_line_check(self.board))
    
#     def test_find_best_move_makes_win_if_possible(self):
#         #keltaisen huono siirto
#         self.board[5][6].mark_yellow()
#         self.assertEqual((1,3),ai.find_best_move(self.board))
    
#     def test_find_best_moves_blocks_other_players_win(self):
#         #vastustaja blokkaa AI:n voiton
#         self.board[1][3].mark_yellow()
#         #blokkaako nyt AI pelaajan voiton?
#         self.assertEqual((2,2), ai.find_best_move(self.board))
    