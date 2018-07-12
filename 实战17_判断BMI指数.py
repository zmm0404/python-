height = float(input('请输入小明的身高（m）:'))
weight = float(input('请输入小明的体重（kg）:'))
BMI = weight/(height*height)
if BMI >= 18.5 and BMI <= 25:
	print('小明的MBI指数是%s,属于正常' % BMI)
elif BMI > 25 and BMI <= 28:
	print('小明的MBI指数是%s,属于过重' % BMI)
elif BMI > 28 and BMI <= 32:
	print('小明的MBI指数是%s,属于肥胖' % BMI)
elif BMI > 32:
	print('小明的MBI指数是%s,属于严重肥胖' % BMI)


else:
	print('小明的MBI指数是%s,属于过轻' % BMI)
