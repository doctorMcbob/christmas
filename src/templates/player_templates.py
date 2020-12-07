def default_update(self):
    self.frame += 1

HERFY = {
    "name"              : "Herfy",
    
    "X"                 : 0,
    "Y"                 : 0,
    "W"                 : 128,
    "H"                 : 96,
    
    "speed"             : 5,
    "run speed"          : 9,
    "jump strength"     : 20,
    "grav"              : -2,
    "weight"            : 18,

    "HP"                : 5000,

    "sprites"           : None,
    "sprites filename"  : "herfy.png",
    "spritesheet data"  : {
        "idle"            : ((0, 0),(128, 96)),
        "walk:0"          : ((128, 0),(128, 96)),
        "walk:5"         : ((256, 0),(128, 96)),
        "jumpstart"       : ((384, 0),(128, 96)),
        "jumping"         : ((512, 0),(128, 96)),
        "landing"         : ((640, 0),(128, 96)),
        "jumpattackstart" : ((768, 0),(128, 96)),
        "jumpattack"      : ((896, 0),(128, 96)),
        "punchstart"      : ((1024, 0),(128, 96)),
        "punching"        : ((1152, 0),(128, 96)),
        "punchstart2"     : ((1280, 0),(128, 96)),
        "punching2"       : ((1408, 0),(128, 96)),
        "HIT"             : ((1536, 0), (128, 96)),
        "KNOCKDOWN:0"     : ((1664, 0), (128, 96)),
        "KNOCKDOWN:25"    : ((1792, 0), (128, 96)),
        "run:0"           : ((1920, 0), (128, 96)),
        "run:4"           : ((2048, 0), (128, 96)),
        "run:8"           : ((2176, 0), (128, 96)),
    },
    "update function"   : default_update,

    "state data"        : {
    # to be indexed in the state machine
    # ( frames, first actionable ) neg 1 if N/A
        "idle"            : (-1, -1),
        "walk"            : (10, -1),
        "run"             : (12, -1),
        "jumpstart"       : (3, -1),
        "jumping"         : (-1, -1),
        "landing"         : (3, -1),
        "jumpattackstart" : (4, -1),
        "jumpattack"      : (-1, -1),
        "punchstart"      : (3, -1),
        "punching"        : (8, 3),
        "punchstart2"     : (2, -1),
        "punching2"       : (10, 5),
        "HIT"             : (25, -1),
        "KNOCKDOWN"       : (45, -1),
    },
    "hitboxes" : {
        # state : rect relative to player position
        # (p.x + x, p.y + y, w, h)
        # when direction is flipped, adjust based on
        # top right instead of top left
        "punching"    : ((120, 40), (40, 30), 10),
        "punching2"   : ((120, 20), (50, 50), 10),
        "jumpattack"  : ((-10, -5), (150, 110), 25),
        "run"         : ((96, 0), (64, 128), 16)
    }
}

BEEFER = {
    "name"              : "Beefer",
    
    "X"                 : 0,
    "Y"                 : 0,
    "W"                 : 96,
    "H"                 : 128,
    
    "speed"             : 4,
    "run speed"         : 7,
    "jump strength"     : 10,
    "grav"              : -1,
    "weight"            : 20,

    "HP"                : 5000,

    "sprites"           : None,
#    "sprites filename"  : "herfy.png",
    "spritesheet data"  : {
    },
    "update function"   : default_update,

    "state data"        : {
    # to be indexed in the state machine
    # ( frames, first actionable ) neg 1 if N/A
        "idle"            : (-1, -1),
        "walk"            : (10, -1),
        "run"             : (10, -1),
        "jumpstart"       : (5, -1),
        "jumping"         : (-1, -1),
        "landing"         : (5, -1),
        "jumpattackstart" : (4, -1),
        "jumpattack"      : (-1, -1),
        "punchstart"      : (3, -1),
        "punching_0"      : (4, -1),
        "punching_1"      : (5, 3),
        "HIT"             : (25, -1),
        "KNOCKDOWN"       : (45, -1),
    },
    "hitboxes" : {
        # state : rect relative to player position
        # (p.x + x, p.y + y, w, h)
        # when direction is flipped, adjust based on
        # top right instead of top left
        "punching_0"  : ((0, 64), (64, 32), 10),
        "punching_1"  : ((64, 64), (64, 32), 10),
        "jumpattack"  : ((-10, -5), (150, 110), 25),
        "landing"     : ((-32, 64), (160, 32), 10),
    }
}

SWANKERS = {
    "name"              : "Swankers",
    
    "X"                 : 0,
    "Y"                 : 0,
    "W"                 : 128,
    "H"                 : 96,
    
    "speed"             : 5,
    "run speed"          : 9,
    "jump strength"     : 20,
    "grav"              : -2,
    "weight"            : 18,

    "HP"                : 5000,

    "sprites"           : None,
#    "sprites filename"  : "herfy.png",
    "spritesheet data"  : {
        "idle"            : ((0, 0),(128, 96)),
        "walk:0"          : ((128, 0),(128, 96)),
        "walk:5"         : ((256, 0),(128, 96)),
        "jumpstart"       : ((384, 0),(128, 96)),
        "jumping"         : ((512, 0),(128, 96)),
        "landing"         : ((640, 0),(128, 96)),
        "jumpattackstart" : ((768, 0),(128, 96)),
        "jumpattack"      : ((896, 0),(128, 96)),
        "punchstart"      : ((1024, 0),(128, 96)),
        "punching"        : ((1152, 0),(128, 96)),
        "punchstart2"     : ((1280, 0),(128, 96)),
        "punching2"       : ((1408, 0),(128, 96)),
    },
    "update function"   : default_update,

    "state data"        : {
    # to be indexed in the state machine
    # ( frames, first actionable ) neg 1 if N/A
        "idle"            : (-1, -1),
        "walk"            : (10, -1),
        "run"             : (10, -1),
        "jumpstart"       : (3, -1),
        "jumping"         : (-1, -1),
        "landing"         : (3, -1),
        "jumpattackstart" : (4, -1),
        "jumpattack"      : (-1, -1),
        "punchstart"      : (3, -1),
        "punching"        : (8, 3),
        "punchstart2"     : (2, -1),
        "punching2"       : (10, 5),
        "HIT"             : (25, -1),
        "KNOCKDOWN"       : (45, -1),
    },
    "hitboxes" : {
        # state : rect relative to player position
        # (p.x + x, p.y + y, w, h)
        # when direction is flipped, adjust based on
        # top right instead of top left
        "punching"    : ((120, 40), (40, 30), 10),
        "punching2"   : ((120, 20), (50, 50), 10),
        "jumpattack"  : ((-10, -5), (150, 110), 25),
    }
}

ERNIE = {
    "name"              : "Ernie",
    
    "X"                 : 0,
    "Y"                 : 0,
    "W"                 : 128,
    "H"                 : 96,
    
    "speed"             : 5,
    "run speed"          : 9,
    "jump strength"     : 20,
    "grav"              : -2,
    "weight"            : 18,

    "HP"                : 5000,

    "sprites"           : None,
#    "sprites filename"  : "herfy.png",
    "spritesheet data"  : {
        "idle"            : ((0, 0),(128, 96)),
        "walk:0"          : ((128, 0),(128, 96)),
        "walk:5"         : ((256, 0),(128, 96)),
        "jumpstart"       : ((384, 0),(128, 96)),
        "jumping"         : ((512, 0),(128, 96)),
        "landing"         : ((640, 0),(128, 96)),
        "jumpattackstart" : ((768, 0),(128, 96)),
        "jumpattack"      : ((896, 0),(128, 96)),
        "punchstart"      : ((1024, 0),(128, 96)),
        "punching"        : ((1152, 0),(128, 96)),
        "punchstart2"     : ((1280, 0),(128, 96)),
        "punching2"       : ((1408, 0),(128, 96)),
    },
    "update function"   : default_update,

    "state data"        : {
    # to be indexed in the state machine
    # ( frames, first actionable ) neg 1 if N/A
        "idle"            : (-1, -1),
        "walk"            : (10, -1),
        "run"             : (10, -1),
        "jumpstart"       : (3, -1),
        "jumping"         : (-1, -1),
        "landing"         : (3, -1),
        "jumpattackstart" : (4, -1),
        "jumpattack"      : (-1, -1),
        "punchstart"      : (3, -1),
        "punching"        : (8, 3),
        "punchstart2"     : (2, -1),
        "punching2"       : (10, 5),
        "HIT"             : (25, -1),
        "KNOCKDOWN"       : (45, -1),
    },
    "hitboxes" : {
        # state : rect relative to player position
        # (p.x + x, p.y + y, w, h)
        # when direction is flipped, adjust based on
        # top right instead of top left
        "punching"    : ((120, 40), (40, 30), 10),
        "punching2"   : ((120, 20), (50, 50), 10),
        "jumpattack"  : ((-10, -5), (150, 110), 25),
    }
}
