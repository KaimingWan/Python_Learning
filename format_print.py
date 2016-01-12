#使用str.format()函数

#使用'{}'占位符
print('I\'m {},{}'.format('Hongten','Welcome to my space!'))

print('#' * 40)

#也可以使用'{0}','{1}'形式的占位符
print('{0},I\'m {1},my E-mail is {2}'.format('Hello','Hongten','hongtenzone@foxmail.com'))
#可以改变占位符的位置
print('{1},I\'m {0},my E-mail is {2}'.format('Hongten','Hello','hongtenzone@foxmail.com'))

print('#' * 40)

#使用'{name}'形式的占位符
print('Hi,{name},{message}'.format(name = 'Tom',message = 'How old are you?'))

print('#' * 40)

#混合使用'{0}','{name}'形式
print('{0},I\'m {1},{message}'.format('Hello','Hongten',message = 'This is a test message!'))

print('#' * 40)

#下面进行格式控制
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))