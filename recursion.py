# 递归案例
# 1.3以内数字累加和
def sum_numbers(num):
    # 如果是1，直接返回1 -- 出口
    if num == 1:
        return 1
    # 如果不是1,重复执行累加并返回结果
    return num + sum_numbers(num-1)
sum_result = sum_numbers(3)
print(sum_result)

# 2.n以内数字阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# fact_result = fact(3)
# print(fact_result)

# 3.斐波那契数列
# def fibo(n):
#     if n ==1 or n == 2:
#         return
#     else:
#         return fibo(n-1) + fibo(n-2)
# # fibo_result = fibo(10)
# # print(fibo_result)
# fibo(10)

def di_gui(n):
    print(n, "<===1====>")
    if n > 0:
        di_gui(n - 1)
    print(n, '<===2====>')
di_gui(5) # 外部调用后打印的结果是？
