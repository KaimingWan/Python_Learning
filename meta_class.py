# 元类的作用:
# 1.拦截类的创建
# 2.修改类
# 3.返回修改之后的类

#====================元类定义方法一：使用metaclass属性绑定一个函数=======================
#__metaclass__在类外面，那么在整个文件中的类都会使用元类来创建，如果在类里面则只有相应的类用元类创建


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    attrs = ((name, value) for name, value in future_class_attr.items()
             if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)



class Foo(object,metaclass=upper_attr):
    name = 'test meta class'

print(hasattr(Foo, 'name'))
# 输出: False
print(hasattr(Foo, 'NAME'))
# 输出:True


#===================元类定义使用方法二：使用metaclass属性绑定一个元类（继承type）=================
class UpperAttrMetaclass(type):
    # __new__ 是在__init__之前被调用的特殊方法

    # __new__是用来创建对象并返回之的方法

    # 而__init__只是用来将传入的参数初始化给对象

    # 你很少用到__new__，除非你希望能够控制对象的创建

    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__

    # 如果你希望的话，你也可以在__init__中做些事情
	def __new__(cls, name, bases, dct):  # 这里的cls就指的是自己UpperAttrMetaclass
		attrs = ((name,value) for name,value in dct.items() if not name.startswith('__'))
		uppercase_attr = dict((name.upper(),value) for name,value in attrs)
        # 调用父类特殊方法(一般是构函数)的方式:super(名字,类对象).__new__或者__init__
		return super(UpperAttrMetaclass,cls).__new__(cls,name, bases, uppercase_attr)

# 子类只要再继承UpperAttrMetaclass即可
class TestUpperAttr(metaclass=UpperAttrMetaclass):			#将元类赋值给metaclass属性
    attr = 'hello world'

print(hasattr(TestUpperAttr, 'attr'))
# 输出: False
print(hasattr(TestUpperAttr, 'ATTR'))
# 输出:True




#==================元类使用案例======================


# #P1


class Hello(object):

    def hello(self, name='world'):
        print('Hello ' + name)


h = Hello()
h.hello()

print(type(Hello))


# #P2
def fn(self, name='china'):
    print('Hi ' + name)

 # 使用type来生成新的类Hello_world
Hello_world = type('Hello_world', (object,), dict(new_hello=fn))
h = Hello_world()
h.new_hello()


# #P3


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
class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):

        attrs['add'] = lambda self, value: self.append(
            value)		# attrs是属性和函数合集，其中的'add'是一个用lambda声明的匿名函数

        for k, v in attrs.items():
            print(k, v)
        return type.__new__(cls, name, bases, attrs)
#
# #这里告诉类模板是基于list来创建类


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(list('Looks good!'))
print(L)


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
        super(StringField, self).__init__(name, 'varchar(100)')		# 调用父类的方法


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 这个就是一个类模板，用来实现一些魔法
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)  # model类就是用户自己定义的模型类，现在还没和关系对象进行关联
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):		# 将用户自己定义的模型类的属性保存到一个map对象里
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除已经有的属性，避免造成类属性和实例属性之间的冲突
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)

# 在ModelMetaclass中，一共做了几件事情：

# 排除掉对Model类的修改；

# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中
# 同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

# 把表名保存到__table__中，这里简化为表名默认为类名。

# 在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。


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

        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
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
