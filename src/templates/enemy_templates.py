def default_update(self):
    self.frame += 1

STREET_THUG = {
    "W"               : 64,
    "H"               : 96,

    "sprites"         : {}
    "update function" : default_update,

    "state data"      : {
        "idle"       : (-1, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30)),
    }
}
