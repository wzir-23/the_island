""" Helper functions for The Island """

import errno
import logging
import os
import random
from time import sleep
import src.maps


def random_location(mem_map):
    """ Returns y and x coordinates of a random accessible
        map position """
    found = 0
    while not found:
        x_pos = random.randrange(0, 79)
        y_pos = random.randrange(0, 23)
        if src.maps.is_accessible(y_pos, x_pos, mem_map):
            found = 1
    logging.debug("random_location: y=%d, x=%d", y_pos, x_pos)
    return (y_pos, x_pos)


def dice(combination):
    """ Returns the result of a D&D style dice roll
        Example arguments:
        3d6  - Three throws with a six-sided dice
        2d20 - Two throws with a twenty-sided dice """
    if len(combination) != 3:  # ubiquitous error control
        return 1
    result = 0
    throws, dice_type = combination.split('d')
    for _ in range(int(throws)):
        result += random.randrange(1, int(dice_type), 1)
    return result


def remove_logfile(fname):
    """ Removes old logfile """
    if len(fname):
        if os.path.exists(fname):
            os.remove(fname)
            return True
    logging.debug('Invalid call to remove logfile: %s', fname)
    return False
