#-- imports --#
import pygame
import os
import sys
from Sprites import character
from config import *

#-- GAME CLASS --#
class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("Naruto RPG")
        self.clock = pygame.time.Clock()
    
    def new(self):
        pass
    
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pass 
    def update(self):
        pass 
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    
    def intro(self):
        pass
    
    def draw(self):
        self.screen.fill((96, 96, 96))
        pygame.display.flip()
        
#-- create game instance --#
g = Game(screen)
while True:
    g.new()
    g.run()