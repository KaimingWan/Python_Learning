# list tuple dict set 用法总结

#==============================list===========================
#list可添加删除，效果类似数组

#创建
classmates=['Michael','Bob'	,'Jack']


#查看
def checkList(classmates=[]):
	for i in range(len(classmates)):		#range的范围是[),结尾是开区间
		print(classmates[i])

print(classmates[-1])		#查看倒数的第一个元素

#修改
classmates.append('Adam')
classmates.insert(0,'Alan')
checkList(classmates)		
print(classmates)		#可以直接打印list
classmates.pop()		#删除尾部元素
classmates.pop(1)		#删除指定位置元素


#================================tuple===========================
#tuple一旦初始化后就无法修改

#创建
students=('s1',['s2','s3'])		#tuple中包含list的话是可变的
s=()		#空的tuple也可以

#查看
print(students[1][0])
print(students)



#================================dict============================
#dict就是用来保存键值对的,采用哈希的方式，查找较快,占用内存；key必须是不可变对象
#因此list就不能作为key

#创建
d={'s1':70,'s2':80,'s3':90}		#使用花括号

#查看
d['s1']
d.get('s1',-1)	#不存在key则会返回-1
d.get('s1')	#不存在返回none





#=====================================set==============================
#无序，不重复的集合。用一个没有重复的元素作为集合输入给set

#创建
s1=set([1,2,3])
se=set([2,3,4])

#查看
print(s1)

#修改
s1.add(5)
s1.remove(2)
print(s1)
