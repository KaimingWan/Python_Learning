__author__ = 'Kaiming'


# #P1
# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello '+name)
#
#
#
# h = Hello()
# h.hello()
#
# print(type(Hello))



# #P2
# def fn(self,name='world'):
#     print('Hi '+name)
#
#
# #使用type来生成新的类Hello_world
# Hello_world=type('Hello_world',(object,), dict(new_hello=fn))
# h = Hello_world()
# h.new_hello()


# #P3

# class ListMetaclass(type):
# object的特殊方法，用来控制创建类
# __new__()方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的名字；
#
# 类继承的父类集合；
#
# 类的方法集合。

#     def __new__(cls, name, bases, attrs):
#
#         attrs['add'] = lambda self, value: self.append(value)
#
#         for k,v in attrs.items():
#             print(k,v)
#         return type.__new__(cls, name, bases, attrs)
#
# #这里告诉类模板是基于list来创建类
# class MyList(list,metaclass=ListMetaclass):
#     pass
#
#
# L = MyList()
# L.add(list('Looks good!'))
# print(L)



# P4 使用元类来创建一个建议的ORM框架






class Field(object):
    '负责保存数据库表的字段名和字段类型'

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        # name保存子类域的类型
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 这个就是一个类模板，用来实现一些魔法
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除已经有的属性，避免造成类属性和实例属性之间的冲突
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)


# 需要用元类创建的类Model类

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        # 把Model类利用dict的__init__初始化
        super(Model, self).__init__(**kw)

    # 返回相应key的value
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            # 从映射表里面获取值的名字
            fields.append(v.name)
            # 用?来表示参数
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
