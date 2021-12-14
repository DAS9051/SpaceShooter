from gameobject import *
import random
from static import *

class Enemy(GameObject):

    def __init__(self, x, y, w, h, target, id, data):
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

    def update(self, deltaTime):
        self.shoottimer += deltaTime
        if self.shoottimer > self.shootspeed:
            p = Projectile(self.x+47, self.y+63, 13, 37, self.bulletimage, 500, 1, [0,1], 2)
            spawnprojectile(enemy_bullets, p)
            self.shoottimer = 0

        self.x += self.velocity[0] * self.speed * deltaTime
        self.y += self.velocity[1] * self.speed * deltaTime

        # x axis target
        if self.target[0] > self.x:
            self.velocity[0] = 1
        if self.target[0] < self.x:
            self.velocity[0] = -1
        if self.x > self.target[0] - 16 and self.x < self.target[0] + 16:
            self.target[0] = random.randint(0,675)

        # y axis target
        if self.target[1] > self.y:
            self.velocity[1] = 1
        if self.target[1] < self.y:
            self.velocity[1] = -1
        if self.y > self.target[1] - 16 and self.y < self.target[1] + 16:
            self.target[1] = random.randint(0, 385)

        # border
        if self.x > 700:
            self.x = 700
        if self.x < 0:
            self.x = 0
        if self.y > 400:
            self.y = 400
        self.rect.x = self.x
        self.rect.y = self.y
    
    def dealdamage(self):
        damage_sound = pygame.mixer.Sound("assets\Bonus\sfx_lose.ogg")
        pygame.mixer.Sound.play(damage_sound)
        self.health -= 1