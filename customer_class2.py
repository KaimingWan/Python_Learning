class Square(object):		# 正方形类
	__count=0		#用于__next__方法中计数
	def __init__(self,x=1):		# x是边长，默认为1
		self.x = x

	def __str__(self):
		return '正方形对象 (边长为: %s)' % self.x	# 可以返回一些额外的属性信息

	__repr__ = __str__	# 简易方法，直接赋值给__repl__



	def __getitem__(self,x):		#先使得其能像list一样操作,返回的是指定边长的正方形对象

	# 要支持切片操作，__getitem__必须要判断传入的对象是int还是slice对象(3:5例如这样的)
		if isinstance(x,int):
			self.x = x
			return self
		if isinstance(x,slice):	#n是切片对象则有start,stop
			start = x.start
			stop = x.stop
			if start is None:
				start = 0

		# 定义一个list用于返回
		L=[]
		for i in range(stop):
			L.append(Square(i))
		return L



	def __iter__(self):
		return	self	# 迭代的就是自己本身（大多数情况都如此）

	def __next__(self):	#返回边长为1递增到边长为x的正方形对象
		self.__count+=1
		if(self.__count>self.x):
			raise StopIteration()		#这个退出__next__的条件一定要有
		s = Square(self.__count)	#产生一个边长为__count的Square对象
		return s




s = Square()
print(s[5])		#输出边长为5的正方形的面积
print('输出边长2至8的Square对象，间隔为1输出')
print(s[2:8:2])

print('开始遍历Square对象,输出边长小于其边长的所有Square对象')
square=Square(10)	#创建一个边长为10的正方形
for t in square:		# 遍历Square对象，在我们这里，遍历正方形意味着边长小于其边长的正方形对象全部输出
	print(t)	#输出每个Square对象的__str__信息


