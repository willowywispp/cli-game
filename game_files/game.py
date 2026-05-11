from Player import Player
from charClass import charClass
from Weapon import Weapon
from Enemy import Enemy
import handlers
import sys

char_name = input("Enter Your Name:\n> ")

bandit = Enemy(name="Bandit", hp=15, damage=2, luck=2)
axe = Weapon(name="Axe", damage=4, scaling_stat="str", scaling_const=0.2, weight=4)
warrior = charClass(name="Warrior", start_weapon=axe, start_armor="Leather", max_health=15, str=12, dex=7, evade=2, fth=5)
player = Player(char_name, warrior)

while True:
    inp = input("> ")

    if inp == "q":
        sys.exit()

    if inp == "ls":
        player.print_stats()

    if inp == "damage":
        print(player.calc_damage())

    if inp == "combat":
        handlers.handle_combat(player, bandit)

