__author__ = 'Kaiming'


# print(1024*768);
#
# print(3>2);


# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,Lisa!'''
#
# print(n,f,s1,s2,s3,s4);

# 使用变量

#
# print('请输入您的名字');
# name=input();
#
# print('请输入您的分数');
# score=input();
#
# print('亲爱的%s,你的成绩是%s'%(name,score));



##使用list和tuple


# 设置一个朋友列表
# classmates=['Jack','John','Tommy'];
#
#
#
# print('我总共有%s个朋友'%len(classmates));
#
# print('我最喜爱的朋友是'+classmates[0]);
#
# #获取列表倒数第一个
#
# print('我最不喜欢倒数第一个朋友'+classmates[-1]);
#
# #添加一个朋友
# classmates.append('Pudding');

# 将一个朋友插入到第2个位置
# classmates.insert(2,'Two');

# print('第二个元素为'+classmates[2]);
#
# #删除最后个元素
#
# print(classmates);
# classmates.pop();
# print(classmates);
#
# #可以嵌套列表结构
#
# #tuple结构，理解成不可变的list
#
#
# #只有一个元素也要加一个逗号
# t=(1,)
#
# print(t[0]);



# 可以不加分号！！ 判断的冒号是不可以漏掉的
# age=2
#
# if age > 18:
#     print('您已经成年！')
#
# else: print('您还未成年！')


# 另外一个判断
# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')
#
#

##这里注意一下可以进行强制类型转化
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# 采用range()函数罗列连续整数

# sum=0
# for x in range(101):  #生成0-100的数字，range()是开区间，不要忘记冒号
#     sum = sum+x;
# print(sum);


# 使用while

# sum=0
# n=1
# while n<=100:
#     sum+=n
#     n+=1
# print(sum)


# key-value数据结构，比list效率高很多。list效率取决于list长度
#
# mydict={'Top1':100,'Top2':90,'Top3':60}
#
# #获取元素方法一，直接获取，当key不存在会报错
# print(mydict['Top1'])
#
# #获取元素方法二，get方法
# print(mydict.get('Top5'));
#
# #删除元素，不存在的key会报错
# mydict.pop('Top3')


# set数据结构保存不重复元素，通过add和remove函数来增删，set函数可以用&当符号来做交集补集等


# 使用自定义函数计算1+2+...+100
#
# n=input()
# def cal_sum(n):
#     sum = 0
#     n=int(n)
#     while n > 0:
#         sum += n
#         n-=1
#     return sum
#
#
# print(cal_sum(n))

# 可以有默认参数
# python根据缩进来判断代码块


#
# def power(x,n=2):
#     i=1
#     for i in range(n+1):
#         x*=x
#     return x
#
# print(power(3))
#
# print(power(3,3))

# 设置一个空对象
# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('End')
#     return L
#
# print(add_end([1,2,3]))


# 传递一个数据结构，传递一个列表或者tuple

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc([1, 2, 3]))

#
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum+=n*n
#     return sum
#
# print(calc(1,2))
#
# #把list和tuple当作参数提交给函数加*
#
# nums=[1,2,3]
# print(calc(*nums))


# 关键字参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# person('Kami',18,loc='Hangzhou',job='IT')
#
# kw={'city': 'Beijing', 'job': 'Engineer'}
# person('Kami',18,**kw)

#
# #命名关键字参数
# def person(name,age,*,city,job):
#     print(name,age,city,job)
#
# #命名关键字参数必须指明名字
# person('name',18,city='Beijing',job='IT')

# def f1(a, b, c = 0,*d,**kw):
#     print('a =', a, 'b =', b, 'c =', c ,'d =', d, 'kw =', kw)
# args = (1,2,3,4,5,6,7)
# kw = {'x': '##'}
# f1(*args,**kw)


# 汉诺塔问题解决

# def hanoi(n,A,B,C):
#     if n==1:
#         print(A,'-->',C)
#     else:
#         hanoi(n-1,A,C,B)#将前n-1个盘子从A移动到B上
#         hanoi(1,A,B,C)#将最底下的最后一个盘子从A移动到C上
#         hanoi(n-1,B,A,C)#将B上的n-1个盘子移动到C上
#
#
#
# n=int(input('请输入汉诺塔的层数：'))
# hanoi(n,'A','B','C')

# 切片操作，取list tuple的内容

# L=list(range(100))

# #取0,1,2三个数
# print(L[0:3])
# #取前十个数
# print(L[:10])
# #取后十个数
# print(L[-10:])
# #最后十个数不取
# print(L[:-10])
# #前十个数。每两个取一个
# print(L[:10:2])

# print(L[:10:2])

# #输出整个list
# print(L)

# #字符也可以操作
# L=list('Good')
# print(L[:4:2])


# dict对象的迭代,按照key顺序，不按照value顺序
# d={'a':1,'b':2,'c':3}
# for key in d:
#     print(key)

# #按照value顺序迭代
# for value in d.values():
#     print(value)

#
# for k,v in d.items():
#     print(v)

# 使用collections 模块的iterable类型判断
#
# from collections import Iterable
# print(isinstance('abc',Iterable))

# 使用enumerate(list)来把list变成索引结构

# for i,value in enumerate(['a','b','c']):
#     print(i,value)


# 循环生成式来生成[1*1,2*2,...]

# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)


# 列表生成式生成式来生成[1*1,2*2,...]
# L=[x*x for x in range(1,11) if x%2==0]
#
# print(L)


# 使用两层循环，生成全排列
# S=[m+n+k for m in 'Luo' for n in 'Meng' for k in 'Ting']
#
# Answer=''
# for i in range(2,6):
#     Answer+=S[i]
# print(Answer)

# 列出当前目录下的所有文件和目录名
# import os
#
# print(os.listdir('.'))
#
# d = {'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#     print(k,'=',v,' Bingo!')

# L = ['Hello', 'World', 18, 'Apple', None]
#
#
# K=[s.lower() for s in L if isinstance(s,str)]
# print(K)


# 一边循环一边计算使用generator

# 普通写法打印斐波那契数列

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         (a,b)=(b,a+b)
#         n=n+1
#     return 'done'
#
# fib(10)

# 包含yield的函数为generator

# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         (a,b)=(b,a+b)
#         n+=1
#     return 'done'


# #输出杨辉三角
# def triangles():
#     L=[1]
#     while(True):
#         yield L
#         L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# map函数使用
#
# def f(x):
#     return x*x
#
# r=map(f,[1,2,3,4,5])
#
# print(list(r))

# reduce函数，继续把结果和下一个元素套用函数

# from  functools import reduce
# def add(x,y):
#     return x+y
# reduce(add,[1,3,5,7,9])

# print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[123])
#
# def is_odd(n):
#     return n%2 == 1
#
# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])) )

# n=123
# f=456.789
# s1='Hello, world'
# s2='Hello, \'Adam\''
# s3=r'Hello, "Bart" '
# s4=r'''Hello,
# Lisa!'''
#
#
# list=[n,f,s1,s2,s3,s4]
#
# for x in range(5):
#     print(list[x])
