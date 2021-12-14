import pygame
from game import Game
from pygame.constants import *
from pygame import mixer
pygame.init()

winOpen = True
game = Game(800, 600)

# Bugs
# sometimes the enemy ship gets stuck on the bottom y axis, x axis is fine

mixer.music.load("assets\Sounds\SkyFire (Title Screen).ogg")
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)

while winOpen:
    if not game.doClose:
        game.loop()
    else:
        winOpen = False