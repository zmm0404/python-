print('在古希腊神话中，玫瑰花集爱情与美丽与一身，所以人们常用玫瑰来表达爱情，但是不用的朵数玫瑰花代表着不同的含义')
rose =int(input('请输入你要送给女朋友玫瑰花的朵数:'))
if rose == 1:
	print('%d朵：你是我的唯一' % rose)
elif rose == 3:
	print('%d朵：I Love You' % rose)
elif rose == 10:
	print('%d朵：十全十美' % rose)
elif rose == 99:
	print('%d朵：天长地久' % rose)
elif rose == 108:	
	print('%d朵：求婚' % rose)
elif rose == 999:
	print('%d朵：土豪' % rose)
else:
	print('我也不知道，你可以考虑送1朵、3朵、10朵、99朵、108朵、999朵效果图')
