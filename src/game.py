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
from src.templates import player_templates
from src.game_world import load_levels
from src import state_machines
from src.sprites.sprites import get_sprite

GAME_TITLE = "The Whales Kill Christmas"
VERSION = "0.1"

DEFAULT_KEY_MAP = {
    "left": K_LEFT,
    "right": K_RIGHT,
    "up": K_UP,
    "down": K_DOWN,
    "btn 0": K_z,
    "btn 1": K_x,
    "ready": K_RETURN,
}
DEFAULT_JOY_MAP = {
    "left": 0,
    "right": 0,
    "up": 1,
    "down": 1,
    "btn 0": 0,
    "btn 1": 1,
    "ready": 9,
}

CHARACTERS = {
    "Herfy": {
        "template": player_templates.HERFY,
        "state machine": state_machines.herfy,
        "icon": "herfyicon.png",
    },
    "Swankers": {
        "template": player_templates.SWANKERS,
        "state machine": state_machines.swankers,
        "icon": "swankersicon.png",
    },
    "Beefer": {
        "template": player_templates.BEEFER,
        "state machine": state_machines.beefer,
        "icon": "beefericon.png"
    },
    "Ernie": {
        "template": player_templates.ERNIE,
        "state machine": state_machines.ernie,
        "icon": "ernieicon.png",
    },
}
def boot_menu(game_state):
    """
    problably the least generic code in the project so far, but I dont mind a scripted menu
    """
    PLAYERS = []
    CONTROLLERS = []
    READY = []
    character_names = list(CHARACTERS.keys())
    W, H = game_state["screen"].get_size()
    if not pygame.joystick.get_init():
        pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    for name in character_names:
        CHARACTERS[name]["icon"] = get_sprite(CHARACTERS[name]["icon"], (1, 255, 1))
    while True:
        game_state["screen"].fill((255, 255, 255))
        game_state["screen"].blit(game_state["fonts"]["HEL64"].render(GAME_TITLE, 0, (0, 0, 0)), (32, 32))
        game_state["screen"].blit(game_state["fonts"]["HEL16"].render(VERSION, 0, (0, 0, 0)), (32, 96))

        for i, player in enumerate(PLAYERS):
            if player is None: continue

            game_state["screen"].blit(game_state["fonts"]["HEL32"].render(str(player), 0, (0, 0, 0)), (64 + i * ((W-64) // 4), 256))
            game_state["screen"].blit(CHARACTERS[player]["icon"], (i * ((W - 64) // 4), 320))
            pygame.draw.rect(game_state["screen"], [(0, 0, 0), (50, 200, 50)][READY[i]], pygame.Rect(((64 + i * ((W-64) // 4), 648), (128, 64))))
            game_state["screen"].blit(game_state["fonts"]["HEL32"].render("READY", 0, [(255, 255, 255), (0, 0, 0)][READY[i]]), (66 + i * ((W - 64) // 4), 650))
            
            if CONTROLLERS[i] == "key":
                if not pygame.event.peek(KEYDOWN): continue
                keys = pygame.key.get_pressed()
                if keys[DEFAULT_KEY_MAP["ready"]]:
                    READY[i] = not READY[i]
                if keys[DEFAULT_KEY_MAP["right"]]:
                    idx = (character_names.index(player) + 1) % 4
                    while character_names[idx] in PLAYERS and idx != i:
                        idx += 1
                        idx %= 4
                    PLAYERS[i] = character_names[idx]
                if keys[DEFAULT_KEY_MAP["left"]]:
                    idx = (character_names.index(player) - 1) % 4 
                    while character_names[idx] in PLAYERS and idx != i:
                        idx += 1
                        idx %= 4
                    PLAYERS[i] = character_names[idx]
            else:
                if not (pygame.event.peek(JOYHATMOTION) or pygame.event.peek(JOYBUTTONDOWN)): continue
                if CONTROLLERS[i].get_button(DEFAULT_JOY_MAP["ready"]):
                    READY[i] = not READY[i]
                if CONTROLLERS[i].get_hat(0)[0] == 1 or CONTROLLERS[i].get_axis(DEFAULT_JOY_MAP["right"]) > .4:
                    idx = (character_names.index(player) + 1) % 4
                    while character_names[idx] in PLAYERS and idx != i:
                        idx += 1
                        idx %= 4
                    PLAYERS[i] = character_names[idx]
                if CONTROLLERS[i].get_hat(0)[0] == -1 or CONTROLLERS[i].get_axis(DEFAULT_JOY_MAP["left"]) < -.4:
                    idx = (character_names.index(player) - 1) % 4 
                    while character_names[idx] in PLAYERS and idx != i:
                        idx += 1
                        idx %= 4
                    PLAYERS[i] = character_names[idx]
        game_state["controller handler"].update()
        pygame.event.clear()

        if len(PLAYERS) < 4:
            if "key" not in CONTROLLERS:
                if any(pygame.key.get_pressed()):
                    for name in character_names:
                        if name in PLAYERS: continue
                        PLAYERS.append(name)
                        break
                    CONTROLLERS.append("key")
                    READY.append(False)
            for joy in joysticks:
                if joy not in CONTROLLERS:
                    if not joy.get_init():
                        joy.init()
                    for btn in range(joy.get_numbuttons()):
                        if not joy.get_button(btn): continue
                        for name in character_names:
                            if name in PLAYERS: continue
                            PLAYERS.append(name)
                            break
                        CONTROLLERS.append(joy)
                        READY.append(False)
                        break

        pygame.display.update()

        if READY and all(READY): break

    for i, player in enumerate(PLAYERS):
        player_obj = Player(CHARACTERS[player]["template"])
        player_obj.set_state_handler(
            CHARACTERS[player]["state machine"].get_state_handler(
                player_obj)
        )
        if CONTROLLERS[i] == "key":
            game_state["controller handler"].add_player(
                player_obj, DEFAULT_KEY_MAP
            )
        else:
            game_state["controller handler"].add_player(
                player_obj, DEFAULT_JOY_MAP, CONTROLLERS[i]
            )
        game_state["players"].append(player_obj)


def setup(screen=None, fullscreen=False, FPS=30):
    """
    added screen as optional argument so this can be called again after game over
    """
    game_state = {}
    if screen: game_state["screen"] = screen
    elif fullscreen: game_state["screen"] = pygame.display.set_mode((920, 720), FULLSCREEN)
    else: game_state["screen"] = pygame.display.set_mode((920, 720))

    game_state["fonts"] = {
        "HEL16" : pygame.font.SysFont("Helvetica", 16),
        "HEL32" : pygame.font.SysFont("Helvetica", 32),
        "HEL64" : pygame.font.SysFont("Helvetica", 64),
        "HEL128": pygame.font.SysFont("Helvetica", 128)
    }
    game_state["clock"] = pygame.time.Clock()
    game_state["FPS"] = FPS
    game_state["objects"] = []
    game_state["enemies"] = []
    game_state["players"] = []
    game_state["controller handler"] = ControllerHandler()
    boot_menu(game_state)
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
    while True:
        levels = load_levels()
        for level in levels:
            #cutscenes?
            while level.run(game_state):
                level.draw_screen(game_state)
                pygame.display.update()
                if not game_state["players"]:
                    game_over(game_state, level)
        #cutscenes?

