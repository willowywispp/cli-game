import math

class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.max_health = char_class.max_health
        self.c_health = self.max_health
        self.weapon = char_class.start_weapon
        self.str = char_class.str
        self.dex = char_class.dex
        self.evade = char_class.evade
        self.fth = char_class.fth

    def print_stats(self):
        print(f"""
    Name: {self.name}
    Class: {self.char_class.name}
    Weapon: {self.weapon.name}
    HP: {self.c_health}/{self.max_health}
    Str: {self.str}
    Dex: {self.dex}
    Evade: {self.evade}
    Faith: {self.fth}
            """)

    def take_damage(self, n):
        self.c_health -= n

    def calc_damage(self):
        scaling = self.weapon.scaling_stat
        scaling_const = self.weapon.scaling_const
        stat_value = getattr(self, scaling)
        damage = self.weapon.damage
        final_damage = math.floor((scaling_const * stat_value) + damage)
        return final_damage
