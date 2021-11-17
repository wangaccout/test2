# f-string 字面量格式化字符串
# f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
name = 'runoob'
print(f'hello {name}')

print(f'{1+2}')

w = {'name': 'runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

x = 1
print(f'{x+1}')
print(x + 1)
print(f'{x+1=}') # 使用=符号来拼接运算表达式与结果
print("x+1=" + str(x+1))

