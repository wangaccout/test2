import math
import sys
import re
# str()：函数返回一个用户易读的表达形式
# repr():产生一个解释器易读的表达形式

s = 'Hello, Runoob'
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
z = 'x 的值为： ' + str(x) + ',  y 的值为：' + str(y) + '...'
print(s)
print(z)

# repr()函数可以转移字符串中的特殊字符
hello = 'Hello, Runoo\nb'
print(str(hello))
print(repr(hello))

# repr()的参数可以是Python中的任何对象
print(repr((x, y, ('good', 'word'))))
w = repr((x, y, ('Google', 'Runoob')))
print(w)

# rjust()方法 将字符串靠右，并在左边填充空格;类似方法有ljust()和center()，
for x in range(1, 5):
    print(repr(x).rjust(1), repr(x*x).rjust(2), repr(x*x*x).rjust(3))
    # print(repr(x*x*x).rjust(3))
print("``````````````````````````````")
for x in range(2, 5):
    print('{0:1d}{1:3d}{2:4d}'.format(x, x*x, x*x*x))

# zfill()在数字的左边填充0
print('12'.zfill(5))

# str.format()的基本使用
print('{}你好，“{}！”'.format('北京', '哈哈'))
print('{1} and {0}'.format(0, 1))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
# 保留3位小数
print('常量PI的值近似为{0:.3f}'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'google': 1, 'runoob': 2, 'taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 在格式化时通过变量名而非位置,使用方括号[]来访问键值
print('runoob: {0[runoob]:d}; taobao: {0[taobao]:d}; google:{0[google]:d}'.format(table))
print('runoob:{runoob:d}'.format(**table))

# %进行格式化
print('常量PI的值近似为%.3f' % math.pi)

# 读取键盘输入
str = input("请输入：")
if not re.match('^[a-z]*$', str):
    print('只能输入a-z')
    sys.exit(0)
elif len(str) > 5:
    print("最多5个字")
    sys.exit(1)
print('你输入的内容是：' + str)





