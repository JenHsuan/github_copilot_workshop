# 請我幫寫一個剪刀石頭布的遊戲

import random


def game():
    # 1. 電腦隨機出拳
    computer = random.choice(['剪刀', '石頭', '布'])
    # 2. 玩家出拳
    player = input('請出拳(剪刀/石頭/布): ')
    # 3. 判斷輸贏
    if player == computer:
        print('平手')
    elif player == '剪刀' and computer == '石頭':
        print('你輸了')
    elif player == '石頭' and computer == '布':
        print('你輸了')
    elif player == '布' and computer == '剪刀':
        print('你輸了')
    else:
        print('你贏了')
    print(f'電腦出拳: {computer}')


game()
    