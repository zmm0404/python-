heigh = int(input('请输入您的身高（cm）:'))
worth = int(input('请输入您的身价：'))
score = int(input('请输入您的颜值分：'))
if heigh >= 180 and worth > 1000000 and score > 99:
	print('高富帅一枚')
if heigh <180 and  worth > 1000000 and  score > 9:
	print('富帅一枚')
if heigh < 180 and worth < 1000000 and  score > 99:
	print('仅仅是帅而已')
if heigh  < 160 and worth < 100 and score < 60:
	print('你就是个矮矬穷')
