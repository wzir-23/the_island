class Tile():
    """ The smallest building block in a map """
    def __init__(self):
        self.tile = '.'
    def get(self):
        return self.tile
    def set(self, item):
        self.tile = item
