import re
# re.match函数 从字符串的其实位置匹配一个模式
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('www', 'www.runoob.com'))
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# re.search方法,扫描整个字符串并返回第一个成功的匹配。
# re.search(pattern, string, flags=0)
print(re.search('com', 'www.runoob.com'))  # 扫描整个字符串并返回第一个成功的匹配

# 检索和替换
# re.sub(pattern, repl, string, count=0, flags=0)
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print('电话号码：', num)
# 移除非数字内容
num = re.sub(r'\D', ' ', phone)
print('电话号码：', num)

# repl参数是一个函数
# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# compile 函数
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
print(pattern.match('one12twothree34four', 2, 10))  # 从'e'的位置开始匹配，没有匹配
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象
print(m.group(0))  # 获得一个或多个分组匹配的字符串
print(m.start(0))  # 获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引）
print(m.start())
print(m.end(0))    # 获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0
print(m.span(0))   # 返回 (start(group), end(group))

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)
print(m.group())

# findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
result1 = re.findall(r'\d+', 'runoob 123 google 456')
pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
print(result3)

# finditer 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())

# re.split()
m = re.split('\W+', 'runoob, runoob, runoob.')
print(m)
print(re.split('\W+', 'runoob, runoob, runoob.'))

