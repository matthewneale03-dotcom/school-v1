import random

class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name
        self.race = race
        self.cls = cls
        self.atk = atk
        self.health = health

class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

class Enemy:
    def __init__(self, name, race, damage, health):
        self.name = name
        self.race = race
        self.damage = damage
        self.health = health