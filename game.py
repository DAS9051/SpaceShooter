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

class Game():
    # sets resolution of screen
    screen = pygame.display.set_mode((800, 600))

    # makes the game start in the main menu
    gameState = "menu"

    # this boolean is responsible for if the game should close in main.py
    doClose = False

    # these 2 lines are responsible for making the variables for the deltatime
    starttime = 0
    deltatime = 0

    # sets a caption on the window
    pygame.display.set_caption("Space Shooter")

    # these 2 lines of code are resonsible for the icon of the window
    icon = pygame.image.load("assets/PNG/playerShip2_red.png")
    pygame.display.set_icon(icon)

    # this initializes the mixer in pygame
    mixer.init()

    # this calls the LoadAssets Function from asset_loader
    LoadAssets()

    # this loads all the waves from wave.py
    load_waves()

    # this creates the background
    bg = Background(0,0,256,256,assets["background_black"], 0)

    # this creates the object player
    player = Player(350.5,0,99,75, assets["playerShip1_blue"], 2, 0.2)

    # this adds the bg and the player to the layer
    objects = pygame.sprite.LayeredUpdates()

    # creates a layer for the players bullets
    playerbullets = pygame.sprite.LayeredUpdates()

    # makes an enemy layer
    enemys = pygame.sprite.LayeredUpdates()
    
    # adds bg and player to the layer
    objects.add(bg)
    objects.add(player)

    # sets next wave to True so it will start on wave 1
    nextwave = True

    # sets the wave to 0
    wave = 0

    # sets the enemy num to 0
    # enemy num is what determines if you have killed everything in the wave. 0 means no more enemys which will start the next wave
    enemynum = 0

    # makes next shot a super shop
    nextsuper = False


    # this loops the background so it will fill the whole screen. I need to do this because the background is smaller then the resoultion
    # of the scren
    for i in range(4):
        for j in range(4):
            bg2 = Background(0+(i*256),0+(j*256),256,256, assets["background_purple"], 1)
            objects.add(bg2)
    
    # this function spawns in all the enemys in the wave
    def spawn_waves(self):
        # sets enemy num to 0
        self.enemynum = 0

        # this for loop goes through each enemy in wavess
        for x in waves[self.wave].entities:
            # this creates the first target for the enemy
            # more target settings can be found in enemy.py
            x.target = [random.randint(0, 675), random.randint(0, 385)]

            # this adds all the enemys to the enemys layer so we can easily spawn them in later
            self.enemys.add(x)

            # this increases the enemy num so we can keep track of all the enemys
            self.enemynum += 1



    # this is making the text for the title
    title = TextObject(assets["font_16"], (800,500), 0, True)
    title.SetValue("WELCOME TO SPACE SHOOTER!      Click SPACE to start", assets["font_16"])

    # this is making the text for the pause screen title
    pausetitle = TextObject(assets["font_25"], (800,300), 0, True)
    pausetitle.SetValue("PAUSED", assets["font_25"])

    # this is making the text for the pause screen 
    pause = TextObject(assets["font_25"], (800,500), 0, True)
    pause.SetValue("Click Space or ESC to continue", assets["font_25"])

    # this is making the text for the Death Screen
    death = TextObject(assets["font_25"], (800,500), 0, True)
    death.SetValue("You Have lost", assets["font_25"])

    # this is making the text for the play again Screen
    again = TextObject(assets["font_16"], (800,600), 0, True)
    again.SetValue("Click SPACE to play again or click exit to leave", assets["font_16"])



    # this just sets the screen to self.screen
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    # this is the main loop for my game
    def loop(self):
        # this is for the start time it is how we can calculate the deltatime
        self.starttime = time()

        # this if statment is for determining what scene we are in, in the game
        if self.gameState == "menu":
            self.run_menu()
        elif self.gameState == "game":
            self.run_game()
        elif self.gameState == "pause":
            self.run_pause()
        elif self.gameState == "gameover":
            self.run_gameover()
        
        # this is how we find deltatime
        self.deltatime = time()-self.starttime

    # this is the game loop
    def run_game(self):
        # event loop

        # this checks key board inputs
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # checks if you click the space bar or ESC
                if (event.key == K_SPACE or event.key == K_ESCAPE):
                    # puts the game on pause and puts the pause music on
                    self.gameState = "pause"
                    mixer.music.load("assets/Sounds/SkyFire (Title Screen).ogg")
                    mixer.music.set_volume(0.1)
                    mixer.music.play(loops=-1)
                if event.key == K_1:
                    self.nextsuper = True

            # checks if the player clicks
            if event.type == MOUSEBUTTONDOWN:
                # this shoots a bullet if the player clcks

                # this makes sure you dont spam
                if self.player.shoottimer > self.player.shootspeed:
                    # spawns the player bullet
                    self.playerbullets.add(Projectile((self.player.x+43), self.player.y, 13, 37, assets["Lazer"], 500, 1, [0,-1], 2))
                    # puts the shoot timer back to zero
                    self.player.shoottimer = 0

            
            # closes teh game if you click the x at the top right
            if event.type == pygame.QUIT:
                self.doClose = True
                pygame.quit()
                exit(0)

        # this checks if we should start the next wave and if so it does
        if self.nextwave:
            self.spawn_waves()
            # sets nextwave to false so it needs to be turned on again
            self.nextwave = False
            
        # checks if next wave should be equal to true by checking the enemy num
        if self.enemynum < 1:
            self.wave += 1
            luck = random.randint(1,100)
            if luck < 20:
                self.player.supershot += 1
            self.nextwave = True



        # bullet collision

        # this makes an array with every bullet that hit an enemy
        bullet_hits = pygame.sprite.groupcollide(self.playerbullets, self.enemys, False, False)

        # for loop that goes through each bullet and sees if it has hit an enemy
        for hits in bullet_hits:
            for collision in bullet_hits[hits]:
                # this method deals damage to the enemy it is located in enemy.py
                collision.dealdamage() # deal damage to enemy here

                # if the health of the enemy is zero it will kill the enemy
                if collision.health <= 0 or self.nextsuper:
                    collision.kill()
                    luck = random.randint(1,100)
                    if luck < 25:
                        self.player.health += 1
                    if self.nextsuper:
                        self.nextsuper = False
                    # it will also lower the number of enemys by 1
                    self.enemynum -= 1
            # this line of code makes sure the bullet dies
            hits.kill() # kill the bullet


        # this code determins where the enemys spawn

        enemys = pygame.sprite.groupcollide(self.enemys, self.enemys, False, False)
        for enemy in enemys:
            # this checks the collision of the enemy
            for collision in enemys[enemy]:
                if enemy.id != collision.id:
                    # if the enemys x,y is zero(default) it will change them
                    if enemy.y == 0:
                        enemy.y = random.randint(0, 385)
                    if enemy.x == 0:
                        enemy.x = random.randint(0, 800)

        # this makes an array with every bullet that hit a player
        enemy_bullet_hits = pygame.sprite.groupcollide(enemy_bullets, self.objects, False, False)
        
        # for loop that goes through each bullet and sees if it has hit a player
        for hits in enemy_bullet_hits:
            for collision in enemy_bullet_hits[hits]:
                if collision.id == "player":
                    # this metod makes the player take damage, the method is located in gameobject.py
                    self.player.takedamage()
                    hits.kill()

        if self.player.health < 1:
            pygame.mixer.Sound.play(assets["player damage"])
            self.gameState = "gameover"

        # user interface        

        # health bar
        health = TextObject(assets["font_25"], (700,550), 0, False)
        health.SetValue(f"Health: {self.player.health}", assets["font_25"])

        # wave bar
        wave = TextObject(assets["font_25"], (700,500), 0, False)
        wave.SetValue(f"Wave: {self.wave+1}", assets["font_25"])

        # power ups
        supershot = TextObject(assets["font_25"], (200,50), 0, False)
        supershot.SetValue(f"SuperShot(Press 1): {self.player.supershot}", assets["font_25"])

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
        self.screen.blit(supershot.text, supershot.rect)

        pygame.display.flip()


    def run_menu(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_ESCAPE):
                    self.gameState = "game"
                    mixer.music.load("assets/Sounds/Battle in the Stars.ogg")
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
                    mixer.music.load("assets/Sounds/Battle in the Stars.ogg")
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
    

    def run_gameover(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_SPACE):
                    self.playagain()
            if event.type == pygame.QUIT:
                self.doClose = True
                pygame.quit()
                exit(0)
        
        self.screen.fill((255,255,255))
        self.screen.blit(self.death.text, self.death.rect)
        self.screen.blit(self.again.text, self.again.rect)
        pygame.display.flip()
    
    def playagain(self):
        for x in self.enemys:
            x.kill()
        self.wave = 0
        self.nextwave = True
        self.enemynum = 0
        self.gameState = "game"
        self.player.health = 3
        self.nextsuper = False