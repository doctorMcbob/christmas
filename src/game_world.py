"""
making this up as I go...
I have to have a way for enemies to see the closest player
and a way to scroll when the enemies are all dead
and a way to know when the level is done...

enemy data will be stored in level template, so when the players
reach a certain point they can be spawned (put in the game_state)

I think this should work...
"""
from src.templates import level_templates
from src.sprites import sprites
from src.enemy import Enemy

class GameWorld(object):
    def __init__(self, template):
        self.W = 920
        
        self.LENGTH = template["LENGTH"]
        self.SCROLL = 0

        self.enemies = template["enemies"]
        for enemy in self.enemies:
            enemy["template"]["X"], enemy["template"]["Y"], enemy["template"]["Z"] = enemy["position"]

        self.bkgimg = sprites.get_sprite(template["background image"])
        


    def update_scroller(self, game_state):
        if game_state["enemies"]: return
        if any([player.x <= 15 for player in game_state["players"]]): return
        for player in game_state["players"]:
            if player.x >= self.W - (self.W // 3) and player.MOV_RIGHT:                
                self.SCROLL += player.speed
                
                for _player in game_state["players"]:
                    _player.x -= player.speed

                # spawn enemies 
                for enemy in self.enemies:
                    if enemy["spawned"]: continue
                    if enemy["scroll"] <= self.SCROLL:
                        e = Enemy(enemy["template"])
                        e.set_state_handler(
                            enemy["state machine"].get_state_handler(e)
                        )
                        game_state["enemies"].append(e)
                return


    def draw_screen(self, game_state):
        game_state["screen"].blit(self.bkgimg, (0 - self.SCROLL, 0))
        # gather objects
        objs = game_state["players"] + game_state["enemies"] + game_state["objects"]
        to_draw = []
        # sort by z axis
        while objs:
            idx = 0
            for i, obj in enumerate(objs):
                if obj.z > objs[idx].z: idx = i
            to_draw.append(objs.pop(idx))
        # draw
        for obj in to_draw:
            obj.draw(game_state["screen"])
        

    def run(self, game_state):
        if self.SCROLL < self.LENGTH or game_state["enemies"]:
            game_state["clock"].tick(game_state["FPS"])
            game_state["controller handler"].update()

            for player in game_state["players"]:
                player.state_handler.update_states()
                player.state_handler.apply_states()
                player.update(player)

            for obj in game_state["objects"]:
                obj.update(obj)

            for enemy in game_state["enemies"]:
                enemy.state_handler.update_states()
                enemy.state_handler.apply_states()
                enemy.update_nearest_player(game_state)
                enemy.update(enemy)
                
            self.update_scroller(game_state)
            return True
        else: return False

def load_levels():
    return [GameWorld(template) for template in level_templates.LEVELS]
