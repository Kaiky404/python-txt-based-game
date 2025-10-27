from colorama import init
init(autoreset=True)

from .utils.helpers import choice
from .assets.colors import C

def start_game():
    from .places import main_choice_loop

    main_choice_loop()


start_game()