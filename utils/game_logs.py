from ..assets.colors import C
from time import sleep
from ..character import inv, stat, bonus
import re
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def formatting(action, amount = None, unit = '', reason = None, obs = ''):
    amount_and_unit = f" {amount} {unit}" if amount is not None else f"{unit}"
    text = f"You {action}{amount_and_unit}!"
    if reason is not None and reason != '':
        text += f" for {reason}"

    lenght = len(ansi_escape.sub('', text))
    line = '-' * lenght

    print("\n--" + line)
    print(" " + text)
    if obs:
        print(" " + obs)
    print(line + "--\n")
    sleep(0.5)

def damage(amount, reason):
    stat['hp'] -= amount
    act = "take"
    unit = "damage"
    if stat['hp'] <= 0:
        stat['hp'] = 0
        obs = f"You died!"
    else:
        obs = f"Your current HP is now: {stat['hp']} HP"
    formatting(act, amount, unit, reason, obs)

def heal(amount, reason):
    stat['hp'] += amount
    act = "heal"
    unit = "HP"
    obs = f"Your current HP is now: {stat['hp']} HP"
    formatting(act, amount, unit, reason, obs)

def add_item(item):
    inv.append(item)
    act = "have acquired "
    formatting(
        action = act,
        unit = f"one {item}"
    )

def remove_item(item):
    if item in inv:
        inv.remove(item)
        act = "have lost: "
        formatting(
            action = act,
            unit = f"one {item}"
        )
    else:
        print(f"Error: Item '{item}' not found in inventory.")

def equip_item(item):
    if item in bonus:
        bonus[item]['is_equipped'] = True
        bonus_output = "Item stats: \n"

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
               
        act = "have equipped "
        formatting(
            action = act,
            unit = f"one {item}",
            obs = bonus_output
            )         
    else:
        print(f"Error: Item '{item}' not found in bonuses.")

def item_unequipped(item, bonus):
    if item in bonus:
        bonus[item]['is_equipped'] = False
        bonus_output = "Item stats: \n"

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
               
        act = "have unequipped "
        formatting(
            action = act,
            unit = f"one {item}",
            obs = bonus_output
            )         
    else:
        print(f"Error: Item '{item}' not found in bonuses.")

def head(type: str):
    if type in ['question']:
        print("------------------------------------------------------------\n")
        print(f"[{type.upper()}]")
    else:
        print("\n------------------------------------------------------------")
        print(f"[{type.upper()}]")