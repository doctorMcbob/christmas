from src.templates.enemy_templates import STREET_THUG
from src.state_machines import street_thug

LEVELS = [
    {
        "LENGTH"            : 7080,
        "enemies"           : [
            {
                "template"       : STREET_THUG.copy(),
                "spawned"        : 0,
                "scroll"         : 50,
                "position"       : (700, 0, 50),
                "state machine"  : street_thug,
            },
            {
                "template"       : STREET_THUG.copy(),
                "spawned"        : 0,
                "scroll"         : 50,
                "position"       : (700, 0, 20),
                "state machine"  : street_thug,
            },
        ],
        "background image"  : "bkgimg0.png",
    }
]

