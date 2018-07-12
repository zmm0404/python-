import random
computer = random.randint(1,10)
player = int(input('请玩家输入一个数字：'))
if player == computer:
	print('胜利')
else:
	print('失败，你是一个loser')
