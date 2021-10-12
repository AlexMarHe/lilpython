#clases de la lógica del dodger
import numpy as np
import pygame
import math
import random
class dodgy:
    name="lib"

    #posicion x, posicion y, imagen, vidas
    def __init__(self, x, y, i, v=3):
        self.posx = x
        self.posy = y
        self.im = pygame.image.load(i)
        self.vidas=v

    def change_name(n):
        this.name=n


class enemy:
    name="col"
    muerto = False
    #posicion x, posicion y, imagen
    def __init__(self, x, y, i):
        self.posx = x
        self.posy = y
        self.impulso = round(random.uniform(0.3,0.55), 2)
        self.im = pygame.image.load(i)
        self.colision = False
