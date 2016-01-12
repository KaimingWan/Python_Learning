__author__ = 'Kaiming'


# 装饰器按照装饰函数是否带参数和被装饰函数是否带参数可以分为4类


import functools


# P1——两者都不带参数

# 定义装饰函数，被装饰函数作为参数
def decorator_one(f1):
    print('start')
    print('call ' + f1.__name__)
    print('end')
    # 被装饰函数不带参数，返回被装饰函数,最外层函数必须接受一个返回函数
    return f1


@decorator_one
# 采取和上面定义不同的名字，否则会出错
def f1():
    pass


f1()


# P2——装饰函数不带参数，被装饰函数带参数

# 定义装饰函数，被装饰函数作为参数
def decorator_two(f2):
    # 定义包装函数，用于传递给被装饰函数当做参数,使用可变参数和关键字参数可以提升灵活性
    def wrapper_two(*args, **kw):
        print('start')
        print('call' + f2.__name__)
        f2(*args, **kw)
        print('end')

    # 这里的return返回的是decorator_two这个函数的返回值
    return wrapper_two


@decorator_two
def f2(s):
    print(s)


'''流程是:f2=decorator_two(f2),然后运行wrapper_two函数，在f2执行前后进行
处理,最后还要把函数最为一个返回值，这个是装饰函数要求的'''

f2('被装饰函数f2的参数')


# P3——装饰函数带参数，被装饰函数不带参数

# 装饰函数外层加一层函数，用来传递装饰函数的参数
def my_decorator_three(*args, **kw):
    # 这里才是装饰函数开始的地方，传入装饰函数参数f3
    def decorator_three(f3):
        #    @functools.wraps(f3) 这句在这里可加可不加，反正不会出现函数名字指定错误
        print('start')
        print('f3的装饰器函数自带参数为:', *args)
        print('call ' + f3.__name__)
        print('end')
        # 这里需要返回被装饰函数本身f3,当做
        return f3

    return decorator_three


'''注意P3的调用逻辑是f3=my_decorator_three(*args,**kw)(f3)(),最后的(f3)在这里是
使用前面的返回函数decorator_three(f3),可以完成装饰函数自带参数实现的功能，最后的()实际上
再使用不带参数的f3()函数本身完成被装饰函数本身的功能'''


# 这里采用最外层的函数
@my_decorator_three('my_decorator_three')
def f3():
    pass


f3()


# P4——装饰器函数和被装饰函数都带参数

# 这层传递的参数是装饰函数本身需要使用的参数
def my_decorator_four(*args_decorator, **kw_decorator):
    # 这一层函数传递需要被装饰的函数f4
    def decorator_four(f4):
        @functools.wraps(f4)
        # 这一层包装函数用于传递被装饰函数f4所需要的参数
        def wrapper(*args, **kw):
            print('start')
            print(f4.__name__ + ' is working')
            # 在这个函数内已经使用了带参数的被装饰函数f4，所以最后也不需要返回函数f4了
            f4(*args, **kw)
            print('end')

        return wrapper

    return decorator_four


'''P4的调用逻辑是f4=my_decorator_four(**args_decorator,**kw_decorator)(f4)(*args,**kw);这个逻辑比较长，首
先是他用最外层的函数，传递装饰函数需要的参数；然后用于最外层函数返回的函数是decorator_four()，所以
后面的(f4)实际上等价于decorator_four(f4),然后由于decorator_four函数的返回值是wrapper,所以(*args,**kw)
等价于wrapper(*args,**kw)'''


@my_decorator_four('my_decorator_four')
def f4(s):
    print(s)


f4('被装饰函数f4的参数')


# P5 课后习题，通过分析课后习题可以知道，需要设计一个装饰函数带可变参数，被装饰函数不带参数的装饰器

# 为了保持前后的统一性，函数名我就不用log了，而是用my_decorator_five代替log,f5代替f
def my_decorator_five(*args, **kw):
    def decorator_five(f5):
        print(*args)
        print('begin call')
        # 在函数中使用了被装饰函数，就不用再返回这个函数了，因为已经在这被执行过了
        f5()
        print('end call')

    return decorator_five


@my_decorator_five()
def f5():
    pass


@my_decorator_five('execute')
def f5():
    pass


'''P5的装饰器函数调用逻辑实际上和P3类似，f5=my_decorator_five(*args,**kw)(f5),好P3的差别就是最后不用加()，因
为最后没有返回被装饰函数'''
