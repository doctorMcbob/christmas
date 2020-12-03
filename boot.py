"""
Christmas Beat em up
working title:
"The day the whales stole christmas"
"A Bunch Of Animals Kill Santa"
"""
import sys
from src.game import setup, run_game


if __name__ == """__main__""":
    game_state = setup(fullscreen="-f" in sys.argv)
    run_game(game_state)
