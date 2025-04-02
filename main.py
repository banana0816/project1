user_input = input("type'start'to start the game: ")
if user_input.lower() == "start":
    start_game()
else:
    print("error,please run the program again to play the game")

    import random
    def display_status(player_hp, enemy_hp, player_mp, enemy_mp):
        print("\n当前状态:")
        print(f"玩家: HP={player_hp}, MP={player_mp}")
        print(f"对手: HP={enemy_hp}, MP={enemy_mp}\n")
    def start_game():
        player_hp = 3
        enemy_hp = 3
        player_mp = 1
        enemy_mp = 1

        print("游戏开始！")
    print("每回合你可以选择：")
    print("1. muse（MP+1）")
    print("2. attact（cost MP）")
    print("3. defense（cost MP）")

while True:
        display_status(player_hp, enemy_hp, player_mp, enemy_mp)
    
        while True:
            try:
                choice = int(input("请选择行动(1-3): "))
                if choice not in [1, 2, 3]:
                    print("请输入1-3之间的数字！")
                    continue
                break
            except ValueError:
                print("请输入有效的数字！")

                player_action = None
        player_power = 0
        
        if choice == 1:
            player_mp += 1
            player_action = "冥想"
            print("你选择了冥想，MP+1")
        elif choice == 2:
            while True:
                try:
                    player_power = int(input("选择攻击等级(1-当前MP): "))
                    if player_power < 1 or player_power > player_mp:
                        print(f"攻击等级必须在1-{player_mp}之间！")
                        continue
                    break
                except ValueError:
                    print("请输入有效的数字！")
            player_mp -= player_power
            player_action = "攻击"
            print(f"你选择了攻击，等级{player_power}")
        elif choice == 3:
            while True:
                try:
                    player_power = int(input("选择防御等级(1-当前MP+1): "))
                    if player_power < 1 or player_power > player_mp + 1:
                        print(f"防御等级必须在1-{player_mp + 1}之间！")
                        continue
                    break
                except ValueError:
                    print("请输入有效的数字！")
            cost = player_power - 1
            if cost > 0:
                player_mp -= cost
            player_action = "防御"
            print(f"你选择了防御，等级{player_power}")

            enemy_action = None
        enemy_power = 0
        
        if enemy_mp == 0:
            enemy_action = "冥想"
            enemy_mp += 1
            print("对手选择了冥想，MP+1")
        else:
            # 简单AI：随机选择行动
            options = []
            if enemy_mp < 3:  # 如果MP不足，倾向于冥想
                options.append("冥想")
            options.append("攻击")
            options.append("防御")
            
            enemy_choice = random.choice(options)
            
            if enemy_choice == "冥想":
                enemy_action = "冥想"
                enemy_mp += 1
                print("对手选择了冥想，MP+1")
            elif enemy_choice == "攻击":
                enemy_power = random.randint(1, enemy_mp)
                enemy_action = "攻击"
                enemy_mp -= enemy_power
                print(f"对手选择了攻击，等级{enemy_power}")
            elif enemy_choice == "防御":
                enemy_power = random.randint(1, enemy_mp + 1)
                cost = enemy_power - 1
                if cost > 0:
                    enemy_mp -= cost
                enemy_action = "防御"
                print(f"对手选择了防御，等级{enemy_power}")

                if player_action == "攻击" and enemy_action == "攻击":
                    if  player_power > enemy_power:
                        enemy_hp -= (player_power - enemy_power)
                print(f"你的攻击更强！对手损失{player_power - enemy_power}点HP")
            elif enemy_power > player_power:
                player_hp -= (enemy_power - player_power)
                print(f"对手的攻击更强！你损失{enemy_power - player_power}点HP")
            else:
                print("双方攻击相互抵消，没有造成伤害")
            elif player_action == "攻击" and enemy_action == "防御":
            if player_power > enemy_power:
                damage = player_power - enemy_power
                enemy_hp -= damage
                print(f"你的攻击突破了对手的防御！对手损失{damage}点HP")
            else:
                print("对手成功防御了你的攻击")
            elif player_action == "防御" and enemy_action == "攻击":
            if enemy_power > player_power:
                damage = enemy_power - player_power
                player_hp -= damage
                print(f"对手的攻击突破了你的防御！你损失{damage}点HP")
            else:
                print("你成功防御了对手的攻击")

        if player_hp <= 0:
            print("\n你的HP归零了...")
            print("You lose!")
            break
        if enemy_hp <= 0:
            print("\n对手的HP归零了！")
            print("You win!")
            break