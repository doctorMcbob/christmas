from src.templates.enemy_templates import STREET_THUG

LEVELS = [
    {
        "LENGTH"            : 7080,
        "enemies"           : [
            {
                "template"       : STREET_THUG.copy(),
                "spawned"        : 0,
                "scroll"         : 50,
                "position"       : (700, 0, 50),
                "state machine"  : None,
            },
            {
                "template"       : STREET_THUG.copy(),
                "spawned"        : 0,
                "scroll"         : 50,
                "position"       : (700, 0, 20),
                "state machine"  : None,
            },
        ],
        "background image"  : "bkgimg0.png",
    }
]

