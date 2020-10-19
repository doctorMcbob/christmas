def default_update(self):
    self.frame += 1

HERFY = {
    "W"                 : 128,
    "H"                 : 96,
    
    "speed"             : 5,
    "jump strength"     : 20,
    "grav"              : -2,

    "sprites"           : {},
    "update function"   : default_update,

    "state data"        : {
    # to be indexed in the state machine
    # ( frames, first actionable ) neg 1 if N/A
        "idle"            : (-1, -1),
        "walk"            : (-1, -1),
        "jumpstart"       : (3, -1),
        "jumping"         : (-1, -1),
        "landing"         : (3, -1),
        "jumpattackstart" : (4, -1),
        "jumpattack"      : (-1, -1),
        "punchstart"      : (3, -1),
        "punching"        : (8, 3),
        "punchstart2"     : (2, -1),
        "punching2"       : (10, 5),
    },
    "hitboxes" : {
        # state : rect relative to player position
        # (p.x + x, p.y + y, w, h)
        # when direction is flipped, adjust based on
        # top right instead of top left
        "punching"    : ((120, 40), (40, 30)),
        "punching2"   : ((120, 20), (50, 50)),
        "jumpattack"  : ((-10, -5), (150, 110)),
    }
}
