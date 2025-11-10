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
        self.running = True   # Controls the outer game loop

    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)  # prevent 100% CPU usage

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False  # Also stop outer loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False

    def intro(self):
        pass

    def draw(self):
        self.screen.fill((96, 96, 96))
        pygame.display.flip()

#-- create game instance --#
g = Game(screen)

while g.running:  # Use flag instead of while True
    g.new()
    g.run()

pygame.quit()
sys.exit()