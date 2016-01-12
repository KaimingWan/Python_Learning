# coding=utf-8
__author__ = 'Kaiming'

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 只有在父进程里面，才会执行以下的内容
if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 通过这个函数来生成子进程，第一个参数指定子进程运行的内容，第二个参数指定参数
    print('child process will start!')
    p.start()  # 启动进程
    p.join()  # join方法用于进程同步，等待进程执行完，再执行下面的代码
    print('child process end.')


# 使用进程池，批量创建进程
