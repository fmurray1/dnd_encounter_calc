class Enemy:
    """
    This is a generic class of a monster in the Monster guide, it takes a name and XP
    """
    def __init__(self, name, xp):
        self._enemy_name = name
        self._xp = xp
    
    @property
    def xp(self):
        return self._xp

    def __repl__(self):
        return "{} at {} xp".format(self._enemy_name, self._xp)


class Encounter:
    def __init__(self):
        self._total_enemies = 0
        self._list_of_enemies = [tuple]

    @property
    def total_enemies(self):
        return self._total_enemies
    
    @property
    def enemies(self):
        return self._list_of_enemies


    def add_enemies(self, count:int, enemy_class:Enemy):
        self._list_of_enemies.append((count, enemy_class))
        self._total_enemies += count
    
    def __repl__(self):
        repl_string = ''
        for c, enemy in self._list_of_enemies:
            repl_string += "{} {}".format(c, enemy)
        return repl_string

