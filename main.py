import random
import time



hp = 0
mp = 0
print("welcome to Harrison's game")
#def __init__(self, name, health, mana)
    #self.name = name
    #self.hp = health
    #self.mp = mana
def status(playerhp,enemyhp,playermp,enemymp): 
        print({playerhp},{playermp},{enemyhp},{enemymp})

class player:
    def __init__(self, hp, mp):
         
         pass
class enemy:
    def __init__(self, hp):
         
         pass



def start():
    hp = 3
    mp = 1
    


userinput = input("type start to start")
if userinput.lower() == "start":
    start()



    print("game start")
    hp += 3
    print("input 1 to get mana")
    print("input 2 to attack")
    print("input 3 to defence")



class player:
    while True:
        choice = int(input("please type (1-3) to choose your movement:"))

        if choice == 1:
            mp += 1
            print("playermp +1")
            print(mp)
            print(hp)
            print("enemy action: defence")




        elif choice == 2:
            while True:
                power2 = int(input("choose your attack level"))
                if power2 < 1 or mp < power2:
                    print("unavaliable attack level")
                    continue
                mp -= power2
                print(mp)
                print("enemy action: charge")
                print("enemy hp - {power2}")
                break


        if choice == 3:
            while True:
                power3 = int(input("choose your defence level"))
                if power3 < 1 or mp < power3 - 1:
                    print("unavaliable defence level")
                    continue
                cost = power3 - 1
                if cost > 0:
                        mp -= cost
                        print(mp)
                        print("enemy action: attack")
                        print("nothing happened")
                        break
                
                        
                

             
     