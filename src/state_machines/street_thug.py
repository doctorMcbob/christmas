from src.state_machines.state_handler import StateHandler

state_over = lambda peice: peice.frame >= peice.state_data[peice.state][0]

initstates = [
    [ lambda peice: peice.state == "idle",
      """
      """
    ],
]

applystates = {

}

def get_state_handler(obj):
    return StateHandler(obj,
                        initstates=initstates,
                        applystates=applystates)
