__author__ = 'Kaiming'



# 调用系统模块
import os

# 查看os的基本信息

# print(os.name)      #查看系统的类型，nt说明是windows
# #print(os.uname())   #查看系统用户的信息，只支持linux类系统
#
# print(os.environ)        #查看系统的环境变量
# print(os.environ.get('PATH')) #查看某个具体的环境变量

# os.path是和路径相关的操作，os则是文件目录的操作

print(os.path.abspath('.'))  # 打印当前目录绝对路径
dir_path = os.path.join('D:/', 'testdir')  # 先生成路径，使用join来生成路径可以屏蔽系统对路径处理方式不同的问题
print(dir_path)

split_path = os.path.split('/Users/michael/testdir/file.txt')  # 用于分离路径，这个只对字符串操作
print(split_path)
get_suffix = os.path.splitext('/path/to/file.txt')
print(get_suffix)

print(type(os.path.splitext('/path/to/file.txt')))  # 看一下ps.path.splittext的返回类型

# os.mkdir(dir_path)  #按照路径创建目录
# os.rmdir(dir_path)  #删除目录
#
# os.rename('D:/test.txt','D:/test.py')
# os.remove('D:/test.py')


# copyfile()函数在shutil中，还有很多使用的函数在shutil中可以作为os的辅助
# import shutil
# shutil.copyfile('D:/banner.jpg','C:/banner.jpg')    #目的地址也要文件名


# 过滤文件

# 一行代码列出所有目录
dir_list = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dir_list)


# 一行代码列出所有.py后缀的文件; 后面取返回元祖的第二个元素
files_py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == 'py']
print(files_py)
