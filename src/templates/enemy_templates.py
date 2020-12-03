def default_update(self):
    self.frame += 1

STREET_THUG = {
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 2,
    "HP"              : 100,

    "fight range"     : 30,
    
    "sprites"         : {},
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (50, 30)),
    }
}
