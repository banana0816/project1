import random

print("welcome to Harrison's game")
def status(playerhp,enemyhp,playermp,enemymp): 
    print({playerhp},{playermp},{enemyhp},{enemymp})





def start():
    playerhp = 3
    enemyhp = 3
    playermp = 1
    enemymp = 1





userinput = input("type start to start")
if userinput.lower() == "start":
    start()



    print("game start")
    print("input 1 to get mana")
    print("input 2 to attack")
    print("input 3 to defence")




    while True:
        choice = int(input("please type (1-3) to choose your movement:"))

        if choice == 1:
            playermp += 1
            print("playermp +1")




        elif choice == 2:
            while True:
                power2 = int(input("choose your attack level"))
                if power2 < 1 or playermp < power2:
                    print("unavaliable attack level")
                    continue
                playermp -= power2
                


        if choice == 3:
            while True:
                power3 = int(input("choose your defence level"))
                if power3 < 1 or playermp < power3 - 1:
                    print("unavaliable defence level")
                    continue
                    cost = power3 - 1
                    if cost > 0:
                        playermp -= cost


                    ea = random.choice
                    if enemymp == 0:
                        ea = "1"
                        enemymp += 1
                        print("enemymp +1")

                    elif ea == "2":
                        epower2 = random.randint(1,enemymp)
                        enemymp -= epower2
                        print("your enemy attacked, level{epower2}")
                    elif ea == "3": 
                        epower3 = random.randint(1,enemymp+1)
                        ecost = epower3 - 1
                        if cost > 0:
                            enemymp -= cost
                        ea = "3"
                        print("your enemy defended, level{epower3}")   




                                            










            
            










                    
