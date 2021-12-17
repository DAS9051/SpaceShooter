import pygame
import random

# starts the font pygame module
pygame.font.init()

# creats a empty dictonary for the assets
assets = {}

# creats a empty dictionary for the specs of enemy 1
enemy_data_1 = {}

# creates a empty dictionary for the specs of enemy 2
enemy_data_2 = {}

# # adds both dictinarys to a list
enemy_ships = []

# function to load the assets
def LoadAssets():

    # loads all pictures
    assets["background_purple"] = pygame.image.load("assets/Backgrounds/purple.png")
    assets["background_black"] = pygame.image.load("assets/Backgrounds/black.png")
    assets["playerShip1_blue"] = pygame.image.load("assets/PNG/playerShip1_blue.png")
    assets["font_16"] = pygame.font.Font("assets/Bonus/kenvector_future.ttf", 16)
    assets["font_25"] = pygame.font.Font("assets/Bonus/kenvector_future.ttf", 25)
    assets["Lazer"] = pygame.image.load("assets/PNG/Lasers/laserBlue02.png")
    assets["enemy1"] = pygame.image.load("assets/PNG/Enemies/enemyBlack2.png")
    assets["enemy2"] = pygame.image.load("assets/PNG/Enemies/enemyBlack1.png")
    assets["Lazerenemy"] = pygame.image.load("assets/PNG/Lasers/laserRed04.png")
    assets["player damage"] = pygame.mixer.Sound("assets/Bonus/sfx_lose.ogg")
    assets["gameover"] = pygame.mixer.Sound("assets/Sounds/Defeated (Game Over Tune).ogg")
    assets["damage_sound"] = pygame.mixer.Sound("assets/Bonus/sfx_lose.ogg")

    # loads assets for data 1
    enemy_data_1["image"] = assets["enemy1"]
    enemy_data_1["layer"] = 3
    enemy_data_1["speed"] = random.randint(100, 175)
    enemy_data_1["health"] = 3
    enemy_data_1["shootspeed"] = random.randint(1,3)
    enemy_data_1["bulletimage"] = assets["Lazerenemy"]

    # loads assets for data 2
    enemy_data_2["image"] = assets["enemy2"]
    enemy_data_2["layer"] = 3
    enemy_data_2["speed"] = random.randint(100, 175)
    enemy_data_2["health"] = 3
    enemy_data_2["shootspeed"] = random.randint(1,3)
    enemy_data_2["bulletimage"] = assets["Lazerenemy"]
    
    # adds enemy 1 to enemy_ships
    enemy_ships.append(enemy_data_1)

    # adds enemy 2 to enemy_ships
    enemy_ships.append(enemy_data_2)


