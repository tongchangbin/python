#无法解决输入字母，程序报错的问题
print('计算BMI公式')
sg = input('请输入你的身高：')
tz = input('请输入你的体重：')
s = float(sg)
t = float(tz)
bmi = t/(s*s)
if bmi >32:
	print('严重肥胖')
elif 28<bmi<=32:
	print('肥胖')
elif 25<bmi<=28:
	print('过重')
elif 18.5<bmi<=25:
	print('正常')
else:
	print('过轻')