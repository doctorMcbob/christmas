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
from src.enemy import Enemy
from src.templates.player_templates import HERFY
from src.templates.enemy_templates import STREET_THUG
from src.game_world import load_levels
from src.state_machines import herfy, street_thug


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

    game_state["fonts"] = {
        "HEL128": pygame.font.SysFont("Helvetica", 128)
    }
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


def game_over(game_state, level):
    t = 0 - game_state["screen"].get_height()
    while level.run(game_state):
        if t < 0: t += 6
        else: t = 0
        pygame.draw.rect(game_state["screen"], (255, 0, 0) ,pygame.Rect((0, t), game_state["screen"].get_size()))
        game_state["screen"].blit(game_state["fonts"]["HEL128"].render("Game Over", 0, (0, 0, 0)), (64, t + 128))
        pygame.display.update()


def run_game(game_state):
    levels = load_levels()
    for level in levels:
        #cutscenes?
        while level.run(game_state):
            level.draw_screen(game_state)
            pygame.display.update()
            if not game_state["players"]:
                game_over(game_state, level)
        #cutscenes?

