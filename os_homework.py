__author__ = 'Kaiming'

import os
import pdb

class IO_dir(object):
    flag = False  # 类变量，用于在类全局内保存是否找到相应的文件

    def dir_l(self):
        '用于显示当前目录下所有文件和目录'
        list_all = os.listdir()  # listdir包括所有文件和目录,不加任何参数默认是当前目录下
        print('当前目录下的所有目录如下：')
        # 这里os.path.isdir不需要join,因为当前目录本来就有x
        list_dirs = [x for x in list_all if os.path.isdir(x)]
        print(list_dirs)

        print('当前目录下的所有文件如下：')
        list_files = [x for x in list_all if os.path.isfile(x)]
        print(list_files)

    def search_file(self, file_name, path):
        '用于在当前目录以及子目录下搜索相关的文件，并打印出它的路径,如果当前目录找到了，则不再进子目录寻找'
        file_list = []  # 如果是文件就直接放入文件list
        dir_list = []  # 如果是目录就直接放入目录list
        for x in os.listdir(path):
            # !!!这一句非常重要，因为isfile的判断需要完整的路径名，如果不加这句，isfile的参数只是单纯的一个名字，就会全部返回False
            # pdb.set_trace()     #调试 
            fullpath = os.path.join(path, x)        # path方法和x的名字连接在一起称为一个完整的路径
            if os.path.isfile(fullpath):
                file_list.append(x)
            else:
                dir_list.append(x)




        if file_name not in file_list:
            if len(dir_list) == 0:
                pass  # 如果当前目录找不到，并且也没子目录了，就可以到函数末尾了，不需要修改flag的值
            else:  # 当前目录没找到，子目录中寻找
                for child_dir in dir_list:      #在每个dir_list中寻找
                    if child_dir == '__pycache__':  # __pycache__是代码产生的二进制文件信息，因此不考虑对其进行搜索
                        return False
                    # 更新最新的路径,将要查找的子目录更新到child_path，切勿join到path，否则path目录下其他目录就无法被遍历。因为for循环每次都执行path.join。
                    child_path = os.path.join(path, child_dir)  
                    self.search_file(file_name, child_path)

        else:  # 如果找到文件
            print('[' + file_name + ']已经找到！')
            print('[' + file_name + ']的相对路径是：' + os.path.join(path, file_name))
            self.flag = True

        return self.flag

    def input_str(self):
        '用于接收用户的输入'
        print('请输入操作命令：')
        ops = str(input())
        return ops


t = IO_dir()    # 创建类实例
print('欢迎使用简易目录文件查看系统,退出系统请输入:exit')
print('------------------------------------------帮助说明------------------------------------------------')
print('（1）dir -l：查看当前目录下（执行该代码处）所有文件和目录')
print('（2）输入名字，会直接在当前目录下以及所有子目录下查找文件名包含指定字符串的文件(只搜索一个)，并打印出相对路径，不支持搜索目录！')
print('------------------------------------------END----------------------------------------------------')

ops = t.input_str()
while ops != 'exit':
    if ops == 'dir -l':
        t.dir_l()
    else:
        flag = t.search_file(ops, '.')  # 其他输入内容均看成是查找
        if flag is False:
            print('很遗憾，没有找到相应的文件！')
    ops = t.input_str()

print('感谢使用，再见！')
