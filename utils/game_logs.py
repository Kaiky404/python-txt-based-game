from ..assets.colors import C
from ..character import inv, stat, bonus

def head(type: str):
        print("\n------------------------------------------------------------")
        print(f"[{type.upper()}]\n")

def damage(char, amount: int, reason: str):
    head('damage')
    stat['hp'] -= amount
    if stat['hp'] <= 0:
        stat['hp'] = 0
        print(f"{char} take {amount} damage for {reason}")
        print(f"{char} died")
    else:
        print(f"{char} took {amount} damage for {reason}")
        print(f"{char} current have {stat['hp']} HP")

def heal(char, amount, reason):
    head('heal')
    stat['hp'] += amount
    print(f"{char} healed {amount} hp for {reason}")
    print(f"{char} currently has {stat['hp']} HP")

def add_item(char, item):
    head('item added')
    inv.append(item)
    print(f"{char} obtained {item}")

def remove_item(char, item):
    if item in inv:
        head('item removed')
        inv.remove(item)
        print(f"{char} discarded {item}")
    else:
        print(f"{char} don't have {item} in inventory")

def equip_item(char, item):
    if item in bonus:
        head('item equipped')
        bonus[item]['is_equipped'] = True
        bonus_output = "Item bonuses: \n"

        for key, value in bonus[item].items():
            if key in ('is_equipped', 'is_equippable'):
                continue

            line = ""
            if value:
                if isinstance(value, (int, float)):
                    if value > 0:
                        line = f"- {key}: +{value}\n"
                    else:
                        line = f"- {key}: {value}\n"
                elif isinstance(value, str):
                    if key == 'body_part':
                        line = f"- Body part: {value}"
            bonus_output += line
        print(f"{char} has equipped {item}")
        print(bonus_output)
    else:
        print(f"{char} don't have {item} in inventory")

def item_unequipped(char, item, bonus):
    if item in bonus:  
        head('item unequipped')
        bonus[item]['is_equipped'] = False
        bonus_output = "Item bonuses: \n"

        for key, value in bonus[item].items():
            if key in ('is_equipped', 'is_equippable'):
                continue

            line = ""
            if value:
                if isinstance(value, (int, float)):
                    if value > 0:
                        line = f"- {key}: +{value}\n"
                    else:
                        line = f"- {key}: {value}\n"
                elif isinstance(value, str):
                    if key == 'body_part':
                        line = f"- Body part: {value}"
            bonus_output += line
        print(f"{char} has unequipped {item}")
        print(bonus_output)
    else:
        print(f"Error: Item '{item}' not found in bonuses.")