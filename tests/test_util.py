import unittest
from pathlib import Path
from src import game
from src import maps
from src import monster
from src import util


class TestRandomLocation(unittest.TestCase):
    def test_upper_limits(self):
        mem_map = maps.init_mem_map()
        game_data = game.Game()
        game_data.set_mem_map(mem_map)
        maps.load_map(0, game_data)     # Load map from disk
        y_pos, x_pos = util.random_location(mem_map)
        for _ in range(1, 4):
            self.assertLessEqual(y_pos, 22)
            self.assertLessEqual(x_pos, 20)


class TestDice(unittest.TestCase):
    def SetUp(self):
        pass
    def test_3d6_upper_limit(self):
        # tested multiple times due to random number
        for _ in range(1, 4):
            self.assertLessEqual(util.dice('3d6'), 18)
    def test_3d6_lower_limit(self):
        # tested multiple times due to random number
        for _ in range(1, 4):
            self.assertGreaterEqual(util.dice('3d6'), 3)


class TestRemoveLogfile(unittest.TestCase):

    def test_empty_filename(self):
        self.assertFalse(util.remove_logfile(''))

    def test_wrong_filename(self):
        bad_fname = 'remove_testfile_2.txt'
        self.assertFalse(util.remove_logfile(bad_fname))

    def test_successful_removal(self):
        fname = 'remove_testfile_1.txt'
        Path(fname).touch()
        self.assertTrue(util.remove_logfile(fname))
