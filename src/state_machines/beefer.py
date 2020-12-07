"""
He's a bear he's a bear he's a big ol' bear

if your looking for documentation,
i wrote a bit in state_handler.py
"""
from src.state_machines.state_handler import StateHandler

state_over = lambda player: player.frame >= player.state_data[player.state][0]
player_actionable = lambda player: player.frame >= player.state_data[player.state][1]

JUMP_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching_0", "punching_1", "jumpattackstart", "jumpattack", "HIT", "KNOCKDOWN"]
PUNCH_STATE_BLACKLIST = ["jumpstart", "jumping", "landing", "punchstart", "punching_0", "punching_1", "jumpattackstart", "jumpattack", "run", "HIT", "KNOCKDOWN"]

initstates = [
    [ lambda player: player.state == "idle" and any([player.MOV_LEFT, player.MOV_RIGHT, player.MOV_UP, player.MOV_DOWN]) and not player.flag,
      """
      fi direction= -1 if P:MOV_LEFT
      fi direction= 1 if P:MOV_RIGHT
      state= walk frame= 0 speed= P:walk_speed
      """
    ],
    
    [ lambda player: player.state in ["walk", "run"] and not any([player.MOV_LEFT, player.MOV_RIGHT, player.MOV_UP, player.MOV_DOWN]),
      """
      state= idle frame= 0 flag= 1
      """
    ],
    [ lambda player: player.state == "idle" and any([player.MOV_LEFT, player.MOV_RIGHT, player.MOV_UP, player.MOV_DOWN]) and player.flag,
      """
      fi direction= -1 if P:MOV_LEFT
      fi direction= 1 if P:MOV_RIGHT
      state= run frame= 0 speed= P:run_speed flag= 0
      """
    ],
    [ lambda player: player.BTN_0 and player.state not in JUMP_STATE_BLACKLIST,
      """
      state= jumpstart frame= 0
      fi jump_direction= 0 if not
      fi jump_direction= - P:MOV_RIGHT P:MOV_LEFT dup or == P:state walk == P:state run
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
      state= punching_0 frame= 0 flag= 0
      """
    ],

    [ lambda player: player.state == "punching_0" and state_over(player),
      """
      state= punching_1 frame= 0
      """
    ],

    [ lambda player: player.state  == "punching_1" and state_over(player),
      """
      state= idle frame= 0
      """
    ],

    [ lambda player: player.state == "HIT" and state_over(player),
      """
      fi state= idle if not
      fi state= jumping if dup != P:y 0
      . P:y . out_of_hitstun
      frame= 0
      """
    ],
    [ lambda player: player.state == "KNOCKDOWN" and state_over(player),
      """
      fi state= idle if not
      fi state= jumping if dup == P:y 0
      frame= 0
      """
    ]
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
    fi flag= 0 if >= P:frame 2
    """,
    "run":  """
    fi direction= -1 x= - P:x P:speed if P:MOV_LEFT
    fi direction= 1 x= + P:x P:speed if P:MOV_RIGHT
    fi z= 0 if < P:z 0
    fi z= 100 if > P:z 100
    fi z= + P:z 1 if P:MOV_UP
    fi z= - P:z 1 if P:MOV_DOWN
    fi frame= 0 if == P:frame 11
    fi flag= 0 if >= P:frame 2
    """, 
    "idle": """
    fi flag= 0 if >= P:frame 2
    """,
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
    "KNOCKDOWN":"""
    x= + P:x * * 2 P:speed P:direction
    """,
}

def get_state_handler(player):
    return StateHandler(player,
                        initstates=initstates,
                        applystates=applystates)
