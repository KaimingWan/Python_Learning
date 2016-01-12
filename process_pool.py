# encoding=utf-8
__author__ = 'Kaiming'

from multiprocessing import Pool
import os
import time
import random


def long_tine_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 同时跑4个进程
    for i in range(5):
        p.apply_async(long_tine_task, args=(i,))
    print('Waiting for all subprocesses done..')
    p.close()
    p.join()
    print('All subprocesses done.')
