import pygame
from pygame.locals import *

class ControllerHandler(object):
    def __init__(self, QUITKEY=K_ESCAPE):
        self.P1 = None
        self.P2 = None
        self.P3 = None
        self.P4 = None
        self.QUITKEY = QUITKEY

    def add_player(self, player_obj, btn_map, joystick=None):
        controller = {
            "player" : player_obj,
            "type"   : "joy" if joystick else "key",
            "joy"    : joystick,
            "map"    : btn_map,
        }
        if self.P1 is None:
            self.P1 = controller
        elif self.P2 is None:
            self.P2 = controller
        elif self.P3 is None:
            self.P3 = controller
        elif self.P4 is None:
            self.P4 = controller

    def update(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[self.QUITKEY]: quit()
        
        for P in [self.P1, self.P2, self.P3, self.P4]:
            if P is None: continue
            player = P["player"]
            if P["type"] == "key":
                player.MOV_LEFT = keys[P["map"]["left"]]
                player.MOV_RIGHT = keys[P["map"]["right"]]
                player.MOV_UP = keys[P["map"]["up"]]
                player.MOV_DOWN = keys[P["map"]["down"]]
                player.BTN_0 = keys[P["map"]["btn 0"]]
                player.BTN_1 = keys[P["map"]["btn 1"]]

            if P["type"] == "joy":
                joy = P["joy"]
                if joy.get_numhats():
                    hat = joy.get_hat(0)
                    player.MOV_LEFT = hat[0] == -1
                    player.MOV_RIGHT = hat[0] == 1
                    player.MOV_UP = hat[1] == 1
                    player.MOV_DOWN = hat[1] == -1

                #         TODO
                # if joy.get_numaxes():
                #     ax = joy.get_axis(0)
                #     player.MOV_LEFT = ax[0] == -1
                #     player.MOV_RIGHT = ax[0] == 1
                #     player.MOV_UP = ax[1] == 1
                #     player.MOV_DOWN = ax[1] == -1
                
                player.BTN_0 = joy.get_button(P["map"]["btn 0"])
                player.BTN_1 = joy.get_button(P["map"]["btn 1"])
                
