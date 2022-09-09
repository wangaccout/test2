# 1.冒泡排序：对比模型，原数组上排序，稳定，慢-------------------------------------
# list1 = [5, 9, 4, 3, 1]
# count = len(list1)
# for i in range(0, count):
#     for j in range(i+1, count):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)

# list1 = [5, 9, 4, 3, 1]
# count = len(list1)
# for i in range(1, count):
#     for j in range(0, count-i):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)

# 2.选择排序：对比模型，原数组上排序，稳定，慢------------------------------------
# list2 = [5, 9, 4, 3, 1]
# count = len(list2)
# for i in range(count):
#     x = i
#     for j in range(i, count):
#         if list2[j] < list2[x]:
#             x = j
#             list2[i], list2[x] = list2[x], list2[i]
# print(list2)

# list2 = [5, 9, 4, 3, 1]
# count = len(list2)
# for i in range(count):
#     x = i
#     for j in range(i, count):
#         if list2[x] > list2[j]:
#             x = j
#             list2[i], list2[j] = list2[j], list2[i]
# print(list2)

# 3.插入排序：对比模型，原数组上排序，稳定，慢-----------------------------------------
# list3 = [5, 9, 4, 3, 1]
# for i in range(len(list3)):
#     for j in range(i):
#         if list3[i] < list3[j]:
#             list3.insert(j, list3.pop(i))
# print(list3)

# 4.快速排序：对比模型，原数组上排序，不稳定，快-------------------------------------------
def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)
    recursive(0, len(array) - 1)
    return array

array = [5, 9, 4, 3, 1]
quick_sort(array)
print(array)










