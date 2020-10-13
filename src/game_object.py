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
from pygame import Surface
from pygame.font import SysFont

HEL16 = SysFont("Helvetica", 16)

class GameObject(object):

    def __init__(self, template):
        self.X = 0
        self.Y = 0
        self.Z = 0

        self.W = template["W"]
        self.H = template["H"]
        
        self.state = "idle"
        self.frame = 0
        
        self.sprites = template["sprites"]

        self.update = template["update function"]

    def draw(self, destination):
        upper = (destination.get_height() // 3) * 2
        lower = destination.get_height()
        
        X, Y = self.X, (lower - self.Y) - self.H

        z_step = (upper - lower) // 100
        Y += self.Z * z_step
        X -= (self.Z * z_step) // 2
        
        destination.blit(self.get_sprite(), (X, Y))

    def get_sprite(self):
        # if state is name of sprite, return it
        if self.state in self.sprites:
            return self.sprites[self.state]

        # otherwise, find the most recent animation frame
        f = self.frame
        while f >= 0:
            name = self.state + ":" + str(f)
            if name in self.sprites:
                return self.sprites[name]
            f -= 1

        # if no sprite was found, return a placeholder
        draft = Surface((self.W, self.H))
        draft.fill((0, 255, 0))
        draft.blit(HEL16.render(self.state, 0, (0, 0, 0)), (0, 0))
        
        return draft

