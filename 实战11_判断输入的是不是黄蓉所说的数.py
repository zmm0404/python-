print('Question:今有物不知其数，三三之数剩二，五五之数剩三，七七之数剩二，问几何')
a = int(input('请输入您认为符合条件的数：'))

if a%3 == 2 and a%5 == 3 and a%7 == 2:
	print('符合条件')
else:
	print('不符合条件')
