__author__ = 'Kaiming'

import functools
from types import MethodType

'''一个练习作业，设计一个学生类，他有三个子类，分别是三个不同国家的学生类，每个类有个成员方法speak可以说自己国家的话，通
过这些类和成员方法和成员属性来复习类的方法覆盖和多态，以及学习使用__slot__特殊变量来限定成员属性，以及使用types.MethType()
来实现增加函数的功能'''

'学生类'


class Student(object):
    # 注意，即使是函数也需要提前给slots，否则无法额外再添加函数
    __slots__ = ('name', 'sex', 'math_score', 'history_score')

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    # 该函数调用成员函数speak用于完成多态
    def start_speak(self, stu):
        stu.speak()


# 不是类当中的方法,但是这里一定需要加self，这样才能添加到类当中成为成员方法
def speak(self, s='Nothing to say!'):
    print('Start to say something:')
    print(s)


'中国学生类'


class Chinese_stu(Student):
    # 覆盖speak方法

    def speak(self, s='Nothing to say'):
        print('Start to say Chineses:')
        print(s)


'英国学生类'


class English_stu(Student):
    # 覆盖speak方法

    def speak(self, s='Nothing to say'):
        print('Start to say English:')
        print(s)


'日本学生类'


class Japenese_stu(Student):
    # 覆盖speak方法

    def speak(self, s='Nothing to say'):
        print('Start to say japenese:')
        print(s)


'使用__slot__和types.MethType()函数'
stu = Student('Kami', '男')
print(stu.name)
stu.math_score = 70
stu.history_score = 80

# stu.chinese_score=100  这一句无法执行，因为没有chinese_score这个属性


# 这里增加的是类的函数而不是实例的函数，需要注意
Student.speak = MethodType(speak, Student)
stu.speak('Hello World')

'使用子类来构建偏函数'
chinese_stu = Chinese_stu('小凯', '男')
print(chinese_stu.name)
chinese_stu.speak('我热爱Python!')

# ------用子类的一个speak函数来创建偏函数------
say_hello = functools.partial(chinese_stu.speak, '你好，偏函数')
say_hello()

'应用类的多态特性'

# 生成日本和英国学生实例
japanese_stu = Japenese_stu('安倍晋三', '不明')
english_stu = English_stu('Jack', 'man')


stu.start_speak(stu)
stu.start_speak(chinese_stu)
stu.start_speak(japanese_stu)
stu.start_speak(english_stu)


# 使用@property和@xxx.setter 可以方便直接使用属性，而不是调用函数
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=60
print(s.score)
# s.score=9999