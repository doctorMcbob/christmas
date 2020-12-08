def default_update(self):
    self.frame += 1

STREET_THUG = {
    "name"            : "street thug",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

STREET_THUG2 = {
    "name"            : "street thug",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
    #"sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

WAREHOUSE_WORKER = {
    "name"            : "warehouse worker",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

TECH_BRO = {
    "name"            : "tech bro",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

SPD = {
    "name"            : "seattle police",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

JEFF_BEZOS = {
    "name"            : "jeff bezos",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

PENGUIN = {
    "name"            : "penguin",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

SNOWMAN = {
    "name"            : "snowman",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

WALRUS = {
    "name"            : "walrus",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

POLAR_BEAR = {
    "name"            : "polar bear",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

BUMBLE = {
    "name"            : "bumble",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

ELF = {
    "name"            : "ELF",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

RAINDEER = {
    "name"            : "raindeer",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

GINGERBREAD_MAN = {
    "name"            : "gingerbread man",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

MSCLAUS = {
    "name"            : "ms.Claus",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

SANTA = {
    "name"            : "santa",
    
    "X"               : 0,
    "Y"               : 0,
    "Z"               : 0,
    "W"               : 64,
    "H"               : 96,
    "speed"           : 3,
    "weight"          : 15,
    "HP"              : 1000,

    "fight range"     : 30,
    
    "sprites"         : None,
#    "sprites filename": "streetthug.png",
    "sprite offset"   : (-64, 0),
    "spritesheet data": {
        "idle"           : ((0, 0), (128, 96)),
        "walk:0"         : ((128, 0), (128, 96)),
        "walk:5"         : ((256, 0), (128, 96)),
        "punchstart"     : ((384, 0), (128, 96)),
        "punching"       : ((512, 0), (128, 96)),
        "HIT"            : ((640, 0), (128, 96)),
        "KNOCKDOWN:0"    : ((768, 0), (128, 96)),
        "KNOCKDOWN:10"   : ((896, 0), (128, 96)),
    },
    "update function" : default_update,

    "state data"      : {
        "idle"       : (10, -1),
        "walk"       : (-1, -1),
        "punchstart" : (5, -1),
        "punching"   : (10, -1),
        "punchstart2": (6, -1),
        "punching2"  : (10, -1),
        "punchstart3": (10, -1),
        "punching3"  : (15, -1),
        "HIT"        : (15, -1),
        "KNOCKDOWN"  : (25, -1),
    },
    "hitboxes"        : {
        "punching"  : ((60, 40), (40, 30), 10),
        "punching2" : ((60, 40), (40, 30), 10),
        "punching3" : ((60, 40), (40, 30), 20),
    }
}

