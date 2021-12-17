from pygame.constants import *
from pygame.sprite import *
import pygame
from pygame import mixer
from asset_loader import *


# creats a gameobject class that inhertes from sprite
# sprite is a pygame module for sprite groups which are an efficent way to handle sprites(images)
class GameObject(Sprite):
    x, y, w, h, image = 0, 0, 0, 0, 0

    def __init__(self, x, y, w, h, image, layer):
        super().__init__()
        self.x, self.y, self.w, self.h, self.image = x, y, w, h, image
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = image.get_rect()
        self.rect.x, self.rect.y, self.rect.w, self.rect.h = x, y, w, h
        self._layer = layer
        self.id = ""
    
    def update(self, deltatime):
        pass

# this is the class for the background
class Background(GameObject):

    def __init__(self,x,y,w,h,image,layer):
        # uses super to get the contructers from gameobject
        super().__init__(x,y,w,h,image,layer)
        self.id = "bg"
        

    def update(self, deltatime):
        pass

# this is the class for the player
class Player(GameObject):
    def __init__(self,x,y,w,h,image,layer,shootspeed):
        # uses super to get the contructers from gameobject
        super().__init__(x,y,w,h,image,layer)
        self.movespeed = 500
        self.velo = [0,0]
        self.shootspeed = shootspeed
        self.shoottimer = 0
        self.health = 3
        self.id = "player"
        self.supershot = 0


    def update(self, deltatime):
        # this checks what key is being pressed
        keys=pygame.key.get_pressed()

        # this is all for the borders to make sure the player doesnt go out of bounds
        # borders
        if self.x > 700:
            self.x = 700
        if self.x < 0:
            self.x = 0
        if self.y > 525:
            self.y = 525
        if self.y < 400:
            self.y = 400

        # checks input and changes velocity accordingly
        if keys[K_a]:
            self.velo[0] = -1
        elif keys[K_d]:
            self.velo[0] = 1
        else:
            self.velo[0] = 0
        if keys[K_w]:
            self.velo[1] = -1
        elif keys[K_s]:
            self.velo[1] = 1
        else:
            self.velo[1] = 0

        # moves speed with velocity that is set above
        self.x += self.velo[0] * self.movespeed * deltatime
        self.y += self.velo[1] * self.movespeed * deltatime
        self.rect.x = self.x
        self.rect.y = self.y
        self.shoottimer += deltatime
    
    def takedamage(self):
        # palys a sound when the player takes damage
        pygame.mixer.Sound.play(assets["player damage"])

        # takes health away from the player
        self.health -= 1