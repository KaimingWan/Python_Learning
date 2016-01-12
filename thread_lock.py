# encoding=utf-8
__author__ = 'Kaiming'
Date = '2015/9/15 0015'


# 线程之间共享资源，因此为了避免由于线程执行顺序造成的数据异常，要加锁（局部变量是线程独有的，不必加锁）

# 由于历史遗留问题，多线程的python程序无法利用多核

import threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 修改前需要先获取锁
        lock.acquire()
        try:
            # 进行改动
            change_it(n)
        finally:
            # 最后一定要释放锁，要不然死锁了
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
