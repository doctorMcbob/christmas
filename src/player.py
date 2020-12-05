from src.game_object import GameObject
from src.sprites import sprites

JUMP_STATE_BLACKLIST = ["jumpstart", "jumping", "landing"]

class Player(GameObject):
    def __init__(self, template):
        GameObject.__init__(self, template)

        self.HP = template["HP"]
        
        self.y_velocity = 0
        self.speed = template["speed"]
        self.walk_speed = template["speed"]
        self.run_speed = template["run speed"]
        self.jump_strength = template["jump strength"]
        self.grav = template["grav"]
        self.jump_direction = 0
        self.weight = template["weight"]

        self.MOV_LEFT = 0
        self.MOV_RIGHT = 0
        self.MOV_UP = 0
        self.MOV_DOWN = 0
        self.BTN_0 = 0
        self.BTN_1 = 0
        
    def get_hit(self, dmg, direction):
        self.HP -= dmg
        if dmg > self.weight:
            self.direction = direction
            self.state = "KNOCKDOWN"
        else:
            self.state = "HIT"
        self.frame = 0

    def die(self, game_state):
        game_state["players"].remove(self)

    
