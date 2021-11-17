import sys
# 错误和异常
# try:
#     # runoob()
#     print('哈哈哈哈')
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('test1.txt') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行')

# 使用raise抛出一个指定的异常
# x = 10
# if x > 5:
#     raise Exception('x不能大于5.x的值为：{}'.format(x))

# 自定义异常,继承自 Exception 类，可以直接继承，或者间接继承
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('my exception occurred,value:', e.value)
# raise  MyError('OOPS')

# 定义清理行为 finally语句
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is:', result)
    finally:
        print('executing finally clause')
# divide(2, 1)
# divide(2, 0)
divide('2', '1')










