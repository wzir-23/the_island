""" Map functions for The Island """

import errno
import logging
import os
import random
from time import sleep
import src.item


def update_creatures(game_data):
    creatures = game_data.get_creatures()
    win = game_data.get_win()
    for creature in creatures:
        ypos, xpos = creature.get_pos()
        logging.debug("creature.char=%s, y=%d, x=%d" % (creature.get_char(),
                                                        ypos, xpos))
        win.addstr(ypos, xpos, creature.get_char())


def is_accessible(y, x, mem_map):
    """ returns booelan describing accessible area """
    walkable = ['.', '#', '^', 'O', 'T']
    if y > 24 or x > 79:   # Boundary check
        return False
    if mem_map[y][x].get() in walkable:
        return True
    else:
        return False


def init_mem_map():
    """ initialize memory representation of visible map to 80x25 chars """
    logging.debug("init_mem_map")
    mem_map = [[src.item.Tile() for x in range(80)] for y in range(25)]
    return mem_map


def load_map(part, game_data):
    """ Load specified map from file to memory """
    logging.debug("load_map")
    mem_map = game_data.get_mem_map()
    delimiter = "%d:island==========" % part
    with open("assets/map.txt") as f:
        matched = False
        y_pos = 0
        for line in f:
            logging.debug(line)
            if delimiter in line:
                matched = True
                logging.debug("match: %s", line.rstrip())
                continue
            if matched:
                line = line.rstrip()
                logging.debug("post: %s", line)
                column = list(line)
                logging.debug('len(column) = %d', len(column))
                logging.debug('->%s<-', column)
                for x_pos in range(len(column)):
                    logging.debug('y = %d, x = %d', y_pos, x_pos)
                    mem_map[y_pos][x_pos].set(column[x_pos])
                y_pos += 1
                if y_pos > 25:
                    matched = False
    game_data.set_mem_map(mem_map)
    f.close()


def mem2map(game_data):
    """ Copies internal map to curses window """
    logging.debug("mem2map")
    mem_map = game_data.get_mem_map()
    win = game_data.get_win()
    for y in range(25):
        for x in range(80):
            # logging.debug("%d:%d" % (x, y))
            win.addch(y, x, mem_map[y][x].get())
    win.refresh()


def splash_screen(game_data):
    """ game init splash screen """
    win = game_data.get_win()
    win.border(0)
    win.addstr(8, 29, "Welcome to The Island")
    game_data.refresh()  # needed?
    win.getch()
    sleep(1)
