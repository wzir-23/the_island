import unittest
from src import item


class TestTileClass(unittest.TestCase):
    """ test the item/Tile class methods """
    def test_update_tile(self):
        brick = item.Tile()
        brick.set('-')
        symbol = brick.get()
        self.assertEqual(symbol, '-')
