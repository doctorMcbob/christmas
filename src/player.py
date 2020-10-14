from src.game_object import GameObject


JUMP_STATE_BLACKLIST = ["jumpstart", "jumping", "landing"]

class Player(GameObject):
    def __init__(self, template):
        GameObject.__init__(self, template)

        self.y_velocity = 0
        self.speed = template["speed"]
        self.jump_strength = template["jump strength"]
        self.grav = template["grav"]
        
        self.MOV_LEFT = 0
        self.MOV_RIGHT = 0
        self.MOV_UP = 0
        self.MOV_DOWN = 0
        self.BTN_0 = 0
        self.BTN_1 = 0

        self.jump_start_frames = template["jump start frames"]
        self.landing_frames = template["landing frames"]
        
    def update_movement_states(self):
        if self.state == "idle" and any(
                [self.MOV_LEFT, self.MOV_RIGHT,
                 self.MOV_UP, self.MOV_DOWN]):
            self.state = "walk"

        if (self.BTN_0 and
            self.state not in JUMP_STATE_BLACKLIST):
            self.state = "jumpstart"
            self.frame = 0

        if (self.state == "jumping" and self.y <= 0):
            self.y = 0
            self.state = "landing"
            self.frame = 0

        if (self.state == "landing" and
            self.frame >= self.landing_frames):
            self.state = "idle"
            self.frame = 0

        if (self.state == "jumpstart" and
            self.frame >= self.jump_start_frames):
            self.state = "jumping"
            self.frame = 0
            self.y_velocity = self.jump_strength
            
    def apply_state(self):
        if self.state == "walk":
            if self.MOV_LEFT: self.x -= self.speed
            if self.MOV_RIGHT: self.x += self.speed
            if self.MOV_UP: self.z = min(100, self.z + 1)
            if self.MOV_DOWN: self.z = max(0, self.z - 1)

        if self.state == "jumping":
            self.y += self.y_velocity
            self.y_velocity += self.grav
            
