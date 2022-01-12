from random import randint
from gameobject import *
from enemy import *
from asset_loader import *


# makes a class for the wave that inhertes game object
class Wave(GameObject):
    
    def __init__(self):
        # creates a variable for the entites
        self.entities = []


# each index in this array is a wave
waves = []

for x in range(50):
    waves.append(Wave())


# this loads each wave
def load_waves():
    for i in range(50):
        waves[i].entities = [Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(i+2)]

