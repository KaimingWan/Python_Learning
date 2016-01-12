__author__ = 'Kaiming'

import logging

# log的级别有debug,info,warning,error 四钟级别，尅根据不同级别来输出信息，比使用assert和print来调试要科学好用
logging.basicConfig(level=logging.INFO)  # 配置下logging使得其支持输出屏幕信息


class Foo(object):
    '这是一个会出错的程序，用于复习使用异常处理'

    def foo(self, s):
        n = int(s)
        if n == 0:
            raise ValueError('invalid value: %s' % s)
        return 10 / n

    def bar(self):
        try:
            self.foo('0')
        except ValueError as e:
            print('ValueError!')
            logging.info("出错啦！！")
            logging.exception(e)
            # raise


f = Foo()
f.bar()

print('END')
