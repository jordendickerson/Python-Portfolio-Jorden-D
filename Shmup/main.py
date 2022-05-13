# Main game File
# PACKAGE INSTALLATION REQUIREMENTS: 'pip install pygame'
# Artwork by kenny
import settings
from settings import *
import pygame as pg
from player import *
from enemy import *
from details import *
from animations import *
from hud_functions import *
from powerups import *


# setup pygame
pg.init()
pg.mixer.init()

running = True

def show_gameOver_screen(screen, background, background_rect,clock):
    global running
    screen.blit(background, background_rect)
    draw_text(screen, TITLE, 64, RED, WIDTH /2, HEIGHT / 4)
    draw_text(screen, "Arrows Move           Space to Shoot", 30, WHITE, WIDTH / 2, HEIGHT * 3/4)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False


def draw_text(surf, text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surf = font.render(text,False,color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf, text_rect)

def draw_bar(surf, x, y, pct, h, w, color):
    if pct < 0:
        pct = 0
    BAR_LENGTH = h
    BAR_HEIGHT = w
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, color, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)


def draw_life_img(surf, x, y, count, img):
    if count > 5:
        count = 5
    for i in range(count):
        img_rect = img.get_rect()
        img_rect.x = x + (img.get_width()+5) * i
        img_rect.y = y
        surf.blit(img,img_rect)



def main():
    global running
    game_over = True
    #Create game objects
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    score = 0


    # load assets
    # background
    background = pg.image.load(os.path.join(img_Folder,"background.png")).convert()
    background = pg.transform.scale(background,(WIDTH,HEIGHT))
    bg_rect = background.get_rect()

    # objects
    player_img = pg.image.load(os.path.join(img_Folder, "playerShip.png")).convert()
    player_mini_img = pg.transform.scale(player_img,(40,30))
    player_mini_img.set_colorkey(BLACK)

    bullet_img = pg.image.load(os.path.join(img_Folder, "laser.png")).convert()

    #meteors
    meteor_images = []
    meteor_list = ["meteorBrown_big1.png", "meteorBrown_med1.png", "meteorBrown_small1.png", "meteorBrown_tiny1.png",
                   "meteorBrown_big2.png", "meteorBrown_med3.png", "meteorBrown_small2.png", "meteorBrown_tiny2.png",
                   "meteorBrown_big3.png", "meteorBrown_big4.png", "meteorGrey_big1.png", "meteorGrey_big2.png",
                   "meteorGrey_big3.png", "meteorGrey_big4.png", "meteorGrey_med1.png", "meteorGrey_med2.png",
                   "meteorGrey_small1.png"]
    for img in meteor_list:
        meteor_images.append(pg.image.load(os.path.join(img_Folder, img)).convert())

    explosion_anim = {}
    explosion_anim["lg"] = []
    explosion_anim["sm"] = []
    explosion_anim["playerExp"] = []
    for i in range(9):
        filename = "regularExplosion0{}.png".format(i)
        img = pg.image.load(os.path.join(img_Folder, filename)).convert()
        img.set_colorkey(BLACK)
        lg_img = pg.transform.scale(img,(75,75))
        explosion_anim["lg"].append(lg_img)
        sm_img = pg.transform.scale(img, (30, 30))
        explosion_anim["sm"].append(lg_img)
        filename = "sonicExplosion0{}.png".format(i)
        img = pg.image.load(os.path.join(img_Folder, filename)).convert()
        img.set_colorkey(BLACK)
        explosion_anim["playerExp"].append(img)

    pow_img = {}
    pow_img[pow_list[0]] = pg.image.load(os.path.join(img_Folder, "shield_gold.png")).convert()
    pow_img[pow_list[1]] = pg.image.load(os.path.join(img_Folder, "bolt_gold.png")).convert()
    pow_img[pow_list[2]] = pg.transform.scale(player_img,(20,20))




    #load sound list
    shoot_snd = pg.mixer.Sound(os.path.join(fx_folder, 'Lazer Fire 1.wav'))
    exp_name = ["Explosion 1.wav", "Explosion 4.wav", "rumble1.ogg"]
    expsnd = []
    for snd in exp_name:
        expsnd.append(pg.mixer.Sound(os.path.join(fx_folder, 'Explosion 1.wav')))

    pow_snd = pg.mixer.Sound(os.path.join(fx_folder, 'powerup.wav'))

    music = pg.mixer.music.load(os.path.join(music_folder, "MattOglseby - 3.ogg"))
    pg.mixer.music.set_volume(0.5)

    # play music
    pg.mixer.music.play(loops=-1)

    #start game loop
    while running:

        if game_over:
            show_gameOver_screen(screen, background, bg_rect,clock)
            game_over = False

            # clear all sprites
            all_sprites = pg.sprite.Group()
            enemy_group = pg.sprite.Group()
            player_group = pg.sprite.Group()
            bullet_group = pg.sprite.Group()
            pow_group = pg.sprite.Group()

            # create player
            player = PlayerControlled(player_img, bullet_img, all_sprites, bullet_group, shoot_snd)

            # create stars
            for i in range(1000):
                star = Stars()
                all_sprites.add(star)

            # create enemy
            for i in range(20):
                enemy = Mob(random.choice(meteor_images))
                all_sprites.add(enemy)
                enemy_group.add(enemy)

                # add to sprite groups
                all_sprites.add(player)
                player_group.add(player)
                bullet_group.add()

        # Update clock
        clock.tick(FPS) #makes the clock tick FPS amount every second
        # Process Events
        for event in pg.event.get():
            # get key down
            if event.type == pg.KEYDOWN:
                #esc key down
                if event.key == pg.K_ESCAPE:
                    running = False

            # if the X was clicked
            if event.type == pg.QUIT:
                running = False

        # collision between player sprite and enemy group
        hits = pg.sprite.spritecollide(player,enemy_group,True,pg.sprite.collide_circle)
        if hits:
            for hit in hits:
                # take damage (includes checking for death)
                # play sound
                random.choice(expsnd).play()
                player.takeDamage(hit)
                size = "lg"
                if hit.radius < 25:
                    size = "sm"
                expl = Explosion(hit.rect.center, size, explosion_anim)
                all_sprites.add(expl)
                enemy = Mob(random.choice(meteor_images))
                all_sprites.add(enemy)
                enemy_group.add(enemy)
                # play animation
            if player.shield <= 0:
                expsnd[2].play()
                expl = Explosion(player.rect.center, "playerExp", explosion_anim)
                all_sprites.add(expl)

                player.die()

        if player.lives <= 0 and not expl.alive():
            game_over = True

        # collision between bullet_group and enemy_group
        hits = pg.sprite.groupcollide(enemy_group, bullet_group, True, True)
        if hits:
            for hit in hits:
                score += int(100 - hit.radius)//20
                size = "lg"
                if hit.radius < 25:
                    size = "sm"
                expl = Explosion(hit.rect.center, size, explosion_anim)
                all_sprites.add(expl)
                if random.random() > 0.9:
                    pow = Pow(hit.rect.center, pow_img)
                    pow_group.add(pow)
                    all_sprites.add(pow)
                random.choice(expsnd).play()
                enemy = Mob(random.choice(meteor_images))
                all_sprites.add(enemy)
                enemy_group.add(enemy)
        # if player hits pow
        hits = pg.sprite.spritecollide(player, pow_group, True)
        if hits:
            pow_snd.play()
            for hit in hits:
                if hit.type == pow_list[0]:
                    # play sound
                    # add to player shield
                    player.add_shield(random.randint(25, 75))
                if hit.type == pow_list[1]:
                    # play sound
                    # lower shoot delay
                    player.rapid_fire()
                if hit.type == pow_list[2]:
                    # play sound
                    # add life
                    player.add_life()





        # Update
        all_sprites.update()


        # Draw (things drawn first are furthest back, things drawn last are closest. like painting.)
        screen.fill(cfBlue) #fills screen with cornflower blue
        screen.blit(background, bg_rect)
        all_sprites.draw(screen) #draws all sprites on the screen

        #draw HUD
        draw_text(screen, str(score), 50, BLACK, WIDTH/2, 25) #score
        draw_text(screen, "Health", 30, WHITE, 50, 10) #Health bar label
        draw_bar(screen, 5 , 50, player.shield, 200, 20, GREEN) #Health bar
        # draw_text(screen, "Ammo", 30, WHITE, 550, 10)  # Ammo bar label
        # draw_bar(screen, 550, 50, 100, 48, 200, RED) #Ammo bar
        draw_life_img(screen, WIDTH - 250, 45, player.lives, player_mini_img)

        pg.display.flip() #flips screen MUST BE THE LAST THING CALLED


main()


