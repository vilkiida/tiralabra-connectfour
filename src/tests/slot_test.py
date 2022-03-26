import unittest
from gamemodules.slot import Slot

class TestSlot(unittest.TestCase):
    def setUp(self):
        self.slot = Slot()
    
    def test_after_setup_empty_is_correct(self):
        self.assertEqual(True, self.slot.is_empty())
    
    def test_after_setup_not_yellow_correct(self):
        self.assertEqual(False, self.slot.is_yellow())
    
    def test_after_setup_not_red_correct(self):
        self.assertEqual(False, self.slot.is_red())

    def test_is_empty_returns_false_after_is_marked_red(self):
        self.slot.mark_red()
        self.assertEqual(False, self.slot.is_empty())
    
    def test_is_empty_returns_false_after_is_marked_yellow(self):
        self.slot.mark_yellow()
        self.assertEqual(False, self.slot.is_empty())
    
    def test_mark_empty_works(self):
        self.slot.yellow = True
        self.slot.mark_empty()
        self.assertEqual(True, self.slot.is_empty())