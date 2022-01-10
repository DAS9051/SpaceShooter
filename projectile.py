from gameobject import *
import sys
import os

# projectily class that inhertices from gameobject
class Projectile(GameObject):

    def __init__(self, x, y, w, h, image, speed, damage, velocity, lifetime):
        super().__init__(x, y, w, h, image, 2)
        self.speed = speed
        self.damage = damage
        self.velocity = velocity
        self.destroyTimer = 0
        self.lifetime = lifetime

    def update(self, deltaTime):
        # this is for the destoy timer of the projectile
        self.destroyTimer += deltaTime
        # this is for the velocity of the projectile
        self.x += self.velocity[0] * self.speed * deltaTime
        self.y += self.velocity[1] * self.speed * deltaTime

        # sets the rect(pygame varaible) to pos
        self.rect.x = self.x
        self.rect.y = self.y

        # destroys the projectile if the lifetime is met, this is to stop it from using extra memeory if it misses
        if self.destroyTimer > self.lifetime:
            self.kill()