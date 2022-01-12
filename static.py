import pygame
from pygame import sprite
from projectile import Projectile
from asset_loader import *




enemy_bullets = pygame.sprite.LayeredUpdates()

# this is to spawn the projectile
# I used this because there were circular imports and this was a good solution
def spawnprojectile(spritegroup:pygame.sprite.LayeredUpdates, projectile:Projectile):
    spritegroup.add(projectile)