from .assets.data import VISITED_PLACES_DEFAULT
from .assets.colors import C
from .utils.helpers import retry_on_inventory, choice
from .utils.game_logs import damage, heal, add_item, remove_item, equip_item, item_unequipped, head
from .character import stat, inv, bonus, display_stats

visited_places = VISITED_PLACES_DEFAULT.copy()

#GAME FLOW
@retry_on_inventory
def main_choice_loop():
    while True:
        head('dev message')
        print(F"{C.BLUE}Welcome to the beta of THE VILLAGE!")
        print(F"{C.BLUE}This is a text-based adventure game where your choices shape the story.")
        head('question')
        char = choice(f"{C.MAGENTA}First, what is your character's first name? {C.NORMAL}").lower().capitalize()
        head('narrator')
        print(f"You are {C.MAGENTA}{char}{C.NORMAL}, a 19-year-old who lives in a village that is {C.RED}connected to the outside world by a famous crossroads.")
        print(F"Your parents are local farmers, {C.RED}Robert {C.NORMAL}and {C.RED}Martha{C.NORMAL}. They are {C.RED}children of the village founders{C.NORMAL}. You have no brothers or sisters.")
        print("You wake up in your bed, the sun is rising at your window. And with that, the sound of the students passing by your house.")
        print(f"On your nightstand you have your {C.YELLOW}favorite shirt{C.NORMAL}, you keep it in your inventory")
        head('question')
        print("What do you want to do?")
        print("1. Go downstairs.")
        print("2. Look at the window.")
        print("3. Look around your room.")
        MainChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if MainChoice == "1":
            head('narrator')
            print("You get on your feet, put on your slippers, and start to go downstairs.")
            print("As you start to see someone making something in the kitchen, someone else calls you.")
            damage(char, 101, "standing up too quickly")
            heal(char, 5, "morning stretch")
            add_item(char, "Well-used dark tanktop")
            remove_item(char, "Well-used dark tanktop")
            add_item(char, "Well-used dark tanktop")
            equip_item(char, "Well-used dark tanktop")
            item_unequipped(char, "Well-used dark tanktop", bonus)
            print()
            print("???: ETHAN, COME HERE, YOU LITTLE PRICK BASTARD!")
            print()
            print("As you step closer, you recognize the voice, it's your old dad, Robert.")
            print("ROBERT_ART")
            print("He stares at you with anger, his face red and his eyes full of rage.")
            break

        elif MainChoice == "2":
            look_window_choice()

        elif MainChoice == "3":
            look_room_choice()

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

@retry_on_inventory
def look_window_choice():
    if visited_places['window']['visited']:
        print("You already looked through the window and saw everything interesting.")
        print()
        return
    
    print("As you approach the window...\n")
    while True:
        print(f"You can see several interesting places, like a {C.YELLOW}stable{C.NORMAL}, a {C.YELLOW}rusty playground{C.NORMAL}, and a {C.YELLOW}big building{C.NORMAL}.")
        print()
        print()
        print("what will you focus on?")
        print("1. Big building.")
        print("2. Rusty playground.")
        print("3. Stable.")
        print("4. Return to bed.")
        LookChoice = choice(F"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
        print()

        if LookChoice == "1":
            if visited_places['window']['big_building_seen']:
                print("You already looked at the big building and saw everything interesting.")
                print()
                continue
            print(f"Looking at the big building you can see some workman's doing their job, something calls you attention, {C.YELLOW}a group of teenagers are mistreating a cat{C.NORMAL}.")
            visited_places['window']['big_building_seen'] = True
            print("You step back from the window.")
            print()
        elif LookChoice == "2":
            if visited_places['window']['rusty_playground_seen']:
                print("You already looked at the rusty playground and saw everything interesting.")
                print()
                continue
            print(f"Looking at the rusty playground, you can see some kids playing there, something calls your attention, {C.YELLOW}a group of kids is practicing bullying against a kid with glasses{C.NORMAL}.")
            visited_places['window']['rusty_playground_seen'] = True
            print("You step back from the window.")
            print()
        elif LookChoice == "3":
            if visited_places['window']['stable_seen']:
                print("You already looked at the stable and saw everything interesting.")
                print()
                continue
            print(f"Looking at the stable you, can see some horses and chickens, besides it, {C.YELLOW}a red hair girl{C.NORMAL} calls your attention, she is taking care of the horses.")
            visited_places['window']['stable_seen'] = True
            print("You step back from the window.")
            print()
        elif LookChoice == "4":
            print("You step back from the window and return to your bed.")
            print()
            print()
            return
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3 or 4.")
        
        if (
            visited_places['window']['big_building_seen'] and
            visited_places['window']['rusty_playground_seen'] and
            visited_places['window']['stable_seen']
        ):
            visited_places['window']['visited'] = True
            print("After spending a while looking outside, you realize there’s nothing new to see.\n")
            return

@retry_on_inventory
def look_room_choice():
    print("As you look around your room...\n")
    while True:
        if visited_places['wardrobe']['visited'] and visited_places['under_bed']['visited'] and visited_places['shelves']['visited']:
            print("You already looked all around your room and found everything interesting.")
            print()
            return
        
        print(f"You can see several interesting locals, like a {C.YELLOW}wardrobe{C.NORMAL}, {C.YELLOW}some shelves{C.NORMAL} and {C.YELLOW}under your bed{C.NORMAL}.")
        print()
        print()
        print("What will you search?")
        print("1. Wardrobe.")
        print("2. Under your bed.")
        print("3. Some shelves.")
        print("4. Return to bed")
        SearchChoice = choice(F"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
        print()

        if SearchChoice == "1":
            wardrobe_choice()
        elif SearchChoice == "2":
            under_bed_choice()
        elif SearchChoice == "3":
            shelves_choice()
        elif SearchChoice == "4":
            return
        else:
            print(F"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3, or 4.")

@retry_on_inventory
def wardrobe_choice():
    CLOTHES_ITEMS = ["Favorite long-sleeve shirt", "Well-used dark tanktop", "Good-looking blazer"]

    if visited_places['wardrobe']['visited']:
        print("You already searched the wardrobe and found everything interesting.")
        print()
        return

    while True:
        if visited_places['wardrobe']['broken_door']:
            print("You are in front of your wardrobe wide open.")
            print("What will you do?")
            print("1. Check inside wardrobe.")
            print("2. Leave it there.")
            print("3. Check wood pile.")
        else:
            print("The wardrobe door is stuck, but you can try to force it open.")
            print("What will you do?")
            print("1. Break the door and check inside wardrobe.")
            print("2. Leave it there.")

        WardrobeChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
        print()

        if WardrobeChoice == "1":
            if visited_places['wardrobe']['broken_door']:
                print("You dodge the pile of wood")
            else:
                visited_places['wardrobe']['broken_door'] = True
                print("You force the wardrobe door open with all your strength.")
                print(f"The broken door collapses to the ground in a second, it is a {C.YELLOW}pile of wood now{C.NORMAL}.")
            print()
            print(f"Inside the wardrobe theres is a {C.YELLOW}collection of old and dusty clothes{C.NORMAL}.")
            print()
            print()

            while True:
                if visited_places['wardrobe']['w_u_d_tanktop_taken'] and visited_places['wardrobe']['g_l_blazer_taken']:
                    visited_places['wardrobe']['visited'] = True
                    print("You already took all the clothes from the wardrobe.")
                    print()
                    return
                
                print("What will you do?")
                print("1. Take the well-used dark tanktop.")
                print("2. Take the good-looking blazer.")
                print("3. Take nothing and leave.")
                ClothesChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
                print()

                if ClothesChoice == "1":
                    if visited_places['wardrobe']['w_u_d_tanktop_taken']:
                        print("You already took the well-used dark tanktop from the wardrobe.")
                        print()
                        return
                    visited_places['wardrobe']['w_u_d_tanktop_taken'] = True
                    inv.append("Well-used dark tanktop")
                    print("You took the well-used dark tanktop from the wardrobe.")
                    print()
                    display_stats()
                    print()
                    return
                elif ClothesChoice == "2":
                    if visited_places['wardrobe']['g_l_blazer_taken']:
                        print("You already took the good-looking blazer from the wardrobe.")
                        print()
                        return
                    visited_places['wardrobe']['g_l_blazer_taken'] = True
                    inv.append("Good-looking blazer")
                    print("You took the good-looking blazer from the wardrobe.")
                    print()
                    display_stats()
                    print()
                    return
                elif ClothesChoice == "3":
                    print("You left the wardrobe without taking any clothes.")
                    print()
                    return
                else:
                    print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2 or 3.")
                    print()

        elif WardrobeChoice == "2":
            print("You decide to leave the wardrobe alone for now.")
            print()
            return
        elif WardrobeChoice == "3":
            inv.append("wood plank")
            print("You check the wood pile and take a wood plank from it.")
            print()
            display_stats()
            print()
            return
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1 or 2.")
            print()

@retry_on_inventory
def under_bed_choice():
    if visited_places['under_bed']['visited']:
        print("You already searched under your bed and found nothing else.")
        print()
        return
    
    while True:
        print(F"As you move your neck to see under your bed, {C.RED}your neck hurts{C.NORMAL}. Passing your hand over it, {C.RED}you notice a bruise{C.NORMAL}. Touching it make it hurt worsen.")
        print()
        print()
        print("You processed to see under the bed?")
        print("1. Yes.")
        print("2. No.")
        BedChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
        print()

        if BedChoice == "1":
            stat['hp'] -= 10
            print("As your move your head under the bed, your neck hurt but you ignores it.")
            print()
            print(f"{C.RED}You lose 10 HP{C.NORMAL}. You current HP is {stat['hp']}.")
            print()
            print(f"There, on the botton of your mattress, {C.YELLOW}you notices something dark{C.NORMAL}.")
            print()
            print()

            while True:
                print("You move your head closer?")
                print("1. Yes.")
                print("2. No.")
                SecondBedChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
                print()

                if SecondBedChoice == "1":
                    stat['hp'] -= 20
                    print("As you move your head closer, your neck hurt more.")
                    print()
                    print(f"{C.RED}You lose 20 HP{C.NORMAL}. You current HP is {stat['hp']}")
                    print()
                    inv.append("Blooded Rusty Knife")
                    print(f"But then, you find out the dark thing was a {C.YELLOW}blooded rusty knife{C.NORMAL}.")
                    print()
                    print("You took it and leave the botton of your bed.")
                    print()

                    
                    visited_places['under_bed']['visited'] = True 
                    visited_places['under_bed']['knife_taken'] = True
                    return
                

                elif SecondBedChoice == "2":
                    print("You decide the pain isn't worth it and pull your head out.")
                    print()
                    return
                else:
                    print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")



        elif BedChoice == "2":
            print("Deciding it's not worth the pain, you lay back down.")
            print()
            return

        else:
            print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")
            print()

@retry_on_inventory
def shelves_choice():
    if visited_places['shelves']['visited']:
        print("You already searched the shelves and found nothing else.")
        print()
        return
    
    while True:
        print("As you pass by some books and others trinkets you've stash in there, you notice some interesting ones.")
        print()
        print(f"In the red shelve there are a {C.YELLOW}key with a feather attached{C.NORMAL} and a {C.YELLOW}hair clip{C.NORMAL}.")
        print("This shelve is way too high to reach it normally, so you grab a wooden stool to reach it.")
        print()
        print()
        print("What will you took?")
        print("1. Key with feather attached.")
        print("2. Hair clip.")
        print("3. Leave the shelf alone.")
        ShelvesChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
        print()

        if ShelvesChoice == "1":
            if visited_places['shelves']['key_taken']:
                print("You already took the Key with feather attached from the shelves.")
                print()
            else:
                visited_places['shelves']['key_taken'] = True
                inv.append("Key with Feather Attached")
                print(f"You took the {C.YELLOW}Key with feather attached{C.NORMAL}.")
            print()
            display_stats()
            print()
            print(f"You will try to catch the {C.YELLOW}Hair Clip{C.NORMAL}?")
            print("1. Yes.")
            print("2. No.")
            StoolChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
            print()

            if StoolChoice == "1":
                if visited_places['shelves']['hair_clip_taken']:
                    print("You already took the Hair clip from the shelves.")
                    print()
                else:
                    visited_places['shelves']['hair_clip_taken'] = True
                    inv.append("Hair Clip")
                    print(f"You took the {C.YELLOW}Hair clip{C.NORMAL}.")
                print()
                print("But as you try to get down, the stool breaks and you fall to the ground.")
                print()
                stat['hp'] -= 15
                print(f"{C.RED}You lose 15 HP{C.NORMAL}. You current HP is {stat['hp']}.")
                print()
                display_stats()
                print()
                print("You get up and leave the shelf.")
                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    print("You took all the interesting items from the shelves.")
                    print()
                return
            
            elif StoolChoice == "2":
                print("You decide to leave the hair clip there.")
                print()
                return
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")
                print()

        elif ShelvesChoice == "2":
            if visited_places['shelves']['hair_clip_taken']:
                print("You already took the Hair clip from the shelves.")
                print()
            else:
                visited_places['shelves']['hair_clip_taken'] = True
                inv.append("Hair Clip")
                print(f"You took the {C.YELLOW}Hair clip{C.NORMAL}.")
            print()
            display_stats()
            print()
            print(f"You will try to catch the {C.YELLOW}Key with feather attached{C.NORMAL}?")
            print("1. Yes.")
            print("2. No.")
            StoolChoice = choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")
            print()

            if StoolChoice == "1":
                if visited_places['shelves']['key_taken']:
                    print("You already took the Key with feather attached from the shelves.")
                    print()
                else:
                    visited_places['shelves']['key_taken'] = True
                    inv.append("Key with feather attached")
                    print(f"You took the {C.YELLOW}Key with feather attached{C.NORMAL}.")
                print()
                print("But as you try to get down, the stool breaks and you fall to the ground.")
                print()
                stat['hp'] -= 15
                print(f"{C.RED}You lose 15 HP{C.NORMAL}. You current HP is {stat['hp']}.")
                print()
                display_stats()
                print()
                print("You get up and leave the shelf.")
                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    print("You took all the interesting items from the shelves.")
                    print()
                return
            elif StoolChoice == "2":
                print("You decide to leave the Key with feather attached there.")
                print()
                return
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")
                print()

        elif ShelvesChoice == "3":
            print("You decide to leave the items where they are.")
            print()
            return
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, or 3.")
            print()

main_choice_loop()