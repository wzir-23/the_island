import src.util

class Creature():
    """ A generic monster/hero class """
    def __init__(self, name, ypos, xpos, char):
        self.name = '.'
        self.ypos = ypos
        self.xpos = xpos
        self.char = char
        self.player = False
    def get_char(self):
        return self.char
    def set_ypos(self, ypos):
        self.ypos = ypos
    def set_xpos(self, xpos):
        self.xpos = xpos
    def get_ypos(self):
        return self.ypos
    def get_xpos(self):
        return self.xpos
    def get_pos(self):
        return (self.ypos, self.xpos)
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    # def move(self, x, y):
        # if not occupied mem_map[y][x]
        # continue


def init_player(game_data):
    """ Initialize creature list with player as 1st element """
    mem_map = game_data.get_mem_map()
    y_pos, x_pos = src.util.random_location(mem_map)
    win = game_data.get_win()
    player = src.monster.Creature('player', y_pos, x_pos, '@')
    creatures = []
    creatures.append(player)
    game_data.set_creatures(creatures)
    src.maps.update_creatures(game_data)
    win.refresh()
    return creatures
