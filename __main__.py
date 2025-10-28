from colorama import init
init(autoreset=True)

def start_game():
    from .places import main_choice_loop

    main_choice_loop()

start_game()