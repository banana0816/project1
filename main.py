import random
import time










import random

def start_game():
    print("欢迎来到魔力对决游戏！")
    while True:
        command = input("请输入'start'开始游戏：").lower()
        if command == 'start':
            break
    
    # 初始化游戏状态
    game_state = {
        'player_hp': 3,
        'opponent_hp': 3,
        'player_mp': 1,
        'opponent_mp': 1,
        'round': 1
    }
    
    while True:
        print(f"\n=== 第 {game_state['round']} 回合 ===")
        print(f"玩家状态: HP={game_state['player_hp']}, MP={game_state['player_mp']}")
        print(f"对手状态: HP={game_state['opponent_hp']}, MP={game_state['opponent_mp']}")
        
        # 玩家行动选择
        player_action = get_player_action(game_state['player_mp'])
        
        # 电脑AI行动选择
        opponent_action = get_opponent_action(game_state['opponent_hp'], game_state['opponent_mp'])
        
        # 处理行动结果
        process_actions(player_action, opponent_action, game_state)
        
        # 检查游戏是否结束
        if game_state['player_hp'] <= 0:
            print("\n你的血量降为零！")
            print("You lose!")
            break
        if game_state['opponent_hp'] <= 0:
            print("\n对手的血量降为零！")
            print("You win!")
            break
        
        # 进入下一回合
        game_state['round'] += 1

def get_player_action(player_mp):
    while True:
        print("\n请选择你的行动:")
        print("1. 增加魔力值(MP+1)")
        print("2. 攻击")
        print("3. 防守")
        choice = input("输入1/2/3: ")
        
        if choice == '1':
            return {'type': 'charge', 'mp_change': 1}
        elif choice == '2':
            return get_attack_action(player_mp)
        elif choice == '3':
            return get_defense_action(player_mp)
        else:
            print("无效输入，请重新选择")

def get_attack_action(player_mp):
    while True:
        print(f"\n当前魔力值: {player_mp}")
        level = input("选择攻击等级(1/2/3): ")
        if level in ['1', '2', '3']:
            level = int(level)
            if level <= player_mp:
                return {'type': 'attack', 'level': level, 'mp_cost': level}
            else:
                print("魔力值不足！")
        else:
            print("无效输入，请重新选择")

def get_defense_action(player_mp):
    while True:
        print(f"\n当前魔力值: {player_mp}")
        level = input("选择防守等级(1/2/3): ")
        if level in ['1', '2', '3']:
            level = int(level)
            mp_cost = level - 1
            if mp_cost <= player_mp:
                return {'type': 'defense', 'level': level, 'mp_cost': mp_cost}
            else:
                print("魔力值不足！")
        else:
            print("无效输入，请重新选择")

def get_opponent_action(opponent_hp, opponent_mp):
    # 简单的AI逻辑
    if opponent_mp == 0:
        return {'type': 'charge', 'mp_change': 1}
    elif opponent_hp <= 1 and opponent_mp >= 2:
        # 低血量时倾向于防守
        max_defense = min(3, opponent_mp + 1)
        return {'type': 'defense', 'level': max_defense, 'mp_cost': max_defense - 1}
    else:
        # 随机选择攻击或充能
        if random.random() < 0.6 and opponent_mp >= 1:  # 60%概率攻击
            attack_level = random.randint(1, min(3, opponent_mp))
            return {'type': 'attack', 'level': attack_level, 'mp_cost': attack_level}
        else:
            return {'type': 'charge', 'mp_change': 1}

def process_actions(player_action, opponent_action, game_state):
    # 处理玩家行动
    if player_action['type'] == 'charge':
        game_state['player_mp'] += player_action['mp_change']
        print(f"\n你选择了充能，魔力值+{player_action['mp_change']}")
    elif player_action['type'] == 'attack':
        game_state['player_mp'] -= player_action['mp_cost']
        print(f"\n你发动了等级{player_action['level']}攻击，消耗{player_action['mp_cost']}MP")
    elif player_action['type'] == 'defense':
        game_state['player_mp'] -= player_action['mp_cost']
        print(f"\n你设置了等级{player_action['level']}防御，消耗{player_action['mp_cost']}MP")
    
    # 处理对手行动
    if opponent_action['type'] == 'charge':
        game_state['opponent_mp'] += opponent_action['mp_change']
        print(f"对手选择了充能，魔力值+{opponent_action['mp_change']}")
    elif opponent_action['type'] == 'attack':
        game_state['opponent_mp'] -= opponent_action['mp_cost']
        print(f"对手发动了等级{opponent_action['level']}攻击，消耗{opponent_action['mp_cost']}MP")
    elif opponent_action['type'] == 'defense':
        game_state['opponent_mp'] -= opponent_action['mp_cost']
        print(f"对手设置了等级{opponent_action['level']}防御，消耗{opponent_action['mp_cost']}MP")
    
    # 处理互动结果
    if player_action['type'] == 'attack' and opponent_action['type'] == 'attack':
        # 双方都攻击
        player_level = player_action['level']
        opponent_level = opponent_action['level']
        
        if player_level > opponent_level:
            damage = player_level - opponent_level
            game_state['opponent_hp'] -= damage
            print(f"你的攻击更强！对手受到{damage}点伤害")
        elif opponent_level > player_level:
            damage = opponent_level - player_level
            game_state['player_hp'] -= damage
            print(f"对手的攻击更强！你受到{damage}点伤害")
        else:
            print("双方攻击等级相同，没有造成伤害")
    
    elif player_action['type'] == 'attack' and opponent_action['type'] == 'defense':
        # 玩家攻击，对手防守
        attack_level = player_action['level']
        defense_level = opponent_action['level']
        
        if attack_level > defense_level:
            damage = attack_level - defense_level
            game_state['opponent_hp'] -= damage
            print(f"你的攻击突破了对手的防御！对手受到{damage}点伤害")
        else:
            print("对手成功防御了你的攻击")
    
    elif player_action['type'] == 'defense' and opponent_action['type'] == 'attack':
        # 玩家防守，对手攻击
        defense_level = player_action['level']
        attack_level = opponent_action['level']
        
        if attack_level > defense_level:
            damage = attack_level - defense_level
            game_state['player_hp'] -= damage
            print(f"对手的攻击突破了你的防御！你受到{damage}点伤害")
        else:
            print("你成功防御了对手的攻击")































                                            










            
            










                    
