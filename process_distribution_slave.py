# encoding=utf-8
__author__ = 'Kaiming'
Date = '2015/9/16 0016'

import time
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager

class QueueManager(BaseManager):
    pass


# 只从网络上获取Queue
QueueManager.register('get_task_queue')
QueueManager.register('gey_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'  # 连接本机
print('Connct to server %s...' % server_addr)

# 端口和严恒吗保持和master设置的一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# 从网络连接
m.connect()

# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n, n * n))
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')

# 处理结束
print('slave exit.')
