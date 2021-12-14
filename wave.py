from random import randint
from gameobject import *
from enemy import *
from asset_loader import *

class Wave(GameObject):
    
    def __init__(self):
        self.entities = []


waves = [
Wave(),
Wave(),
Wave()
]

nextwave = True

def load_waves():
    waves[0].entities = [
        Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(1)
        ]
    waves[1].entities = [Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(2)]
    waves[2].entities = [Enemy(0,0, 93,84,0,x,random.choice(enemy_ships)) for x in range(3)]
