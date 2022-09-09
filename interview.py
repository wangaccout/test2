# coding=utf-8

# 1.给定三个数a b c,通过程序判断任意两数之和大于第三个数
# a = input(int)
# b = input()
# c = input()
# if (a+b>c) or (a+c>b) or (b+c>a):
#     print('yes')
# else:
#     print('no')

# 2.按词倒序输出，并输出s的个数
# a = 'this is a test'
# l = a.split(" ")
# print(l)
# l1 = l[::-1]
# print(l1)
# a1 = ' '.join(l1)
# print(a1)
# c = a.count('s')
# print('s的个数：', c)

# 3.a[]={2,6,8,9,1,2}进行排序输出
# a = [7, 6, 18, 9, 1, 2]
# count = len(a)
# for i in range(0, count):
#     for j in range(i+1, count):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# for i in range(1, count):
#     for j in range(0, count-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
#
# for i in range(0, count):
#     for j in range(0, count-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
#
# def bubble_sort(array):
#     for i in range(1, len(array)):
#         for j in range(0, len(array) - i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
# if __name__ == '__main__':
#     array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
#     print(bubble_sort(array))
#
#
# def bubbleSort(arr):
#     n = len(arr)
#     # 遍历所有数组元素
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])

# 4.字符索引
# def getInfo(abc, a, b):
#     startIndex = abc.index(a)
#     if startIndex >= 0:
#         startIndex += len(a)
#         endIndex = abc.index(b)
#         print(abc[0:startIndex-4])
#         print(abc[startIndex:endIndex])
#         print(startIndex, endIndex)
#
# getInfo('terlet is good jobs', 'er', 'od')

# 5.解密算法函数
# str0 = 'abc1fd2eh3'
# str1 = ''
# for i in str0:
#     if i.isdigit():
#         x = int(i)
#         str1 += str0[0:str0.index(i)] * x
#         str0 = str0[str0.index(i) + 1:]
# print(str1)

# 6.拆分字符串
# str = 'http://***?stringOne=++jj&timeStamp=151'
# str1 = str.split('?')
# # str2 = str1[1].split('&')[0].split('=')
# str2 = str1[1].split('&')
# str3 = str2[0].split('=')
# str4 = str2[1].split('=')
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# 7.两数组求交集
# a = [6, 4, 1]
# b = [1, 9, 10, 7, 1, 6, 2]
# for i in a:
#     for j in b:
#         if i == j:
#             print(i)

# 8.判断闰年
# 普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
# 世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）
# year = input('请输入一个整数')
# year = input(int)
# year = int(input('请输入年份:'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, '是闰年')
# else:
#     print(year, '不是闰年')
#
import calendar
# years = int(input('请输入年份'))
# check_year = calendar.isleap(years)
# if check_year:
#     print('{0}是闰年'.format(years))
# else:
#     print('{}不是闰年'.format(years))

# 9.找出列表中出现次数超过一半的数字
# list = 1, 2, 3, 4, 2, 2, 2
list = 'a', 'b', 'c', 'a', 'a', 'a'
dict = {}
half = len(list) // 2
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

for k, v in dict.items():
    if v > half:
        print(k, '出现的次数是', v)

# list = 1, 2, 3, 4, 1, 1, 1
# len = len(list)
# count = 0
# for i in list:
#     if list.count(i) > len/2:
#         print(i)
#         count = list.count(i)
#         print(i, '的个数：', count)




