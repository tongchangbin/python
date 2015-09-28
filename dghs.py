#递归函数
n = input('请输入数值：')
n = int(n)
def fact(n):
	return fact_iter(n, 1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
print('输出数值：',fact(n))