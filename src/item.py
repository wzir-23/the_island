""" Helper classes and functions for game items """


class Tile():
    """ The smallest building block in a map """
    def __init__(self):
        self.tile = '.'
    def get(self):
        """ get tile """
        return self.tile
    def set(self, item):
        """ update tile """
        self.tile = item
