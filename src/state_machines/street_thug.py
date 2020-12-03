from src.state_machines.state_handler import StateHandler
from math import sqrt

state_over = lambda p: p.frame >= p.state_data[p.state][0]
actionable = lambda p: p.frame >= p.state_data[p.state][1]


initstates = [
    [
        lambda piece: piece.state == "idle" and state_over(piece),
        """
        frame= 0
        fi state= walk if not
        fi state= punchstart if dup
        call P:punch_distance
        /*
        i wrote this huge fucking crazy
        code block here and decided to
        replace it with enemy.punch_distance
        */
        """
    ],[
        lambda piece: piece.state == "walk" and piece.punch_distance(),
        """
        frame= 0 state= punchstart
        """
    ],[
        lambda piece: piece.state == "punchstart" and state_over(piece),
        """
        frame= 0 state= punching
        """
    ], [
        lambda piece: piece.state == "punching" and state_over(piece),
        """
        frame= 0 state= idle
        """
    ]
]

applystates = {
    "walk": """
    fi z= + P:z 1 if > 10 - P:z :z P:nearest_player
    fi z= - P:z 1 if < 10 - P:z :z P:nearest_player
    """,
}

def get_state_handler(obj):
    return StateHandler(obj,
                        initstates=initstates,
                        applystates=applystates)
