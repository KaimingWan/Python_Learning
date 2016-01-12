class Student(object):					# 括号内是继承object

    def __init__(self, name, score):		# 和java构造器一样的功能
        self.__name = name			# 双下划线表示私有变量
        self.__score = score


class Animal(object):

    def run(self):
        print('Animal is running!')


class Dog(Animal):

    def run(self):
        print('Dog is running')


class Cat(Animal):

    def run(self):
        print('Cat is running')


def start_to_run(animal):  # python的多态比较特别，不需要很强的继承关系，因为本来就是弱类型
    animal.run()

dog = Dog()
cat = Cat()

start_to_run(dog)
start_to_run(cat)
