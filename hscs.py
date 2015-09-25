#函数的参数
x = input('请输入数字：')
n = input('请输入数字：')
x = int(x)
n = int(n)
def power(x,n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(x,n))