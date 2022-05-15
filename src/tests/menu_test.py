import unittest
from menu.mainmenu import MainMenu
class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.menu = MainMenu()
    def test_clicked_is_correct_after_setup(self):
        self.assertEqual(False, self.menu.clicked)
    def test_mouse_click_to_singleplayer_game_button_makes_clicked_true(self):
        self.menu.mouse_click((300, 300))
        self.assertEqual(True, self.menu.clicked)
    def test_reset_menu_makes_clickes_false(self):
        self.menu.clicked = True
        self.menu.reset_menu()
        self.assertEqual(False, self.menu.clicked)