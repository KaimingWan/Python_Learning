# encoding=utf-8
__author__ = 'Kaiming'
Date = '2015/9/15 0015'

import random
import queue
from multiprocessing.managers import BaseManager


# 发送任务的队列
task_queue = queue.Queue()

# 接受结果的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


# 把两Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=task_queue)
QueueManager.register('get_result_queue', callable=result_queue)

# 绑定端口5000，设置验证码为'abc'，这里验证信息要byte string
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列读取数据
print('Try get results')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

# 关闭
manager.shutdown()
print('master exit')
