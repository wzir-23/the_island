import unittest
from src import monster


class TestMonsterClass(unittest.TestCase):
    """ Test monster/Creature class """

    def test_update_xy_pos(self):
        ork = monster.Creature('WAAAGH', 0, 0, 'W')
        ork.set_ypos(10)
        ork.set_xpos(20)
        y_pos = ork.get_ypos()
        x_pos = ork.get_xpos()
        self.assertEqual(y_pos, 10)
        self.assertEqual(x_pos, 20)


    def test_get_char(self):
        ork = monster.Creature('WAAAGH', 0, 0, 'W')
        monster_char = ork.get_char()
        self.assertEqual(monster_char, 'W')


    def test_set_name(self):
        ork = monster.Creature('WAAAGH', 0, 0, 'W')
        ork.set_name('Warboss')
        name = ork.get_name()
        self.assertEqual(name, 'Warboss')
