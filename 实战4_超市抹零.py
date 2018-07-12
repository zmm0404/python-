print('请输入苹果的价格：')
A = input()  

print('请输入香蕉的价格：')
B = input() 

C = float(A)+float(B)  # 总价格
print('商品的总价格为：')
print(C)
print(type(C))
print('-----------------------------')
print('价格转化为字符型结果为：')
D = str(C) # 浮点型转化成字符型
print(D)
print(type(D))
print('-----------------------------')
print('抹零')
E = int(C)  # 取整
print(E)
print (type(E))
