#!/usr/bin/env python3
""" A game heavily inspired by Phantasie II and rogue """

import curses
import logging
import time
import traceback
# Specific to this game
import src.maps
import src.monster
import src.log
import src.util
import src.game


def init_game(win):
    """ Initialize game  """
    src.log.setup_logging()
    game_data = src.game.Game()         # container for commonly used data
    game_data.set_win(win)
    mem_map = src.maps.init_mem_map()
    game_data.set_mem_map(mem_map)
    src.maps.load_map(1, game_data)     # Load map from disk
    creatures = src.monster.init_player(game_data)  # Add player
    game_data.set_creatures(creatures)
    return game_data


def exit_screen(win):
    """ Quit ncurses and return to terminal """
    win.keypad(0)          # Restore terminal on exit
    win.echo()
    win.nocbreak()
    win.endwin()
    traceback.print_exc()  # Print exception if any


def main(win):
    """ main function """
    curses.curs_set(0)  # Rendeds an error by flake8
    game_data = init_game(win)
    # splash_screen?
    render_all(game_data)
    still_in_game = 1
    while still_in_game:
        time.sleep(0.1)
        key = win.getch()
        logging.debug("pressed key: %d", key)
        if key == 81:     # Q quits game
            still_in_game = False
        elif key == 104:  # KEY_LEFT
            update_game('LEFT', game_data)
        elif key == 106:  # KEY_DOWN
            update_game('DOWN', game_data)
        elif key == 107:  # KEY_UP
            update_game('UP', game_data)
        elif key == 108:  # KEY_RIGHT
            update_game('RIGHT', game_data)


def update_game(key, game_data):
    win = game_data.get_win()
    creatures = game_data.get_creatures()
    player = creatures[0]
    new_ypos = player.get_ypos()
    new_xpos = player.get_xpos()
    if key == 'LEFT':
        new_xpos = new_xpos - 1
        if src.maps.is_accessible(new_ypos, new_xpos, game_data.get_mem_map()):
            player.set_xpos(new_xpos)
    if key == 'RIGHT':
        new_xpos = new_xpos + 1
        if src.maps.is_accessible(new_ypos, new_xpos, game_data.get_mem_map()):
            player.set_xpos(new_xpos)
    if key == 'DOWN':
        new_ypos = new_ypos + 1
        if src.maps.is_accessible(new_ypos, new_xpos, game_data.get_mem_map()):
            player.set_ypos(new_ypos)
    if key == 'UP':
        new_ypos = new_ypos - 1
        if src.maps.is_accessible(new_ypos, new_xpos, game_data.get_mem_map()):
            player.set_ypos(new_ypos)
    win.erase()
    render_all(game_data)


def render_all(game_data):
    src.maps.mem2map(game_data)
    src.maps.update_creatures(game_data)
    game_data.refresh()


if __name__ == '__main__':
    # The wrapper initializes curses and restores terminal on exit
    curses.wrapper(main)
