from typing import Tuple
import cr_classes as cr

class Enemy:
    """
    This is a generic class of a monster in the Monster guide, it takes a name and a cr level
    """
    def __init__(self, name, cr_str):
        self._enemy_name = name
        cr_base = cr.classmap.get(cr_str)
        if cr_base is not None:
            self.cr: cr.CR = cr_base()
        else:
            raise ValueError("CR value was not valid for an enemy")
    
    @property
    def xp(self):
        return self.cr.xp

    def __repl__(self):
        return "{} at {}".format(self._enemy_name, self.cr)

    def __str__(self):
        return self.__repl__()

class Encounter:
    def __init__(self, name):
        self._total_enemies = 0
        self._list_of_enemies: Tuple(int, Enemy) = []
        self.max_xp = 0
        self.name = name

    def add_enemies(self, count:int, enemy_class:Enemy):
        if enemy_class is None:
            raise ValueError("No enemy class of that type")
        self._list_of_enemies.append((count, enemy_class))
        self._total_enemies += count
    
    def __repl__(self):
        repl_string = 'Encounter {}:\n'.format(self.name)
        for c, enemy in self._list_of_enemies:
            repl_string += "\t{} {}\n".format(c, enemy)
        repl_string += 'Total/Max XP: {}'.format(self.max_xp)
        return repl_string
    
    def __str__(self):
        return self.__repl__()

    def xp_calc(self):
        total_xp = 0
        modifier = 0

        if self._total_enemies == 2:
            modifier = 1.5
        elif self._total_enemies >= 3 and self._total_enemies <= 6:
            modifier = 2
        elif self._total_enemies >= 7 and self._total_enemies <= 10:
            modifier = 2.5
        elif self._total_enemies >= 11 and self._total_enemies <= 14:
            modifier = 3
        elif self._total_enemies > 14:
            modifier = 4
        else:
            modifier = 1

        for count, enemy in self._list_of_enemies:
            total_xp += count*enemy.xp
        self.max_xp = total_xp*modifier

