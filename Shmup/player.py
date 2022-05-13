from settings import *
import pygame as pg
import random



class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/1.05)


    def update(self):
        pass

    # def screenwrapping(self):
    #     if self.rect.x > WIDTH: #if the rectangle leaves the screen on the right it is sent to the other side
    #         self.rect.x = -PLAYER_WIDTH
    #     elif self.rect.x < -PLAYER_WIDTH: #if the rectangle leaves the screen on the left it is sent to the other side
    #         self.rect.x = WIDTH
    #
    #     if self.rect.y > HEIGHT: #if the rectangle leaves the screen on the top it is sent to the bottom
    #         self.rect.y = -PLAYER_HEIGHT
    #     elif self.rect.y < -PLAYER_HEIGHT: #if the rectangle leaves the screen on the bottom it is sent to the top
    #         self.rect.y = HEIGHT
    #
    # def screenbouncing(self):
    #     #reverse the speed variable when the player reaches the bounds of the window
    #     if self.rect.x > 400-PLAYER_WIDTH:#
    #         self.xspeed = -self.xspeed
    #     if self.rect.x < 0:
    #         self.xspeed = -self.xspeed
    #     if self.rect.y > 400-PLAYER_HEIGHT:
    #         self.yspeed = -self.yspeed
    #     if self.rect.y < 0:
    #         self.yspeed = -self.yspeed
    #
    # def bounceLeft(self):
    #     self.xspeed = -self.xspeed
    # def bounceRight(self):
    #     self.xspeed = -self.xspeed
    # def bouceUp(self):
    #     self.yspeed = -self.yspeed
    # def bounceDown(self):
    #     self.yspeed = -self.yspeed




class PlayerControlled(pg.sprite.Sprite):
    def __init__(self, sprite, bullet_img, all_sprites, bullet_group, shoot_snd):
        super(PlayerControlled, self).__init__()
        # player image
        self.image = sprite
        self.image = pg.transform.scale(self.image,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.image.set_colorkey(BLACK)


        # Player rect & radius
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .80 / 2
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT-40
        # pg.draw.circle(self.image, RED, self.rect.center, self.radius)


        # Player speed
        self.moveSpeed = 15
        self.speed_x = 0
        self.dir_x = 0

        self.shield = 100

        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

        self.bullet_img = bullet_img
        self.all_sprites = all_sprites
        self.bullet_group = bullet_group
        self.shoot_snd = shoot_snd

        self.lives = 5
        self.hidden = False
        self.hide_timer = pg.time.get_ticks()

        self.power_level = 0



    def update(self):
        if self.hidden and pg.time.get_ticks() - self.hide_timer > 1500:
            self.hidden = False
            self.rect.centerx = (WIDTH / 2)
            self.rect.bottom = HEIGHT - 40



        self.speed_x = 0


        # get key pressed
        keystate = pg.key.get_pressed()
        # move sprite
        if keystate[pg.K_a] or keystate[pg.K_LEFT]:
            self.speed_x = self.moveSpeed * -1
        if keystate[pg.K_d] or keystate[pg.K_RIGHT]:
            self.speed_x = self.moveSpeed

        #shoot
        if keystate[pg.K_SPACE]:
            self.shoot(self.bullet_img, self.all_sprites, self.bullet_group,500, self.shoot_snd)


        # mousex,mousey = pg.mouse.get_pos()
        # self.rect.center = (mousex,HEIGHT / 1.05)

        # bind to screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0


        # update sprite position
        self.rect.centerx += self.speed_x

    def shoot(self, sprite, all_sprites, bullet_group,ammo,shoot_snd):

        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            if ammo > 0:
                self.last_shot = now
                if self.power_level == 0:
                    shoot_snd.play()
                    bullet = Bullet(sprite, self.rect.centerx, self.rect.centery-1, all_sprites, bullet_group)
                    ammo -= 1
                elif self.power_level == 1:
                    bullet = Bullet(sprite, self.rect.centerx, self.rect.centery - 1, all_sprites, bullet_group)
                    self.shoot_delay = 200
                elif self.power_level == 2:
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group)
                elif self.power_level == 3:
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.centerx, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group)
                elif self.power_level == 4:
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group, -5)
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group, +5)
                elif self.power_level == 5:
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group, -5)
                    bullet = Bullet(sprite, self.rect.left, self.rect.centery - 1, all_sprites, bullet_group, -8)
                    bullet = Bullet(sprite, self.rect.centerx, self.rect.centery - 1, all_sprites, bullet_group)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group, +5)
                    bullet = Bullet(sprite, self.rect.right, self.rect.centery - 1, all_sprites, bullet_group, +8)



    def die(self):
        self.loseLife()
        self.hide()
        self.shield = 100

    def takeDamage(self, hit):
        self.shield -= hit.radius
    def loseLife(self):
        self.lives -= 1

    def add_shield(self, num):
        self.shield += num
        if self.shield >= 100:
            self.shield = 100

    def add_life(self):
        self.lives += 1

    def rapid_fire(self):
        self.power_level += 1
        if self.power_level > 5:
            self.power_level = 5

    def hide(self):
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 1000)



class Bullet(pg.sprite.Sprite):
    def __init__(self, sprite, x, y, all_sprites,bullet_group, speed_x = 0):
        super(Bullet, self).__init__()
        # Bullet image

        self.image = sprite
        self.image = pg.transform.scale(self.image, (10, 20))
        self.image.set_colorkey(BLACK)


        # Bullet rect & radius
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .80 / 2
        self.rect.centerx = x
        self.rect.bottom = y
        # pg.draw.circle(self.image, RED, self.rect.center, self.radius)


        # Bullet speed
        self.moveSpeed = 20
        self.speed_y = -self.moveSpeed
        self.speed_x = speed_x

        #bullet sprite groups
        all_sprites.add(self)
        bullet_group.add(self)

    def update(self):
        self.rect.centery += self.speed_y
        self.rect.centerx += self.speed_x
        if self.rect.bottom < -15:
            self.kill()

