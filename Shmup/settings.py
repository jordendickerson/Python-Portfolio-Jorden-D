# Game Settings
import random
import os
import pygame as pg
import random

#set directories
game_Folder = os.path.dirname(__file__)
assets_Folder = os.path.join(game_Folder, "assets")
img_Folder = os.path.join(assets_Folder, "imgs")
audio_Folder = os.path.join(assets_Folder, "audio")
music_folder = os.path.join(audio_Folder, "music")
ambient_foler = os.path.join(audio_Folder, "ambient")
fx_folder = os.path.join(audio_Folder, "fx")

font_name = pg.font.match_font('Comic Sans Ms')


# game title
TITLE = "SHUMP" #Sets title

# screen size
WIDTH = 600 #sets width of screen
HEIGHT = 900 #sets height of screen

# Player Size
PLAYER_HEIGHT = WIDTH // 12
PLAYER_WIDTH = WIDTH // 12

#enemy size
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50

# clock speed
FPS = 30 #sets frames per second (clock tick)

# difficulty
diff = "Normal" #sets difficulty


# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255 ,0)
BLUE = (0, 0 ,255)
cfBlue = (100, 149, 237)

pow_list = ["shield", "gun", "life"]