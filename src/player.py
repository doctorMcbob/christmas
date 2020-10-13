from src.game_object import GameObject

class Player(GameObject):
    def __init__(self, template):
        GameObject.__init__(self, template)

        self.y_velocity = 0

        self.MOV_LEFT = 0
        self.MOV_RIGHT = 0
        self.MOV_UP = 0
        self.MOV_DOWN = 0
        self.BTN_0 = 0
        self.BTN_1 = 0

    def update_movement(self):
        pass
