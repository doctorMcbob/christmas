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

from src.controller_handler import ControllerHandler
from src.player import Player
from src.templates.player_templates import HERFY
from src.state_machines import herfy


DEFAULT_KEY_MAP = {
    "left": K_LEFT,
    "right": K_RIGHT,
    "up": K_UP,
    "down": K_DOWN,
    "btn 0": K_z,
    "btn 1": K_x,
}
DEFAULT_JOY_MAP = {
    "left": 0,
    "right": 0,
    "up": 1,
    "down": 1,
    "btn 0": 0,
    "btn 1": 1,
}

def setup(fullscreen=False):
    game_state = {}
    if fullscreen: game_state["screen"] = pygame.display.set_mode((920, 720), FULLSCREEN)
    else: game_state["screen"] = pygame.display.set_mode((920, 720))

    game_state["clock"] = pygame.time.Clock()

    # temporary for testing
    game_state["objects"] = []
    
    game_state["players"] = [Player(HERFY)]
    game_state["players"][0].set_state_handler(
        herfy.get_state_handler(game_state["players"][0]))
    
    game_state["controller handler"] = ControllerHandler()
    for i in range(pygame.joystick.get_count()):
        joy = pygame.joystick.Joystick(i)
        joy.init()
        game_state["controller handler"].add_player(game_state["players"][0], DEFAULT_JOY_MAP, joystick=joy)

    if pygame.joystick.get_count() == 0:
        game_state["controller handler"].add_player(game_state["players"][0], DEFAULT_KEY_MAP)
    
    return game_state

def run_game(game_state):
    while True:
        game_state["clock"].tick(30)

        game_state["controller handler"].update()

        for player in game_state["players"]:
            player.state_handler.update_states()
            player.state_handler.apply_states()
            player.update(player)
            
        for obj in game_state["objects"]:
            obj.update(obj)
        
        game_state["screen"].fill((255, 255, 255))
        for player in game_state["players"]:
            player.draw(game_state["screen"])

        for obj in game_state["objects"]:
            obj.draw(game_state["screen"])
        pygame.display.update()


