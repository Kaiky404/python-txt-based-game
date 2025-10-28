DEFAULT_ATRIBUTES = { 
    "hp": 100,
    "charisma": 0,
    "bravery": 0,
    "intimidation": 0
}

DEFAULT_INVENTORY = ["favorite long-sleeve shirt"]

ITEM_BONUSES = { 
    "favorite long-sleeve shirt": {
        "charisma": -1,
        "bravery": 1,
        "intimidation": -1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "well-used dark tanktop": {
        "charisma": -1,
        "bravery": 0,
        "intimidation": 1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "good-looking blazer": {
        "charisma": 1,
        "bravery": 0,
        "intimidation": -1,
        "body_part": "torso",
        "is_equippable": True,
        "is_equipped": False
    },
    "rusty kitchen knife": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 1,
        "body_part": "hand",
        "is_equippable": True,
        "is_equipped": False
    },
    "hair clip": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 0,
        "body_part": "none",
        "is_equippable": False,
        "is_equipped": False
    },
    "key with a feather attached": {
        "charisma": 0,
        "bravery": 0,
        "intimidation": 0,
        "body_part": "none",
        "is_equippable": False,
        "is_equipped": False
    },
    "wood plank": {
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