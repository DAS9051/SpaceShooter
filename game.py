import pygame
from enemy import Enemy
from gameobject import *
from wave import *
from asset_loader import *
from time import time
import random
from pygame.constants import *
from projectile import Projectile
from static import *
from textobject import TextObject
from wave import load_waves
from pygame import mixer
import json

class Game():
    screen = pygame.display.set_mode((800, 600))
    gameState = "menu"
    doClose = False
    starttime = 0
    deltatime = 0
    pygame.display.set_caption("Space Shooter")
    icon = pygame.image.load("assets\PNG\playerShip2_red.png")
    pygame.display.set_icon(icon)
    mixer.init()
    LoadAssets()
    load_waves()
    bg = Background(0,0,256,256,assets["background_black"], 0)
    player = Player(350.5,0,99,75, assets["playerShip1_blue"], 2, 0.2)
    objects = pygame.sprite.LayeredUpdates()
    playerbullets = pygame.sprite.LayeredUpdates()
    enemys = pygame.sprite.LayeredUpdates()
    objects.add(bg)
    objects.add(player)
    nextwave = True
    wave = 0
    enemynum = 0


    for i in range(4):
        for j in range(4):
            bg2 = Background(0+(i*256),0+(j*256),256,256, assets["background_purple"], 1)
            objects.add(bg2)
    
    def spawn_waves(self):
        self.enemynum = 0
        for x in waves[self.wave].entities:
            x.target = [random.randint(0, 675), random.randint(0, 385)]
            self.enemys.add(x)
            self.enemynum += 1


    title = TextObject(assets["font_16"], (800,500), 0, True)
    title.SetValue("WELCOME TO SPACE SHOOTER!      Click SPACE to start", assets["font_16"])

    pausetitle = TextObject(assets["font_25"], (800,300), 0, True)
    pausetitle.SetValue("PAUSED", assets["font_25"])

    pause = TextObject(assets["font_25"], (800,500), 0, True)
    pause.SetValue("Click Space or ESC to continue", assets["font_25"])

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def loop(self):
        self.starttime = time()
        if self.gameState == "menu":
            self.run_menu()
        elif self.gameState == "game":
            self.run_game()
        elif self.gameState == "pause":
            self.run_pause()
        
        self.deltatime = time()-self.starttime

    def run_game(self):
        # event loop
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_ESCAPE):
                    self.gameState = "pause"
                    mixer.music.load("assets\Sounds\SkyFire (Title Screen).ogg")
                    mixer.music.set_volume(0.1)
                    mixer.music.play(loops=-1)

            if event.type == MOUSEBUTTONDOWN:
                if self.player.shoottimer > self.player.shootspeed:
                    self.playerbullets.add(Projectile((self.player.x+43), self.player.y, 13, 37, assets["Lazer"], 500, 1, [0,-1], 2))
                    self.player.shoottimer = 0
            if event.type == pygame.QUIT:
                self.doClose = True
                self.save()
                pygame.quit()
                exit(0)

        # wave
        if self.nextwave:
            self.spawn_waves()
            self.nextwave = False
            
        if self.enemynum < 1:
            self.wave += 1
            self.nextwave = True



        # delete bullets and enemy damage
        bullet_hits = pygame.sprite.groupcollide(self.playerbullets, self.enemys, False, False)
        for hits in bullet_hits:
            for collision in bullet_hits[hits]:
                collision.dealdamage() # deal damage to enemy here
                if collision.health <= 0:
                    collision.kill()
                    self.enemynum -= 1
            hits.kill() # kill the bullet
    
        enemys = pygame.sprite.groupcollide(self.enemys, self.enemys, False, False)
        for enemy in enemys:
            for collision in enemys[enemy]:
                if enemy.id != collision.id:
                    if enemy.y == 0:
                        enemy.y = random.randint(0, 385)
                    if enemy.x == 0:
                        enemy.x = random.randint(0, 800)

        enemy_bullet_hits = pygame.sprite.groupcollide(enemy_bullets, self.objects, False, False)
        for hits in enemy_bullet_hits:
            for collision in enemy_bullet_hits[hits]:
                if collision.id == "player":
                    self.player.takedamage()
                    hits.kill()

        if self.player.health < 1:
            self.save()
            pygame.quit()
            exit(0)

        # user interface        

        # health bar
        health = TextObject(assets["font_25"], (700,550), 0, False)
        health.SetValue(f"Health: {self.player.health}", assets["font_25"])

        # wave bar
        wave = TextObject(assets["font_16"], (700,500), 0, False)
        wave.SetValue(f"Wave: {self.wave+1}", assets["font_25"])

        #update
        self.objects.update(self.deltatime)
        self.enemys.update(self.deltatime)
        self.playerbullets.update(self.deltatime)
        enemy_bullets.update(self.deltatime)
        self.screen.fill(0)
        self.objects.draw(self.screen)
        self.enemys.draw(self.screen)
        self.playerbullets.draw(self.screen)
        enemy_bullets.draw(self.screen)
        self.screen.blit(health.text, health.rect)
        self.screen.blit(wave.text, wave.rect)

        pygame.display.flip()


    def run_menu(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_ESCAPE):
                    self.gameState = "game"
                    mixer.music.load("assets\Sounds\Battle in the Stars.ogg")
                    mixer.music.set_volume(0.1)
                    mixer.music.play(-1)
            if event.type == pygame.QUIT:
                self.doClose = True
                pygame.quit()
                exit(0)
        
        self.screen.fill((255,255,255))
        self.screen.blit(self.title.text, self.title.rect)
        pygame.display.flip()
    
    def run_pause(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_ESCAPE):
                    self.gameState = "game"
                    mixer.music.load("assets\Sounds\Battle in the Stars.ogg")
                    mixer.music.set_volume(0.1)
                    mixer.music.play(-1)
            if event.type == pygame.QUIT:
                self.doClose = True
                pygame.quit()
                exit(0)
        
        self.screen.fill((255,255,255))
        self.screen.blit(self.pausetitle.text, self.pausetitle.rect)
        self.screen.blit(self.pause.text, self.pause.rect)
        pygame.display.flip()
    
    def save(self):
        with open('data.json', 'r') as f:
            data = json.load(f)

        data["highscore"] = self.wave+1

        with open('data.json', 'w') as f:
            json.dump(data,f)