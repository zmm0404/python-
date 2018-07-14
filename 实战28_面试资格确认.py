while True:
	age = int(input('请输入您的年龄：'))
	subject = input('请输入您的专业:')
	college = input('是否为重点大大学:')

		
	if age > 25 and subject == '电子信息工程':
		print('恭喜您已被录取\n')
	elif subject == '电子信息工程' and college == '是':
		print('恭喜您已被录取\n')
	elif age < 28 and subject == '计算机':
		print('恭喜您已被录取\n')
	else:
		print('抱歉，您未达到面试要求')
		break
