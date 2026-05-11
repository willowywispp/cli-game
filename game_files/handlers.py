import os
import time

def handle_combat(player, enemy):
    print(f"Entered Combat vs {enemy.name}")
    while enemy.hp > 0:
        print("----------------------------")
        print("Your Turn:")
        inp = input("Combat > ").lower()
        if inp == "attack":
            enemy.hp -= player.calc_damage()
            time.sleep(0.5)
            if enemy.hp <= 0:
                print(f"\nDamage Done: {player.calc_damage()}\n")
                time.sleep(1)
                print(f"{enemy.name} HP: 0")
                continue
            print(f"\nDamage Done: {player.calc_damage()}\n")
            time.sleep(1)
            print(f"{enemy.name} HP: {enemy.hp}")
        else:
            print("\nInvalid Input, Turn Skipped\n")
        print("----------------------------")
        time.sleep(2)
        print(f"{enemy.name}'s Turn:\n")
        time.sleep(1)
        print(f"{enemy.name} Attacks for {enemy.damage}HP\n")
        time.sleep(1)
        player.c_health -= enemy.damage
        print(f"You Have {player.c_health}HP left")
        time.sleep(1)
    print("Combat Finished\n")
    print("You Won!")

def handle_interaction(player, target):
    while True:
        os.system("clear")
        print(f"Interacting with {target.name}")
        print("""
    What do you want to do?
    1. Talk
    2. Gift
    3. Attack
    4. Leave
        """)
        inp = input(f"{target.name} > ").lower()
        if inp == "1" or inp == "talk":
            while True:
                os.system("clear")
                print(f"Talking to {target.name}")
                print("""
                What do you want to talk about?
                1.




                """)


