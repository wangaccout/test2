# f-string 字面量格式化字符串
# f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
# name = 'runoob'
# print(f'hello {name}')
#
# print(f'{1+2}')
#
# w = {'name': 'runoob', 'url': 'www.runoob.com'}
# print(f'{w["name"]}: {w["url"]}')
#
# x = 1
# print(f'{x+1}')
# print(x + 1)
# print(f'{x+1=}')  # 使用=符号来拼接运算表达式与结果
# print("x+1=" + str(x+1))

# 字符串反转 5种方法
# 1.reverse()方法对列表操作取反,join()方法使列表转换为字符串
# str = 'abcd'
# list1 = list(str)
# list1.reverse()
# print(''.join(list1))

# 2.for循环
# str = list(input('please input'))
# str = 'abcd'
# list = []
# for i in range(len(str)):
#     list.append(str[len(str) - i - 1])
# print(''.join(list))

# 3.递归+切片
def des_output(str):
    if(len(str) > 0):
        print(str[-1], end='')  # 负数下标，先打印最后一个元素
        des_output(str[0:-1])  # 从第一个元素到倒数第二个元素(从第一个元素到倒数第三个元素...)
str = 'abcd'
des_output(str)
print('``````````')
print(str[0:-1])

str = 'abcd'
for i in range(len(str)):
    if(len(str) > 0):
            print(str[-1], end='')  # 负数下标，先打印最后一个元素
            str = str[0:-1]
print('``````````')

# 4.range()第三个参数
str = 'abcd'
for i in range(len(str) - 1, -1, -1):  # 起始，结束(不包含)，反向步长
    print(str[i], end='')
print('``````````')

# 5.切片
str = 'abcd'
print(str[::-1])

