from functools import wraps
from ..assets.colors import C
from ..character import inventory_menu
from .. import player


class InventoryInterrupt(Exception):
    pass

def retry_on_inventory(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except InventoryInterrupt:
                return
    return wrapper

def choice(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'inv':
            inventory_menu(player.char)
            return None
        return user_input.lower()
