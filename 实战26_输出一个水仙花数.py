while True:
	a = int(input('请输入百位数：'))
	b = int(input('请输入十位数：'))
	c = int(input('请输入个位数：'))
	d = 100*a+10*b+c
	if a**3+b**3+c**3 == d:
		print('恭喜，您输入的 %d 是水仙花数\n'%d)
	else:
		print('sorry,您输入的数不是水仙花数，请重新输入\n')
