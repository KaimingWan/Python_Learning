# ============================位置参数=====================
#位置参数就是平常很常见的形参
def pwoer_0(x):		#此处的x就是位置参数
	return x*x


#============================默认参数=======================
def power_1(x,n=2):	#默认参数
	s=1
	while n>0:
		n=n-1
		s*=x
	return s

print(power_1(3))

def add_end(L=None):		# ！！！默认参数必须指向不变对象，否则重复使用函数会出错
    if L is None:
        L = []
    L.append('END')
    return L


#======================可变参数================================
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

num=[1,2,3]
calc(*num)	#可以通过这种方式传递list



#=====================关键字参数===========================
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#

def person(name, age, **kw):		#kw即使关键字参数
    print('name:', name, 'age:', age, 'other:', kw)

person('bob', 35,city='beijing')


#=====================命名关键字参数======================
#效果同关键字参数一样，只不过规定了接受的参数的key的名字
def person(name, age, *, city, job):		#采用一个*来分隔位置参数和命名关键字参数
    print(name, age, city, job)