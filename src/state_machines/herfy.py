"""
if your looking for documentation,
i wrote a bit in state_handler.py
"""
from src.state_machines.state_handler import StateHandler

JUMP_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching"]
PUNCH_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching"]
# BASIC MOVEMENT
initstates = [
    [ lambda player: player.state == "idle" and any([player.MOV_LEFT, player.MOV_RIGHT, player.MOV_UP, player.MOV_DOWN]),
      """
      fi direction= -1 if P:MOV_LEFT
      fi direction= 1 if P:MOV_RIGHT
      state= walk frame= 0
      """
    ],
    
    [ lambda player: player.state == "walk" and not any([player.MOV_LEFT, player.MOV_RIGHT, player.MOV_UP, player.MOV_DOWN]),
      """
      state= idle frame= 0
      """
    ],
    
    [ lambda player: player.BTN_0 and player.state not in JUMP_STATE_BLACKLIST,
      """
      state= jumpstart frame= 0
      fi jump_direction= - P:MOV_RIGHT P:MOV_LEFT if == P:state walk
      fi jump_direction= 0 if != P:state walk
      """
    ],
    
    [ lambda player: player.state == "jumping" and player.y <= 0,
      """
      y= 0 state= landing frame= 0
      """
    ],
    
    [ lambda player: player.state == "landing" and player.frame >= player.landing_frames,
      """
      state= idle frame= 0
      """
    ],
    
    [ lambda player: player.state == "jumpstart" and player.frame >= player.jump_start_frames,
      """
      state= jumping frame= 0 y_velocity= P:jump_strength
      """
    ],

    [ lambda player: player.BTN_1 and player.state not in PUNCH_STATE_BLACKLIST,
      """
      state= punchstart frame= 0
      """
    ],
    # TODO figure out a more template-based
    # start frames, end frames solution
    [ lambda player: player.state == "punchstart" and player.frame >= 3,
      """
      state= punching frame= 0
      """
    ],

    [ lambda player: player.state == "punching" and player.frame >= 8,
      """
      state= idle frame= 0
      """
    ]
]

applystates = {
    "walk": """
    fi x= - P:x P:speed if P:MOV_LEFT
    fi x= + P:x P:speed if P:MOV_RIGHT
    fi z= 0 if < P:z 0
    fi z= 100 if > P:z 100
    fi z= + P:z 1 if P:MOV_UP
    fi z= - P:z 1 if P:MOV_DOWN
    """,
    "jumping": """
    x= + P:x * P:speed P:jump_direction
    y_velocity= + P:y_velocity P:grav
    y= + P:y P:y_velocity
    """,
    "punching" : """
    """
}

def get_state_handler(player):
    return StateHandler(player,
                        initstates=initstates,
                        applystates=applystates)
