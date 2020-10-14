def default_update(self):
    self.frame += 1

HERFY = {
    "W"                 : 64,
    "H"                 : 96,
    
    "speed"             : 5,
    "jump strength"     : 20,
    "grav"              : -2,
    "jump start frames" : 3,
    "landing frames"    : 3,

    "sprites"           : {},
    "update function"   : default_update,
}
