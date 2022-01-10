from gameobject import *
import random
from static import *
import sys
import os

# makes enemy class that inherites from gambeobject
class Enemy(GameObject):

    # constructor that has everything enemy uses
    def __init__(self, x, y, w, h, target, id, data):

        # uses super class that gets data["image"] and data["layer from enemy ships in assetloader"]
        super().__init__(x, y, w, h, data["image"], data["layer"])
        self.target = target
        self.speed = data["speed"]
        self.velocity = [0,0]
        self.health = data["health"]
        self.id = id
        self.target_offset_y = 0
        self.target_offset_x = 0
        self.shootspeed = data["shootspeed"]
        self.shoottimer = 0
        self.bulletimage = data["bulletimage"]
        self.x = self.x
        self.y = self.y

    # this is pygames update function, it updates every frame
    def update(self, deltaTime):
        # this adds to delta time
        # delta time = real time no cpu time
        self.shoottimer += deltaTime

        # this checks to cooldown of which bullets can shoot
        if self.shoottimer > self.shootspeed:
            p = Projectile(self.x+47, self.y+63, 13, 37, self.bulletimage, 500, 1, [0,1], 2)
            spawnprojectile(enemy_bullets, p)
            self.shoottimer = 0

        # this is the speed of the enemy
        self.x += self.velocity[0] * self.speed * deltaTime
        self.y += self.velocity[1] * self.speed * deltaTime

        # x axis target
        # this makes a random x axis target that the enemy needs to go to (pathing)

        if self.target[0] > self.x:
            self.velocity[0] = 1
        if self.target[0] < self.x:
            self.velocity[0] = -1
        if self.x > self.target[0] - 16 and self.x < self.target[0] + 16:
            self.target[0] = random.randint(0,675)

        # y axis target
        # this makes a random y axis target that the enemy needs to go to (pathing)
        if self.target[1] > self.y:
            self.velocity[1] = 1
        if self.target[1] < self.y:
            self.velocity[1] = -1
        if self.y > self.target[1] - 16 and self.y < self.target[1] + 16:
            self.target[1] = random.randint(0, 385)

        # Creates border so enemy doesnt go out of range
        if self.x > 700:
            self.x = 700
        if self.x < 0:
            self.x = 0
        if self.y > 400:
            self.y = 400

        # sets the rect(pygame variable) to pos
        self.rect.x = self.x
        self.rect.y = self.y
    
    # this handles the damage that the enemy takes
    def dealdamage(self):
        
        # this plays a sound when the enemy is hit
        pygame.mixer.Sound.play(assets["damage_sound"])

        # makes the enemy lose health
        self.health -= 1