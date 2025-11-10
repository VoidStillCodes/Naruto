#-- Imports --#
import pygame
import os
import sys
import random
from config import ClanList, NatureList
#--------------#
#-- Player Class --#
class character(): # template for characters
    def __init__(self):
        self.name = ""
        self.clan = ""
        self.chakra_nature = []
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.stats = {
            'strength': 0,
            'agility': 0,
            'intelligence': 0,
            'endurance': 0,
            'chakra': 0,
            'Ninjutsu': 0,
            'Taijutsu': 0,
            'Genjutsu': 0
        }
        self.statPoints = 0

    def get_clan(self, ClanList):
        x = random.randint(0, len(ClanList)-1)
        self.clan = ClanList[x]
        return self.clan
    
    def get_chakra_nature(self, NatureList):
        amount = random.randint(0,5)
        print("Amount of Natures:", amount)
        for i in range(amount):
            y= True
            while y:
                x = random.randint(0, len(NatureList)-1)
                nature = NatureList[x]
                if nature not in self.chakra_nature:
                    self.chakra_nature.append(nature)
                    y = False
        return self.chakra_nature
    
    def level_up(self):
        self.level += 1
        self.statPoints += 5
        return self.level, self.statPoints
    
    def gain_exp(self, amount):
        self.exp += amount
        while self.exp >= self.exp_to_next_level:
            if self.exp >= self.exp_to_next_level:
                self.level_up()
                self.exp -= self.exp_to_next_level
                self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
        return self.exp, self.level

#-- testing --#
player = character()
        