__author__ = 'Kaiming'

import json

# 序列化pickle使用局限比较多，一般涉及传输的时候都序列化成json比较好
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# 序列化 通过dumps将python对象序列成一个json对象(json对象可以理解为一个字符串)
d = dict(name='Bob', age=20, score=80)
print(json.dumps(d))


# 反序列化，通过loads将json对象反序列化成一个dict对象,注意json对象里面的字符串都用双引号

json_str = '{"name":"Jack","age":18,"score":88}'
print(json.loads(json_str))


# 对类对象进行序列化操作

# 需要一个转换函数将类转化成dict对象(如果没有__slot__变量的可以用另外一种方法)
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score

    }


print(json.dumps(s, default=student2dict))

# 偷懒方法，一般没有__slot__的类都可以使用这种偷懒的方法
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 把类json对象反序列成类对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json_str, object_hook=dict2student))
