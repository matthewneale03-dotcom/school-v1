import random
from game_objects import Player, Weapon, Enemy

# Pre-defined selection lists
players = [
    Player('Gimli', 'Dwarf', 'Fighter', 3, 180),
    Player('Legolas', 'Elf', 'Ranger', 5, 120),
    Player('Gandalf', 'Wizard', 'Mage', 8, 90),
    Player('Aragorn', 'Human', 'Paladin', 4, 150)
]

weapons = [
    Weapon('Battleaxe', 'Melee', random.randint(12, 15)),
    Weapon('Longbow', 'Ranged', random.randint(10, 14)),
    Weapon('Staff', 'Magic', random.randint(8, 16)),
    Weapon('Broadsword', 'Melee', random.randint(11, 15))
]

def select_character():
    print("=== Choose Your Character ===")
    for idx, p in enumerate(players, 1):
        print(f"{idx}. {p.name} ({p.race} {p.cls})")

    while True:
        try:
            choice = int(input("Select a character (1-4): ")) - 1
            if 0 <= choice < len(players):
                return players[choice]
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def select_weapon():
    print("\n=== Choose Your Weapon ===")
    for idx, w in enumerate(weapons, 1):
        print(f"{idx}. {w.name} [{w.category}] (Dmg: {w.damage})")

    while True:
        try:
            choice = int(input("Select a weapon (1-4): ")) - 1
            if 0 <= choice < len(weapons):
                return weapons[choice]
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Program Execution
selected_player = select_character()
selected_weapon = select_weapon()
enemy = Enemy('Orc Berserker', 'Orc', random.randint(15, 18), random.randint(80, 140))

print(f"\n--- Selection Summary ---")
print(f"Player: {selected_player.name} | Class: {selected_player.cls} | HP: {selected_player.health}")
print(f"Weapon: {selected_weapon.name} ({selected_weapon.category}) | Damage: {selected_weapon.damage}")
print(f"\n--- Enemy Encounter ---")
print(f"Enemy: {enemy.name} | HP: {enemy.health} | Damage: {enemy.damage}")