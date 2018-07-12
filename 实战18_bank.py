account = int(input('请输入您的账号：'))
passwd = int(input('请输入您的密码:'))
if account == 100 and passwd ==10:
	print('请输入取钱金额')
	money = int(input())
 
	if money >= 1000: 
		print('您本次取现%s元,剩余%s元'%(money,(5000-1000)))
	else:
		print('目前您的账目没有钱，还去毛线')
else:
	print('非法账户')
