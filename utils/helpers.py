from functools import wraps
from ..assets.colors import C
from ..character import inventory_menu

# custom exception for inventory interrupt - allows me to use try/catch for interrupting input flow without breaking the code
class InventoryInterrupt(Exception):
    pass

# func is the def we want to decorate and protect against inventory interrupts
# it turns any function able to handle inventory interrupts
def retry_on_inventory(func):

    # import wraps to preserve function metadata
    from functools import wraps
    @wraps(func)

    # def wrapper is like the main_choice_loop, look_window_choice, etc, it has their name and shit
    # so when we call main_choice_loop, we are actually calling wrapper, the args and kwargs are like the 1, 2 etc choices
    # so if "inv" is typed, InventoryInterrupt is raised, so it's like opening the inventory menu of the def inventory_menu()
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except InventoryInterrupt:
                continue
    return wrapper

# this swap places with input() to handle inventory interrupts
def choice(prompt):
    """
    Show the prompt and get user input.

    If the user inputs 'inv', opens the inventory menu and restarts the function.
    Returns the input in lowercase.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'inv':
            # opens the inventory menu and raises the interrupt to warn the decorator - "the inventory was opened,
            # and thats why the choice the player was making was interrupted"
            inventory_menu()
            raise InventoryInterrupt()
        
        # else, return player input normally
        return user_input.lower()