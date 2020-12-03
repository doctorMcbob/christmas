import pygame
from pygame import Surface

def load_spritesheet(filename, data, colorkey=None):
    """data should be dict with key: ((x, y), (w, h)), assumes w, h are 32, 32"""
    surf = pygame.image.load("src/sprites/bin/"+filename).convert()
    sheet = {}
    for name in data:
        sprite = Surface(data[name][1])
        x, y = 0 - data[name][0][0], 0 - data[name][0][1]
        sprite.blit(surf, (x, y))
        sprite.set_colorkey(colorkey)
        sheet[name] = sprite
    return sheet

def get_sprite(filename, colorkey=None):
    surf = pygame.image.load("src/sprites/bin/"+filename).convert()
    surf.set_colorkey(colorkey)
    return surf
