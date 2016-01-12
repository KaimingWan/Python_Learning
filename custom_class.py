__author__ = 'Kaiming'

'自己设计一个练习来使用这些定制类的特殊函数。我们这里首先自己编写一个采用埃氏筛法' \
'来计算素数的函数(使用filter的方式，在前面)，然后通过定制类使他支持迭代、切片、调用自己等特点'


class Prime(object):
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

    def __init__(self, max):
        # self.__max保存计算素数的上限值，也是最后出循环的条件
        self.__max = max

        # 初始化的Prime类只能处理[2,max+1]以内的素数
        self.__sequence = list(range(3, self.__max, 2))

        self.__count = 0

    def reset_prime(self):
        '用完self.__sequence之后需要用这个函数将self.__sequence初始化一下，避免再次调用出错'
        self.__sequence = list(range(3, self.__max, 2))
        self.count = 0

    def __str__(self):
        '''___str___这个特殊函数用于当执行print(函数名)的时候返回一些函数本身相关的信息
        __repr__这个特殊函数主要用于当直接使用 函数名 的时候返回一些函数本身的信息，这些
        返回的信息可以引入一些函数的成员变量，从而使得提供更多有用的信息'''
        return 'This is a class called Prime to process prime!'

    __repr__ = __str__

    def _not_divisible(self, i):
        '判断是否被整除，用于辅助埃氏筛法'
        return lambda x: x % i > 0

    def __iter__(self):
        '用于返回自己作为迭代'
        return self

    def __next__(self):

        if self.__count == 0:
            self.__count += 1
            return 2

        if self.__count == 1:
            self.__count += 1
            return 3

        # self.__sequence指向一个新的序列,经过_not_divisible函数处理后剔除了能被self.__sequence[0]整除的值
        self.__sequence = list(filter(self._not_divisible(self.__sequence[0]), self.__sequence))

        if len(self.__sequence) == 0:
            raise StopIteration()

        self.__count += 1
        return self.__sequence[0]

    # 得到n以内的素数
    def get_primes(self, n):
        if not isinstance(n, int):
            return ValueError('请输出大于1的数字')
        L = []
        if n == 1:
            return L
        if n == 2:
            L.append(2)
            return L
        for i in range(3, n, 2):
            self.__sequence = list(filter(self._not_divisible(self.__sequence[0]), self.__sequence))

            # 跳出循环的时候，添加2,3两个最前面的素数
            if len(self.__sequence) == 0:
                L.insert(0, 2)
                L.insert(1, 3)
                self.reset_prime()
                return L

            L.append(self.__sequence[0])

    def __getitem__(self, item):
        return self.get_primes(self.__max)[item]

    def __getattr__(self, item):
        '用户需要取得属性的时候做处理'
        if item == 'help':
            print('Prime类的帮助内容如下：XXXXX')


p = Prime(100)
print(p)
for x in p:
    print(x)

# 每次迭代过一次需要初始化一些实例变量比如count
p.reset_prime()


# 输出100以内的倒数第2到倒数第10的素数，每2个输出1个
print(p[-5::2])
