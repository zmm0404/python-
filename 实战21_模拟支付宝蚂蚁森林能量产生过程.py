print('查询能量请输出能量来源!退出程序请输入0:0\n能量来源如下:\n生活缴费 行走捐 共享单车 线下支付 网络购票\n')
while True:
	mode = input('请输入能量来源:')
	if mode == '行走捐':
		print('本次产生的能量为:200g\n')
	elif mode == '生活缴费':
		print('本次产生的能量为:300g\n')
	elif mode == '共享单车':
		print('本次产生的能量为:350g\n')
	elif mode == '线下支付':
		print('本次产生的能量为:380g\n')
	elif mode == '网络购票':
		print('本次产生的能量为:500g\n')
	elif mode == '0:0':
		print('已退出')
		break
	else:
		print('输入有误,请重新输入\n')
