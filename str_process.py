__author__ = 'Kaiming'


# P1
def normalize(name):
    return str(name).capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# P2

def multipy(x, y):
    return x * y


def prod(L):
    return reduce(multipy, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# P3

from functools import reduce


# 小数点前的使用multipy函数
def multipy(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    s0 = s.split('.')
    s1 = s0[0]
    s2 = s0[1]

    # 小数点后的位数
    length = len(s2)

    return reduce(multipy, map(char2num, s1)) + reduce(multipy, map(char2num, s2)) / (10 ** length)


print('str2float(\'123.456\')=', str2float('123.456'))
