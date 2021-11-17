# !/usr/bin/python3
# 文件名: using_sys.py

# import loop

import sys
print('命令行参数如下')
for i in sys.argv:
    print(i)

print('\nPython 路径为：', sys.path, '\n')

dir(sys)
print(dir(sys))  # 找到模块内定义的所有名称，以一个字符串的列表形式返回
print(dir())  # 没有参数，罗列出当前定义的所有名称

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')

