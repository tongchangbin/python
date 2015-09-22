#无法解决输入小数的问题:
print('永远为整数')
print('----')
a = input('请输入数字：')
a = int(a)
if a >= 0:
	print(a)
else:
	print(-a)