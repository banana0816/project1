print("welcome to Harrison's game")
def status(playerhp,enemyhp,playermp,enemymp): 
    print(status)





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
                if power3 < 1 or playermp < power3-1





            
            










                    
