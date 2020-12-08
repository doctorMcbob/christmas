from src.state_machines.state_handler import StateHandler
from math import sqrt

state_over = lambda p: p.frame >= p.state_data[p.state][0]

initstates = [
    [
        lambda piece: piece.state == "idle" and state_over(piece),
        """
        frame= 0
        fi state= walk if not
        fi state= punchstart if dup
        call P:punch_distance
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
        fi state= idle if not
        fi state= punchstart2 if dup
        call P:punch_distance
        frame= 0 
        """
    ], [
        lambda piece: piece.state == "punchstart2" and state_over(piece),
        """
        frame= 0 state= punching2
        """
    ], [
        lambda piece: piece.state == "punching2" and state_over(piece),
        """
        fi state= idle if not
        fi state= punchstart3 if dup
        call P:punch_distance
        frame= 0 
        """
    ], [
        lambda piece: piece.state == "punchstart3" and state_over(piece),
        """
        frame= 0 state= punching3
        """
    ], [
        lambda piece: piece.state == "punching3" and state_over(piece),
        """
        frame= 0 state= idle
        """
    ], [
        lambda piece: piece.state == "HIT" and state_over(piece),
        """
        frame= 0 state= idle
        """
    ], [
        lambda piece: piece.state == "KNOCKDOWN" and state_over(piece),
        """
        frame= 0 state= idle
        """
    ]
]

applystates = {
    "walk": """
    fi frame= 0 if == P:frame 10
    fi direction= 1 if < P:x :x P:nearest_player
    fi direction= -1 if > P:x :x P:nearest_player
    fi
       fi z= + P:z 1 if > 
         10 - P:z :z P:nearest_player
       fi z= - P:z 1 if < 
         10 - P:z :z P:nearest_player
       fi x= + P:x P:speed if > 
         P:fight_range - P:x :x P:nearest_player
       fi x= - P:x P:speed if < 
         P:fight_range - P:x :x P:nearest_player
    if % swap 2 / P:frame 5
    """,
    "KNOCKDOWN": """
    x= + P:x * * 2 P:speed P:direction
    """
}

def get_state_handler(obj):
    return StateHandler(obj,
                        initstates=initstates,
                        applystates=applystates)
