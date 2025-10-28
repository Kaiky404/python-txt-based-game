from .core import C, helpers, game_logs, visited_places


#GAME FLOW
@helpers.retry_on_inventory
def main_choice_loop():
    game_logs.head('dev message')
    print(F"{C.BLUE}Welcome to the beta of THE VILLAGE!")
    print(F"{C.BLUE}This is a text-based adventure game where your choices shape the story.")

    game_logs.head('question')
    char = helpers.choice(f"{C.MAGENTA}First, what is your character's first name? {C.NORMAL}").lower().capitalize()

    game_logs.head('narrator')
    print(f"You are {C.MAGENTA}{char}{C.NORMAL}, a 19-year-old who lives in a village that is {C.RED}connected to the outside world by a famous crossroads.")
    print(F"Your parents are local farmers, {C.RED}Robert {C.NORMAL}and {C.RED}Martha{C.NORMAL}. They are {C.RED}children of the village founders{C.NORMAL}. You have no brothers or sisters.")
    print("You wake up in your bed, the sun is rising at your window. And with that, the sound of the students passing by your house.")
    print(f"On your nightstand you have your {C.YELLOW}favorite shirt{C.NORMAL}, you keep it in your inventory")
    while True:
        game_logs.head('question')
        print("What do you want to do?")
        print("1. Go downstairs.")
        print("2. Look at the window.")
        print("3. Look around your room.")
        MainChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if MainChoice == "1":
            game_logs.head('narrator')
            print("You get on your feet, put on your slippers, and start to go downstairs.")
            print("As you start to see someone making something in the kitchen, someone else calls you.")
            print("???: ETHAN, COME HERE, YOU LITTLE PRICK BASTARD!")
            print("As you step closer, you recognize the voice, it's your old dad, Robert.")
            print("ROBERT_ART")
            print("He stares at you with anger, his face red and his eyes full of rage.")
            break

        elif MainChoice == "2":
            look_window_choice()

        elif MainChoice == "3":
            look_room_choice(char)

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

@helpers.retry_on_inventory
def look_window_choice():
    if visited_places['window']['visited']:
        game_logs.head('info')
        print("You already looked through the window and saw everything interesting.")
        return
    
    game_logs.head('narrator')
    print("As you approach the window...")
    while True:
        print(f"You can see several interesting places, like a {C.YELLOW}stable{C.NORMAL}, a {C.YELLOW}rusty playground{C.NORMAL}, and a {C.YELLOW}big building{C.NORMAL}.")
        
        game_logs.head('question')
        print("what will you focus on?")
        print("1. Big building.")
        print("2. Rusty playground.")
        print("3. Stable.")
        print("4. Return to bed.")
        LookChoice = helpers.choice(F"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if LookChoice == "1":
            if visited_places['window']['big_building_seen']:
                game_logs.head('info')
                print("You already looked at the big building and saw everything interesting.")
                continue

            visited_places['window']['big_building_seen'] = True
            game_logs.head('narrator')
            print(f"Looking at the big building you can see some workman's doing their job, something calls you attention, {C.YELLOW}a group of teenagers are mistreating a cat{C.NORMAL}.")
            print("You step back from the window.")

        elif LookChoice == "2":
            if visited_places['window']['rusty_playground_seen']:
                game_logs.head('info')
                print("You already looked at the rusty playground and saw everything interesting.")
                continue

            visited_places['window']['rusty_playground_seen'] = True
            game_logs.head('narrator')
            print(f"Looking at the rusty playground, you can see some kids playing there, something calls your attention, {C.YELLOW}a group of kids is practicing bullying against a kid with glasses{C.NORMAL}.")
            print("You step back from the window.")

        elif LookChoice == "3":
            if visited_places['window']['stable_seen']:
                game_logs.head('info')
                print("You already looked at the stable and saw everything interesting.")
                continue
            
            visited_places['window']['stable_seen'] = True
            game_logs.head('narrator')
            print(f"Looking at the stable you, can see some horses and chickens, besides it, {C.YELLOW}a red hair girl{C.NORMAL} calls your attention, she is taking care of the horses.")
            print("You step back from the window.")

        elif LookChoice == "4":
            game_logs.head('narrator')
            print("You step back from the window and return to your bed.")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3 or 4.")
        
        if (
            visited_places['window']['big_building_seen'] and
            visited_places['window']['rusty_playground_seen'] and
            visited_places['window']['stable_seen']
        ):
            visited_places['window']['visited'] = True
            game_logs.head('info')
            print("After spending a while looking outside, you realize there’s nothing new to see.")
            return

@helpers.retry_on_inventory
def look_room_choice(char):
    while True:
        if visited_places['wardrobe']['visited'] and visited_places['under_bed']['visited'] and visited_places['shelves']['visited']:
            game_logs.head('info')
            print("You already looked all around your room and found everything interesting.")
            return
        
        game_logs.head('narrator')
        print("As you look around your room...")
        print(f"You can see several interesting locals, like a {C.YELLOW}wardrobe{C.NORMAL}, {C.YELLOW}some shelves{C.NORMAL} and {C.YELLOW}under your bed{C.NORMAL}.")

        game_logs.head('question')
        print("What will you search?")
        print("1. Wardrobe.")
        print("2. Under your bed.")
        print("3. Some shelves.")
        print("4. Return to bed")
        SearchChoice = helpers.choice(F"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if SearchChoice == "1":
            wardrobe_choice(char)
        elif SearchChoice == "2":
            under_bed_choice(char)
        elif SearchChoice == "3":
            shelves_choice(char)
        elif SearchChoice == "4":
            return
        else:
            print(F"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, 3, or 4.")

@helpers.retry_on_inventory
def wardrobe_choice(char):
    CLOTHES_ITEMS = ["favorite long-sleeve shirt", "well-used dark tanktop", "good-looking blazer"]
    if visited_places['wardrobe']['visited']:
        game_logs.head('info')
        print("You already searched the wardrobe and found everything interesting.")
        return

    while True:
        if visited_places['wardrobe']['broken_door']:
            game_logs.head('narrator')
            print("You are in front of your wardrobe wide open.")

            game_logs.head('question')
            print("What will you do?")
            print("1. Check inside wardrobe.")
            print("2. Leave it there.")
            print("3. Check wood pile.")

        else:
            game_logs.head('narrator')
            print("The wardrobe door is stuck, but you can try to force it open.")

            game_logs.head('question')
            print("What will you do?")
            print("1. Break the door and check inside wardrobe.")
            print("2. Leave it there.")

        WardrobeChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if WardrobeChoice == "1":
            if visited_places['wardrobe']['broken_door']:
                game_logs.head('narrator')
                print("You dodge the pile of wood")

            else:
                visited_places['wardrobe']['broken_door'] = True
                game_logs.head('narrator')
                print("You force the wardrobe door open with all your strength.")
                print(f"The broken door collapses to the ground in a second, it is a {C.YELLOW}pile of wood now{C.NORMAL}.")

            print(f"Inside the wardrobe theres is a {C.YELLOW}collection of old and dusty clothes{C.NORMAL}.")

            while True:
                if visited_places['wardrobe']['w_u_d_tanktop_taken'] and visited_places['wardrobe']['g_l_blazer_taken']:
                    visited_places['wardrobe']['visited'] = True
                    game_logs.head('info')
                    print("You already took all the clothes from the wardrobe.")
                    return
                
                game_logs.head('question')
                print("What will you do?")
                print("1. Take the well-used dark tanktop.")
                print("2. Take the good-looking blazer.")
                print("3. Take nothing and leave.")
                ClothesChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

                if ClothesChoice == "1":
                    if visited_places['wardrobe']['w_u_d_tanktop_taken']:
                        game_logs.head('info')
                        print("You already took the well-used dark tanktop from the wardrobe.")
                        return
                    
                    visited_places['wardrobe']['w_u_d_tanktop_taken'] = True
                    game_logs.add_item(char, "well-used dark tanktop")
                    return
                
                elif ClothesChoice == "2":
                    if visited_places['wardrobe']['g_l_blazer_taken']:
                        game_logs.head('info')
                        print("You already took the good-looking blazer from the wardrobe.")
                        return
                    
                    visited_places['wardrobe']['g_l_blazer_taken'] = True
                    game_logs.add_item(char, "good-looking blazer")
                    return
                
                elif ClothesChoice == "3":
                    game_logs.head('narrator')
                    print("You left the wardrobe without taking any clothes.")
                    return
                
                else:
                    print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2 or 3.")

        elif WardrobeChoice == "2":
            game_logs.head('narrator')
            print("You decide to leave the wardrobe alone for now.")
            return
        
        elif WardrobeChoice == "3":
            game_logs.head('narrator')
            print("You check the wood pile.")

            game_logs.add_item(char, "wood plank")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1 or 2.")

@helpers.retry_on_inventory
def under_bed_choice(char):
    if visited_places['under_bed']['visited']:
        game_logs.head('info')
        print("You already searched under your bed and found nothing else.")
        return
    
    while True:
        game_logs.head('narrator')
        print(F"As you move your neck to see under your bed, {C.RED}your neck hurts{C.NORMAL}. Passing your hand over it, {C.RED}you notice a bruise{C.NORMAL}. Touching it make it hurt worsen.")
        
        game_logs.head('question')
        print("You processed to see under the bed?")
        print("1. Yes.")
        print("2. No.")
        BedChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if BedChoice == "1":
            game_logs.head('narrator')
            print("As your move your head under the bed, your neck hurt but you ignores it.")

            game_logs.damage(char, 10, "forcing his neck besides the pain")

            game_logs.head('narrator')
            print(f"There, on the botton of your mattress, {C.YELLOW}you notices something dark{C.NORMAL}.")

            while True:
                game_logs.head('question')
                print("You move your head closer?")
                print("1. Yes.")
                print("2. No.")
                SecondBedChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

                if SecondBedChoice == "1":
                    game_logs.head('narrator')
                    print("As you move your head closer, your neck hurt more.")

                    game_logs.damage(char, 20, "forcing his neck again besides the pain")

                    game_logs.head('narrator')
                    print(f"But then, you find out the dark thing was a {C.YELLOW}blooded rusty knife{C.NORMAL}.")

                    game_logs.add_item(char, "blooded rusty knife")
                    visited_places['under_bed']['knife_taken'] = True

                    game_logs.head('narrator')
                    print("You took it and leave the botton of your bed.")

                    visited_places['under_bed']['visited'] = True 
                    return
                
                elif SecondBedChoice == "2":
                    game_logs.head('narrator')
                    print("You decide the pain isn't worth it and pull your head out.")
                    return
                
                else:
                    print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif BedChoice == "2":
            game_logs.head('narrator')
            print("Deciding it's not worth the pain, you lay back down.")
            return

        else:
            print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

@helpers.retry_on_inventory
def shelves_choice(char):
    if visited_places['shelves']['visited']:
        game_logs.head('info')
        print("You already searched the shelves and found nothing else.")
        return
    
    while True:
        game_logs.head('narrator')
        print("As you pass by some books and others trinkets you've stash in there, you notice some interesting ones.")
        print(f"In the red shelve there are a {C.YELLOW}key with a feather attached{C.NORMAL} and a {C.YELLOW}hair clip{C.NORMAL}.")
        print("This shelve is way too high to reach it normally, so you grab a wooden stool to reach it.")

        game_logs.head('question')
        print("Will you try to took something?")
        print("1. Key with feather attached.")
        print("2. Hair clip.")
        print("3. Leave the shelf alone.")
        ShelvesChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

        if ShelvesChoice == "1":
            if visited_places['shelves']['key_taken']:
                game_logs.head('info')
                print("You already took the Key with feather attached from the shelves.")

            else:
                visited_places['shelves']['key_taken'] = True
                game_logs.add_item(char, "key with feather attached")

            game_logs.head('question')
            print(f"You will try to catch the {C.YELLOW}Hair Clip{C.NORMAL}?")
            print("1. Yes.")
            print("2. No.")
            StoolChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

            if StoolChoice == "1":
                if visited_places['shelves']['hair_clip_taken']:
                    game_logs.head('info')
                    print("You already took the Hair clip from the shelves.")

                else:
                    visited_places['shelves']['hair_clip_taken'] = True
                    game_logs.add_item(char, "hair clip")
                
                game_logs.head('narrator')
                print("But as you try to get down, the stool breaks and you fall to the ground.")

                game_logs.damage(char, 15, "falling off the stool")

                game_logs.head('narrator')
                print("You get up and leave the shelf.")

                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    game_logs.head('info')
                    print("You took all the interesting items from the shelves.")
                return
            
            elif StoolChoice == "2":
                game_logs.head('narrator')
                print("You decide to leave the hair clip there.")
                return
            
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif ShelvesChoice == "2":
            if visited_places['shelves']['hair_clip_taken']:
                game_logs.head('info')
                print("You already took the Hair clip from the shelves.")

            else:
                visited_places['shelves']['hair_clip_taken'] = True
                game_logs.add_item(char, "hair clip")

            game_logs.head('question')
            print(f"You will try to catch the {C.YELLOW}Key with feather attached{C.NORMAL}?")
            print("1. Yes.")
            print("2. No.")
            StoolChoice = helpers.choice(f"{C.MAGENTA}Enter the number of your choice: {C.NORMAL}")

            if StoolChoice == "1":
                if visited_places['shelves']['key_taken']:
                    game_logs.head('info')
                    print("You already took the Key with feather attached from the shelves.")

                else:
                    visited_places['shelves']['key_taken'] = True
                    game_logs.add_item(char, "key with feather attached")

                game_logs.head('narrator')
                print("But as you try to get down, the stool breaks and you fall to the ground.")

                game_logs.damage(char, 15, "falling off the stool")
                
                game_logs.head('narrator')
                print("You get up and leave the shelf.")

                if visited_places['shelves']['hair_clip_taken'] and visited_places['shelves']['key_taken']:
                    visited_places['shelves']['visited'] = True
                    game_logs.head('info')
                    print("You took all the interesting items from the shelves.")
                return
            
            elif StoolChoice == "2":
                game_logs.head('narrator')
                print("You decide to leave the Key with feather attached there.")
                return
            
            else:
                print(f"{C.RED}Invalid choice{C.NORMAL}! Please enter 1 or 2.")

        elif ShelvesChoice == "3":
            game_logs.head('narrator')
            print("You decide to leave the items where they are.")
            return
        
        else:
            print(f"{C.RED}Invalid choice!{C.NORMAL} Please enter 1, 2, or 3.")

main_choice_loop()