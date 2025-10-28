from .core import C
from .assets.data import inv, bonus, stat
from .utils.game_logs import head
from . import player


def set_char():
    global char
    player.char = input(f"{C.MAGENTA}First, what is your character's first name? {C.NORMAL}").lower().capitalize()

def calc_bonuses():
    all_bonuses = {} 
    except_keys = ['is_equipped', 'body_part']

    for item in inv:
        if item in bonus:
            info = bonus[item]
            if info.get('is_equipped', False):
                
                for stat_name, bonus_value in info.items():
                    if stat_name not in except_keys:
                        if isinstance(bonus_value, (float, int)):
                            all_bonuses[stat_name] = all_bonuses.get(stat_name, 0) + bonus_value
                        else:
                            pass
    return all_bonuses

# Get total stat including bonuses
def get_total(stat_name):
    return stat[stat_name] + calc_bonuses(stat_name)

def state(value):
    if value > 0:
        return C.GREEN
    elif value < 0:
        return C.RED
    else:
        return C.NORMAL

def hp_state(value):
    if value > 75:
        return C.GREEN
    elif value > 50:
        return C.YELLOW
    else:
        return C.RED



# Display character stats
def display_stats(char):
    head(f"{char} stats")
    all_bonuses = calc_bonuses()
    for atribute in stat:
        atribute_val = stat[atribute]
        atribute_bonus = all_bonuses.get(atribute, 0)
        atribute_now = atribute_val + atribute_bonus
        if atribute != 'hp':
            color = state(atribute_now)
            print(f"{atribute}: {color}{atribute_now}{C.NORMAL}")
        else:
            color = hp_state(atribute_now)
            print(f"{atribute}: {color}{atribute_now}{C.NORMAL}")

def inventory_menu(char):
    while True:
        head(f"{char} inventory")
        print("'left' to leave the inventory.")
        print("2. See general items.")
        print("3. See equippable items.")
        inv_choice = input(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}").strip()

        if inv_choice == "left":
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