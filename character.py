from .core import stat_b, inv_b, bonus_b, C
stat = stat_b.copy()
inv = inv_b.copy()
bonus = bonus_b.copy()

# Calculate bonuses from inventory
def calc_bonuses(stat_name):
    total_bonus = 0

    for item in inv:
        if item in bonus:
            info = bonus[item]
            if info.get('is_equipped', False) and stat_name in info:
                total_bonus += info[stat_name]

    return total_bonus

# Get total stat including bonuses
def get_total(stat_name):
    return stat[stat_name] + calc_bonuses(stat_name)

# Determine color based on value
def state(value):
    if value > 0:
        return C.GREEN
    elif value < 0:
        return C.RED
    else:
        return C.NORMAL

# Display character stats
def display_stats():
    print(f"--- {C.YELLOW}Char's Stats{C.NORMAL} ---")

    print(f"HP: {stat['hp']}")
    stats_to_display = ['charisma', 'bravery', 'intimidation']

    for stat in stats_to_display:
        base_val = stat[stat]
        bonus = calc_bonuses(stat)
        total = base_val + bonus
        color = state(total)
        print(f"{stat.capitalize()}: {color}{total}{C.NORMAL} (Base: {base_val}, Bonus: {bonus})")

    if inv:
        print("Inventory:")
        for item in inv:
            info = bonus.get(item, {})
            is_equipped = info.get('is_equipped', False)
            equipped_tag = f"{C.GREEN} (Equipped){C.NORMAL}" if is_equipped else ""
            bonus_list = [f"{'+' if v>0 else ''}{v} {k.capitalize()}"
                          for k,v in info.items() if k not in ['is_equipped'] and v != 0]
            bonus_str = f" ({', '.join(bonus_list)})" if bonus_list else ""
            print(f" - {item}{equipped_tag}{bonus_str}")
    else:
        print("Inventory: (Empty)")


def inventory_menu():
    while True:
        print()
        print(f"--- {C.YELLOW}Inventory{C.NORMAL} ---")
        print("1. Left inventory.")
        print("2. See general items.")
        print("3. See equippable items.")
        inv_choice = input("Enter the number of your choice: ")
        print()

        if inv_choice == "1":
            return

        elif inv_choice == "2":
            general_items = [item for item in inv if not bonus.get(item, {}).get('is_equippable', False)]

            if general_items:
                print("Your general items:")
                for item in general_items:
                    print(f" - {item}")
            else:
                print("Your have no general items.")

        elif inv_choice == "3":
            equippable_items = [item for item in inv if bonus.get(item, {}).get('is_equippable', False)]

            if equippable_items:
                print("Your equippable items:")
                for item in equippable_items:
                    is_equipped = bonus[item].get('is_equipped', False)
                    equipped_tag = f"{C.GREEN} (Equipped){C.NORMAL}" if is_equipped else ""
                    print(f" - {item}{equipped_tag}")

                print()
                print("To equip an item, type its name.")
                print("To desequip an item, type 'unequip <body_part>' (e.g., 'unequip torso').")
                print("Type 'no' to return to the menu.")
                equip_choice = input("Enter your choice: ").strip()
                if equip_choice.lower() == 'no':
                    continue

                if equip_choice.lower().startswith("unequip"):
                    parts = equip_choice.split()
                    if len(parts) == 2:
                        body_part = parts[1].lower()
                        found = False
                        for item_name in equippable_items:
                            if bonus[item_name]['body_part'].lower() == body_part:
                                bonus[item_name]['is_equipped'] = False
                                found = True
                        if found:
                            print(f"All items in {body_part} are now unequipped.")
                        else:
                            print(f"{C.RED}No equipped items found in {body_part}.{C.NORMAL}")
                    else:
                        print(f"{C.RED}Invalid format. Use 'unequip <body_part>'.{C.NORMAL}")
                    continue

                equipped_item_name = next(
                    (item_name for item_name in equippable_items if item_name.lower() == equip_choice.lower()),
                    None
                )

                if equipped_item_name:
                    body_part = bonus[equipped_item_name]['body_part']
                    for item_name in equippable_items:
                        if bonus[item_name]['body_part'] == body_part:
                            bonus[item_name]['is_equipped'] = False

                    bonus[equipped_item_name]['is_equipped'] = True
                    print(f"You have equipped the {equipped_item_name}.")
                else:
                    print(f"{C.RED}Item not found or name typed incorrectly.{C.NORMAL}")
            else:
                print("You have no equippable items.")

        else:
            print(f"{C.RED}Invalid choice! Please enter a valid number.{C.NORMAL}")

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