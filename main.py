import pygame
from game import Game
from pygame.constants import *
from pygame import mixer
pygame.init()
import sys
import os

winOpen = True
game = Game(800, 600)

# Bugs
# sometimes the enemy ship gets stuck on the bottom y axis, x axis is fine

# test comment
# starts music at the begeing of the code
mixer.music.load("assets/Sounds/SkyFire (Title Screen).ogg")
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)


# Starts game loop if the window is open and stops python if the window is closed
while winOpen:
    if not game.doClose:
        game.loop()
    else:
        winOpen = False