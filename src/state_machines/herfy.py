"""
hey man, it makes sense to me so shove it

if your looking for documentation,
i wrote a bit in state_handler.py
"""
from src.state_machines.state_handler import StateHandler

state_over = lambda player: player.frame >= player.state_data[player.state][0]
player_actionable = lambda player: player.frame >= player.state_data[player.state][1]

JUMP_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching", "punchstart2", "punching2", "jumpattackstart", "jumpattack"]
PUNCH_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching", "punchstart2", "punching2", "jumpattackstart", "jumpattack"]

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
    
    [ lambda player: player.state in ["jumping", "jumpattackstart", "jumpattack"] and player.y <= 0,
      """
      y= 0 state= landing frame= 0
      """
    ],

    [ lambda player: player.state == "jumping" and player.BTN_1,
      """
      state= jumpattackstart frame= 0
      """
    ],

    [ lambda player: player.state == "jumpattackstart" and state_over(player),
      """
      state= jumpattack frame= 0
      """
    ],
    
    [ lambda player: player.state == "landing" and state_over(player),
      """
      state= idle frame= 0
      """
    ],
    
    [ lambda player: player.state == "jumpstart" and state_over(player),
      """
      state= jumping frame= 0 y_velocity= P:jump_strength
      """
    ],

    [ lambda player: player.BTN_1 and player.state not in PUNCH_STATE_BLACKLIST,
      """
      state= punchstart frame= 0
      """
    ],

    [ lambda player: player.state == "punchstart" and state_over(player),
      """
      state= punching frame= 0 flag=0
      """
    ],

    [ lambda player: player.state in ["punching", "punching2"] and state_over(player),
      """
      state= idle frame= 0
      """
    ],
    [ lambda player: player.state == "punching" and player.flag and player_actionable(player) and player.BTN_1,
      """
      state= punchstart2 frame= 0
      """
    ],
    [ lambda player: player.state == "punchstart2" and state_over(player),
      """
      state= punching2 frame=0 flag=0
      """
    ],
]

applystates = {
    "walk": """
    fi direction= -1 x= - P:x P:speed if P:MOV_LEFT
    fi direction= 1 x= + P:x P:speed if P:MOV_RIGHT
    fi z= 0 if < P:z 0
    fi z= 100 if > P:z 100
    fi z= + P:z 1 if P:MOV_UP
    fi z= - P:z 1 if P:MOV_DOWN
    fi frame= 0 if == P:frame 11
    """,
    # these three are the same...
    # maybe change key to a list, and check
    # for key in keys, if state in key.
    # i dont really like that though
    "jumping": """
    x= + P:x * P:speed P:jump_direction
    y_velocity= + P:y_velocity P:grav
    y= + P:y P:y_velocity
    """,
    "jumpattackstart" : """
    x= + P:x * P:speed P:jump_direction
    y_velocity= + P:y_velocity P:grav
    y= + P:y P:y_velocity
    """,
    "jumpattack": """
    x= + P:x * P:speed P:jump_direction
    y_velocity= + P:y_velocity P:grav
    y= + P:y P:y_velocity
    """,
    #---
    
    "punching" : """
    fi flag= 1 if == P:BTN_1 0
    """
}

def get_state_handler(player):
    return StateHandler(player,
                        initstates=initstates,
                        applystates=applystates)
