# __author__ = 'Kaiming'
#
# def triangles():
# ##首先理解杨辉三角是如何计算下一行的。简单来说就是，从第三行开始，每一
# # 行的左右两边都和上一行相同，中间的元素是通过上一行的元素两两相加得来的##
#
#
#     L=[1]
#     yield L
#     while True:
#         #列表生成式就是将上一行相邻的两个元素的和作为现在新行的元素，同时保留上一行两边的元素值
#         L=[1]+[sum(L[i:i+2]) for i in range(0,len(L)-1)]+[1]
#         yield L
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break


# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
#
# def char2num(s):
#    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# print(list(map(char2num, '13579')))
