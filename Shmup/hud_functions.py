import pygame as pg
import settings
import player




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