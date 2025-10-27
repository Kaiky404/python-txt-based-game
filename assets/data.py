DEFAULT_ATRIBUTES = { 
    "hp": 100,
    "charisma": 0,
    "bravery": 0,
    "intimidation": 0
}

DEFAULT_INVENTORY = ["Favorite long-sleeve shirt"]

ITEM_BONUSES = { 
    "Favorite long-sleeve shirt": {
        "charisma": -1,
        "bravery": 1,
        "intimidation": -1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "Well-used dark tanktop": {
        "charisma": -1,
        "bravery": 0,
        "intimidation": 1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "Good-looking blazer": {
        "charisma": 1,
        "bravery": 0,
        "intimidation": -1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "Rusty kitchen knife": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 1,
        "body_part": "hand",
        "is_equippable": True,
        "is_equipped": False
    },
    "Hair clip": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 0,
        "body_part": "none",
        "is_equippable": False,
        "is_equipped": False
    },
    "Key with a feather attached": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 0,
        "body_part": "none",
        "is_equippable": False,
        "is_equipped": False
    },
    "Wood plank": {
        "charisma": 0,
        "bravery": 1,
        "intimidation": 0,
        "body_part": "hand",
        "is_equippable": True,
        "is_equipped": False
    }
}

VISITED_PLACES_DEFAULT = {
    "wardrobe": {
        "visited": False,
        "broken_door": False,
        "w_u_d_tanktop_taken": False,
        "g_l_blazer_taken": False
    },
    "under_bed": {
        "visited": False,
        "knife_taken": False
    },
    "shelves": {
        "visited": False,
        "hair_clip_taken": False,
        "key_taken": False
    },
    "window": {
        "visited": False,
        "big_building_seen": False,
        "rusty_playground_seen": False,
        "stable_seen": False
    }
}