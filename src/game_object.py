"""
game_object.py

HOW SPRITES WORK
   sprites are stored in a dict
   if the state has only one frame it will be stored
    "state": img
   if the state is animated, it will be stored
    "state:2": img,
    "state:5": img
   in this example, state frame 0, 1, and 2
     will be the first img and frames 3, 4, and 5
     will be the second img. i hope that makes sense
"""
import pygame
from pygame import Surface, Rect
from pygame.font import SysFont
from pygame.transform import flip
from src.sprites import sprites

HEL16 = SysFont("Helvetica", 16)

class GameObject(Rect):

    def __init__(self, template):
        Rect.__init__(self, (template["X"], template["Y"]), (template["W"], template["H"]))
        self.z = 0 if "Z" not in template else template["Z"]
        self.state = "idle"
        self.frame = 0
        self.flag = 0

        self.direction = 1
        if "sprites filename" in template:
            self.sprites = sprites.load_spritesheet(
                template["sprites filename"],
                template["spritesheet data"],
                colorkey=(1, 255, 1)
            )
        else:
            self.sprites = {}

        self.update = template["update function"]
        self.state_data = template["state data"]
        self.state_handler = None

        self.hitboxes = template["hitboxes"] 

        self.sprite_offset = (0, 0) if "sprite offset" not in template else template["sprite offset"]

    def set_state_handler(self, state_handler):
        self.state_handler = state_handler

    def get_position(self):
        return (self.x, self.z)

    def draw(self, destination):
        upper = (destination.get_height() // 3) * 2
        lower = destination.get_height()
        
        X, Y = self.x, (lower - self.y) - self.h

        z_step = (upper - lower) // 100
        Y += self.z * z_step
        X -= (self.z * z_step) // 2

        X += self.sprite_offset[0]
        Y += self.sprite_offset[1]
        self._draw_hitbox(destination)
        destination.blit(self.get_sprite(), (X, Y))

    def _draw_hitbox(self, destination):
        # out dated
        hbox = self.get_hitbox()
        if not hbox:
            return

        pos, dim, dmg = hbox
        X_, Y_ = pos
        
        upper = (destination.get_height() // 3) * 2
        lower = destination.get_height()
        
        X, Y = X_, (lower - Y_) - self.h

        z_step = (upper - lower) // 100
        Y += self.z * z_step
        X -= (self.z * z_step) // 2
        pygame.draw.rect(destination, (255, 0, 0), pygame.Rect((X, Y), dim))

    def get_sprite(self):
        # if state is name of sprite, return it
        if self.state in self.sprites:
            if self.direction == 1:
                return self.sprites[self.state]
            elif self.direction == -1:
                return flip(self.sprites[self.state], 1, 0) 
        # otherwise, find the most recent animation frame
        f = self.frame
        while f >= 0:
            name = self.state + ":" + str(f)
            if name in self.sprites:
                if self.direction == 1:
                    return self.sprites[name]
                elif self.direction == -1:
                    return flip(self.sprites[name], 1, 0)
            f -= 1

        # if no sprite was found, return a placeholder
        draft = Surface((self.w, self.h))
        draft.fill((0, 255, 0))
        draft.blit(HEL16.render(self.state, 0, (0, 0, 0)), (0, 0))
        
        return draft

    def get_hitbox(self):
        if self.state in self.hitboxes:
            pos, dim, dmg = self.hitboxes[self.state]
            X, Y = pos
            if self.direction == 1:
                X += self.left
            if self.direction == -1:
                X = self.right - X - dim[0]
            if self.y: Y = self.y - Y
            return (X, Y), dim, dmg
        return None
