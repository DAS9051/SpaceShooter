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
waves = [
Wave(),
Wave(),
Wave()
]


# this loads each wave
def load_waves():
    waves[0].entities = [
        Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(1)
        ]
    waves[1].entities = [Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(2)]
    waves[2].entities = [Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(3)]
