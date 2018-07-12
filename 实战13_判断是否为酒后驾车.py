print('为了您和他人的安全，严禁酒后驾车')
alcohol = int (input('请输入每100ml血液的酒精含量（mg）：'))
if alcohol >= 20:
	if alcohol >= 20 and alcohol < 80:
		print('已经到达酒后驾驶标准，请不要开车')
	else:
		print('已经达到醉酒驾驶的标准，请千万不要开车！') 
else:
	print('您还构不成饮酒行为，可以开车，但是要注意安全')
