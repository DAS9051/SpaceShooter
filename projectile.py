from gameobject import *


class Projectile(GameObject):

    def __init__(self, x, y, w, h, image, speed, damage, velocity, lifetime):
        super().__init__(x, y, w, h, image, 2)
        self.speed = speed
        self.damage = damage
        self.velocity = velocity
        self.destroyTimer = 0
        self.lifetime = lifetime

    def update(self, deltaTime):
        self.destroyTimer += deltaTime
        self.x += self.velocity[0] * self.speed * deltaTime
        self.y += self.velocity[1] * self.speed * deltaTime
        self.rect.x = self.x
        self.rect.y = self.y
        if self.destroyTimer > self.lifetime:
            self.kill()