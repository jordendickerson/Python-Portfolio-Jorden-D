import pygame as pg
from settings import *


class Mob(pg.sprite.Sprite):
    def __init__(self, sprite):
        super(Mob, self).__init__()
        # Enemy image
        self.image_original = sprite
        self.image_original.set_colorkey(BLACK)
        self.image = self.image_original.copy()

        # self.image = pg.transform.scale(self.image, (50, 40))



        # Enemy rect & radius
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(20, WIDTH-20)
        self.rect.bottom = random.randint(-100, -20)
        self.radius = (self.rect.width * .80) / 2
        # pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        # Enemy speed
        self.speed_x = random.randint(-3,3)
        self.speed_y = random.randint(4,18)

        #rotation
        self.rot = 0
        self.rot_speed = random.randint(-8,8)
        self.last_update = pg.time.get_ticks()




    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed)%360
            newimg = pg.transform.rotate(self.image_original, self.rot)
            oldcenter = self.rect.center
            self.image = newimg
            self.rect = self.image.get_rect()
            self.rect.center = oldcenter

    def update(self):
        self.rotate()
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y
        self.screenwrapping()


    def screenwrapping(self):
        # if self.rect.left > WIDTH:  # if the rectangle leaves the screen on the right it is sent to the other side
        #     self.rect.left = -ENEMY_WIDTH
        # elif self.rect.right < -ENEMY_WIDTH:  # if the rectangle leaves the screen on the left it is sent to the other side
        #     self.rect.right = WIDTH

        # if self.rect.top >HEIGHT + random.randint


        # elif self.rect.bottom <= -ENEMY_HEIGHT:  # if the rectangle leaves the screen on the bottom it is sent to the top
        #     self.rect.bottom = 0
        if self.rect.x > WIDTH: #if the rectangle leaves the screen on the right it is sent to the other side
            self.rect.x = -PLAYER_WIDTH
            if self.rect.y <= HEIGHT - (PLAYER_HEIGHT+20):
                self.rect.y = -PLAYER_HEIGHT
        elif self.rect.x < -PLAYER_WIDTH: #if the rectangle leaves the screen on the left it is sent to the other side
            self.rect.x = WIDTH
            if self.rect.y <= HEIGHT - (PLAYER_HEIGHT+20):
                self.rect.y = -PLAYER_HEIGHT

        if self.rect.y > HEIGHT: #if the rectangle leaves the screen on the top it is sent to the bottom
            self.rect.y = -PLAYER_HEIGHT
        elif self.rect.y < -PLAYER_HEIGHT: #if the rectangle leaves the screen on the bottom it is sent to the top
            self.rect.y = HEIGHT