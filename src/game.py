"""
game.py

a good place to start

Ive got some notes here, im going to try to write out my thinking as i go.

im going to write a controller handler class, it will get something like
{
    "player1": {
        "character": <Player Object ()>
        "type": "key" # or "joy" for joystick
        "map": {
            "left" : K_left # or joystick event...
            ...
        }
    },
    "player2": ...,
    "player3": None,
    "player4": None,
}

There will be a player object, it will get a template.
the template will be the "character": herfy, swankers, beefer, and ernie

player will have methods like draw, and update state
"""
import pygame
from pygame.locals import *
pygame.init()

from src.game_object import GameObject

#  DUMMY FOR TESTING
####################################
def dummy_update(self):
    self.z = (self.z + 1) % 100

dummy_obj = GameObject({
    "W": 64, "H": 64,
    "sprites": {},
    "update function": dummy_update
})
####################################


def setup(fullscreen=False):
    game_state = {}
    if fullscreen: game_state["screen"] = pygame.display.set_mode((920, 720), FULLSCREEN)
    else: game_state["screen"] = pygame.display.set_mode((920, 720))

    game_state["clock"] = pygame.time.Clock()
        
    # dummy, just to get something on screen
    game_state["objects"] = [dummy_obj]
    
    return game_state

def run_game(game_state):
    while True:
        game_state["clock"].tick(30)
        
        for obj in game_state["objects"]:
            obj.update(obj)
        
        game_state["screen"].fill((255, 255, 255))
        for obj in game_state["objects"]:
            obj.draw(game_state["screen"])
        pygame.display.update()

        # just until i have the controller handler started
        for e in pygame.event.get():
            if e.type == QUIT: quit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE: quit()

