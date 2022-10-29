import logging


class Game():
    def __init__(self):
        self.mem_map = []
        self.win = False
        self.creatures = False

    # gui stuff
    # ---------------------------
    def get_win(self):
        """ get gui handle """
        return self.win

    def set_win(self, win):
        """ set gui handle """
        self.win = win

    def refresh(self):
        """ refresh gui """
        self.win.refresh()

    # Memory map representation
    # ---------------------------
    def get_mem_map(self):
        """ get memory map """
        return self.mem_map

    def set_mem_map(self, mem_map):
        """ update memory map """
        self.mem_map = mem_map
        logging.debug('Game.set_mem_map')

    # Monster and character lists
    # ---------------------------
    def get_creatures(self):
        """ get list (player and) monsters """
        return self.creatures

    def set_creatures(self, creatures):
        """ update list (player and) monsters """
        self.creatures = creatures
