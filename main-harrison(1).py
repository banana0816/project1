import random
import time

def print_status(a, b, c, d):#function for printing status
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    if c < 0:
        c = 0
    if d < 0:
        d = 0
    print(f"\nplayer's HP: {a}  player's MP: {b}  enemy's HP: {c}  enemy's MP: {d}")

def choice():#function for choosing
    print("what do you want to do?")
    print("1. charge")
    print("2. attack")
    print("3. defend")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_level(mp, action): #detect the level of attack or defend
    while True:
        try:
            if action == "attack":
                level = int(input(f"Enter attack level {action}(current MP is {mp}):"))
                if 1 <= level <= mp:
                    return level
                
            elif action == "defend":
                level = int(input(f"Enter defend level {action}(current MP is {mp}):"))
                if 1 <= level <= mp:
                    return level
                
        except:
            pass
        print(f"Invalid input. Please enter a number between 1 and {mp}.")

def enemy_ai(x, y):
    if y == 0:
        return 1, 0 #charge
    action = random.randint(2, 3)
    if action == 2:
        level = random.randint(1, y)
    else:
        level = random.randint(1, y + 1)
    return action, level

start = input("enter \" start \" to start the game: ").lower()
if start != "start":
    print("Invalid input. Please enter 'start' to begin the game.")
    exit()

player_hp = 3
player_mp = 1
enemy_hp = 3
enemy_mp = 1

while player_hp > 0 and enemy_hp > 0:
    print_status(player_hp, player_mp, enemy_hp, enemy_mp)

    player_action = choice()
    if player_action == 1:
        player_level = 0
    elif player_action == 2 and player_mp > 0:
        player_level = get_level(player_mp, "attack")
    elif player_action == 3 and player_mp > 0:
        player_level = get_level(player_mp, "defend")
    else :
        print("failed")
    

    enemy_action, enemy_level = enemy_ai(enemy_hp, enemy_mp)

    print(f"\n enemy chose {enemy_action} with level {enemy_level}")
    time.sleep(1)

    if player_action == 1:
        player_mp += 1
    elif player_action == 2:
        player_mp -= player_level
    elif player_action == 3:
        player_mp -= (player_level - 1)


    if enemy_action == 1:
        enemy_mp += 1
    elif enemy_action == 2:
        enemy_mp -= enemy_level
    elif enemy_action == 3:
        enemy_mp -= (enemy_level - 1)

    if player_action == 1 and enemy_action == 1:
        pass 
    elif player_action == 2 and enemy_action == 2:
        if player_level > enemy_level:
            enemy_hp -= player_level - enemy_level
        elif player_level < enemy_level:
            player_hp -= enemy_level - player_level
    elif player_action == 2 and enemy_action == 3:
        if player_level < enemy_level:
            pass
        else:
            enemy_hp -= enemy_level - player_level
    elif player_action == 3 and enemy_action == 2:
        if enemy_level < player_level:
            pass
        else:
            player_hp -= player_level - enemy_level
    elif player_action == 1 and enemy_action == 2:
        player_hp -= enemy_level
    elif player_action == 1 and enemy_action == 3:
        pass
    elif player_action == 2 and enemy_action == 1:
        enemy_hp -= player_level
    elif player_action == 3 and enemy_action == 1:
        pass
    elif player_action == 3 and enemy_action == 3:
        pass

print_status(player_hp, player_mp, enemy_hp, enemy_mp)
if player_hp <= 0:
    print("\nYou lose!")
elif enemy_hp <= 0: 
    print("\nYou win!")



    
