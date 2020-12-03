from src.game_object import GameObject
from math import sqrt

dist = lambda p1, p2: sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class Enemy(GameObject):
    def __init__(self, template):
        GameObject.__init__(self, template)
        self.nearest_player = None
        self.fight_range = template["fight range"]
        self.speed = template["speed"]
        
    def update_nearest_player(self, game_state):
        for player in game_state["players"]:
            if player is self.nearest_player: continue
            if (self.nearest_player is None or
                dist(self.position, player.position) <
                dist(self.position, self.nearest_player.position)):

                self.nearest_player = player

    def punch_distance(self):
        if self.nearest_player is None:
            return False
        if abs(self.nearest_player.z - self.z) > 10:
            return False
        
        if self.x > self.nearest_player.x:
            return self.left - self.nearest_player.right <= self.fight_range
        else:
            return self.nearest_player.left - self.right <= self.fight_range 
