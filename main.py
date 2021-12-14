import pygame
from game import Game

from pygame.constants import *

pygame.init()

winOpen = True
game = Game(800, 600)

# Bugs
# sometimes the enemy ship gets stuck on the bottom y axis, x axis is fine


while winOpen:
    if not game.doClose:
        game.loop()
    else:
        winOpen = False