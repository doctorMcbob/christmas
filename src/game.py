"""
game.py

a good place to start

Here we are again, old friends. Every day is a good day for a christmas adventure.
"""
import pygame
from pygame.locals import *
pygame.init()

from src.controller_handler import ControllerHandler
from src.player import Player
from src.templates.player_templates import HERFY
from src.game_world import load_levels
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

def setup(fullscreen=False, FPS=30):
    """
    eventually put a game menu here...
    """
    game_state = {}
    if fullscreen: game_state["screen"] = pygame.display.set_mode((920, 720), FULLSCREEN)
    else: game_state["screen"] = pygame.display.set_mode((920, 720))

    game_state["clock"] = pygame.time.Clock()
    game_state["FPS"] = FPS
    
    game_state["objects"] = []
    game_state["enemies"] = []

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
    levels = load_levels()
    for level in levels:
        #cutscenes?
        while level.run(game_state):
            level.draw_screen(game_state)
            pygame.display.update()
        #cutscenes?

