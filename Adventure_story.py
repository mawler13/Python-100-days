import random

health = 100
inventory = []

def start_game():
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.")
    answer = input("Are you ready? Type y or n: ").strip().lower()
    if answer == 'y':
        print("You are a brave soul")
        crossroad()
    else:
        print("Goodbye coward")

def crossroad():
    path = input("You've landed on the island, you come to a crossroads, do you go left or right? type left or right : ").strip().lower()
    if path == "left":
        print("You were ambushed and killed by an indigenous tribe. Game over ")
    elif path == "right":
        jungle_path()

def jungle_path():
    direction = input("Do you want to go left into the woods or right towards the river? Type right or left ").strip().lower()
    if direction == 'left':
        print("You get lost in the woods and die. Game over. ")
    elif direction == 'right':
        river_crossing()
    else:
        print("You are unsure and delay too long. A snake bites you. Game over. ")

def offer_torch():
    global inventory
    choice = input("You see a torch nearby. Do you pick it up? Type yes or no: ").strip().lower()
    if choice == "yes":
        inventory.append("torch")
        print("Torch added to inventory.")
    else:
        print("You leave the torch behind.")

def river_crossing():
    global health, inventory
    river_choice = input("You come to a river, do you wait for a boat or do you swim across? Type wait or swim ").strip().lower()
    if river_choice == 'wait':
        print("As you wait, a mysterious old man with a boat comes to take you across. ")
        offer_torch()
        print("On the other side you find an X on the ground but it seems too easy... ")
        dig_decision()
    elif river_choice == 'swim':
        swim_fate = random.choice(["safe", "crocodile", "current"])
        if swim_fate == "crocodile":
            print("You are attacked by a crocodile while swimming!")
            health -= 100
            print(f"Health: {health}")
            print("You have died. Game over. ")
        elif swim_fate == "current":
            print("The current pulls you off course, but you manage to reach the shore exhausted.")
            health -= 20
            print(f"Health: {health}")
            print("You see an X marked on the ground near some bushes.")
            offer_torch()
            dig_decision()
        else:
            print("You swim across safely.")
            offer_torch()
            print("You see an X marked on the ground near some bushes.")
            print("It looks too easy... something feels off.")
            dig_decision()
    else:
        print("You wander around in circles and succumb to dehydration. Game over. ")

def dig_decision():
    global health, inventory
    dig_choice = input("Do you dig or decide to ignore it and move on? Type dig or move: ").strip().lower()
    if dig_choice == 'dig':
        outcome = random.choice(["treasure", "nothing", "trap"])
        if outcome == "treasure":
            print("You uncover a hidden chest with gold coins! Lucky you!")
            inventory.append("extra gold")
            cave_scene()
        elif outcome == "nothing":
            print("You dig and dig... but find nothing but dirt. You move on disappointed.")
            cave_scene()
        elif outcome == "trap":
            print("A trap springs! You fall into a spike pit and don't survive. Game over.")
            health = 0
    elif dig_choice == 'move':
        print("You decide to trust your instincts and move on.")
        print("You walk deeper into the jungle and stumble upon a dark cave entrance.")
        print("Carved into the cave walls are hieroglyphics glowing faintly... ")
        cave_scene()
    else:
        print("You stand too long trying to decide... and a venomous snake bites you. ")
        health -= 30
        print(f"You lose 30 health. Current health: {health}")
        if health <= 0:
            print("You have died. Game over.")

def cave_scene():
    global inventory
    glyph_choice = input("Do you decide to enter the cave or stay outside? Type enter or stay: ").strip().lower()
    if glyph_choice == 'enter':
        if "torch" in inventory:
            use_torch = input("You have a torch. Do you want to light it? Type yes or no: ").strip().lower()
            if use_torch == "yes":
                print("You light your torch and step into the cave. The symbols begin to glow brighter.")
                print("A hidden door opens .... revealing a chamber full of gold and ancient relics.")
                print("Congratulations you have found the treasure!")
                inventory.append("gold")
                boss_fight()
            else:
                print("Without light, you stumble in the darkness and fall into a pit. Game over.")
        else:
            print("It's too dark to see. You stumble and fall into a pit. Game over.")
    elif glyph_choice == 'stay':
        print("You wait outside, but night falls and strange sounds fill the jungle. You are never seen again. ")
        print("Game over.")
    else:
        print("Frozen by indecision, you are caught in a sudden land slide. Game over.")

def boss_fight():
    global health
    print("Suddenly, a shadowy figure emerges from the gold chamber - it's the Guardian of the Treasure!")
    print("You must decide how to face it: fight, run, or outsmart ")
    action = input("What do you do? Type fight, run, or outsmart: ").strip().lower()
    if action == 'fight':
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print("You bravely battle the Guardian and win, the treasure is yours!")
        else:
            print("You fought valiantly, but the Guardian was too much. Game over. ")
    elif action == 'run':
        print("You drop some gold and manage to escape with your life. Not bad!")
    elif action == 'outsmart':
        print("You challenge the Guardian with a riddle. Answer it correctly and you win your freedom. ")
        answer = input("I speak without a mouth and hear without ears. I have no body but I come alive with the wind. What am I? ").strip().lower()
        if "echo" in answer:
            print("The Guardian nods. 'You are wise,' it says, and lets you leave with the treasure. You win!")
        else:
            print("The Guardian frowns. 'Incorrect,' it growls. 'Prepare to meet your end.' Game over.")
    else:
        print("You freeze in fear. The Guardian shows no mercy. Game over. ")

start_game()
