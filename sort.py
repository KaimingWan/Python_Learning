# __author__ = 'Kaiming'
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def by_name(t):
#     return t[0].lower()
#
#
# def by_score(t):
#     return t[1]
#
#
# # 按照名字排序（不考虑大小写）
# L2 = sorted(L, key=by_name)
# print(L2)
#
#
# # 按分数排序
# L2 = sorted(L, key=by_score, reverse=True)
# print(L2)

L = [[1, 2], [3, 4], [5, 6], [7, 8]]
print([(lambda x: x[0] * x[0] + x[1] * x[1])(x) for x in L])
