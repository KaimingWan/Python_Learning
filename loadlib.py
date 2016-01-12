__author__ = 'Kaiming'


## 引入外部文件 方法1，每次使用外部文件类和函数还要写上文件名.函数名
# import mylib
#
# h = mylib.Hello()
# h.sayHello()


# 引入外部文件方法2

from mylib import Hello

h = Hello()
h.sayHello()
