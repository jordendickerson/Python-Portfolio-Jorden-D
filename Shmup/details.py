import settings
from settings import *
import pygame as pg
from player import *
from enemy import *
import random


class Stars(pg.sprite.Sprite):
    def __init__(self):
        super(Stars, self).__init__()
        self.image = pg.Surface((2,2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0,WIDTH)
        self.rect.centery = random.randint(-100000,0)
        self.movespeed = 15

    def update(self):
        self.rect.bottom += self.movespeed