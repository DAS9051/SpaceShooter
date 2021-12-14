import pygame
from pygame import sprite
from projectile import Projectile
from asset_loader import *




enemy_bullets = pygame.sprite.LayeredUpdates()

def spawnprojectile(spritegroup:pygame.sprite.LayeredUpdates, projectile:Projectile):
    spritegroup.add(projectile)