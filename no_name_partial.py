# =====================================匿名函数==========================
f = lambda x: x * x  # 冒号左边是参数，右边是函数实现
print(f(3))


# ======================================偏函数=============================
# new_func=functools.partial(func,*args,**kw),args、**kw就好比给原func函数传入了确定的参数！


# ===============================高阶函数map,reduce,filter,sorted=======================


# ---------------map-------------
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])  # map函数的第一个参数接受一个函数，后面的每一项都用这个map操作
print(list(r))  # 打印map函数的结果可以用list，因为它有很多处理结果


# -------------reduce-----------
from functools import reduce


def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])  # reduce和map的区别是每次使用函数后的结果作为下一次的输入


# ----------filter----------------
# filter也是对每一项套用函数，但是会剔除一些不满足条件的结果

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))		# filter是一个惰性序列，返回的是迭代器

# ---------sorted---------------------

# key 表示按照什么排序,reversed表示是否要反向排列
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
