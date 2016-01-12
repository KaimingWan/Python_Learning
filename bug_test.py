__author__ = 'Kaiming'

import logging

# log的级别有debug,info,warning,error 四钟级别，尅根据不同级别来输出信息，比使用assert和print来调试要科学好用
logging.basicConfig(level=logging.INFO)  # 配置下logging使得其支持输出屏幕信息


class Foo(object):
    '这是一个会出错的程序'

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




import unittest			# 使用inittest模块 进行单元测试




class Test_Foo(unittest.TestCase):	#继承unittest.TestCase
    '这是一个测试程序'

    def test_bar(self):		#名字以test_xxx命名
        f = Foo()
        f.bar()
        self.assertRaises(ValueError)

class TestDict(unittest.TestCase):	#适合数据库连接和释放。。

    def setUp(self):			#setUp方法可以让你任意一个test_xxx方法使用前都使用setUp方法
        print('setUp...')

    def tearDown(self):			#tearDwwn方法可以让你任意一个test_xxx方法使用结束后使用tearDown方法
        print('tearDown...')


if __name__ == '__main__':		#__name__ == '__main__'表示直接通过python xx.py来运行该文件而不是通过import
    unittest.main()				#执行所有单元测试

