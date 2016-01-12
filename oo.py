__author__ = 'Kaiming'


class Hello:
    # 构造函数
    def __init__(self, name):
        self._name = name

    def sayHello(self):
        print("hello {0} python".format(self._name))


h = Hello("Kami")
h.sayHello()


# 继承

class Hi(Hello):
    # 自己本身的构造方法
    def __init__(self, name):
        # 需要执行父类的构造函数
        Hello.__init__(self, name)

    def sayHi(self):
        print("Hi {0}".format(self._name))


h1 = Hi("Jack")
h1.sayHi()
