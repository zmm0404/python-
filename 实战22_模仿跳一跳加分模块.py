print('--------挑一挑,输入"退出"即可退出游戏-------\n')
while True:
	module = input('请输入中心.音乐模块.微信支付模块中的任意一个模块:')
	if module == '中心':
		print('您的分数为:32分\n')
	elif module == '音乐模块':
		print('您的分数为:30分\n')
	elif module == '微信支付模块':
		print('您的分数为:42分\n')
	elif module == '退出':
		print('已退出')
		break
	else:
		print('输入有误,请重新输入\n')
