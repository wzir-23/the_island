import unittest
from src import game


class TestGameClass(unittest.TestCase):
    """ Test Game class """

    def test_gui_stuff(self):
        """ test setting and retrieving curses handle """
        # Don't know how to test using real curses
        # handler. Using string instead
        test_data = game.Game()
        self.assertFalse(test_data.get_win())
        test_data.set_win('foo')
        self.assertEqual(test_data.get_win(), 'foo')

    def test_mem_map(self):
        """ test set/get memory map """
        # Test uses simple list instead of a mem_map
        # of Tile objects
        test_data = game.Game()
        self.assertEqual(test_data.get_mem_map(), [])
        test_list = [1, 2]
        test_data.set_mem_map(test_list)
        self.assertEqual(test_data.get_mem_map(), test_list)

    def test_creature_methods(self):
        """ test updating creature list """
        # Test uses simple list instead of a list
        # of Creature objects
        test_data = game.Game()
        test_list = [1, 2]
        test_data.set_creatures(test_list)
        self.assertEqual(test_data.get_creatures(), test_list)
