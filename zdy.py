#自定义函数
x = input('请输入数字：')
x = int(x)
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
print(my_abs(x))