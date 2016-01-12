# =====================try-catch使用======================
try:
    print('try...')
    r = 10 / 0
    print('result:', r)			
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


#==============使用logging记录错误，可以"打印错误堆栈信息"同时使得程序继续执行====
import logging
try:
    print('try...')
    r = 10 / 0
    print('result:', r)			
except Exception as e:		
    logging.exception(e)
finally:
    print('finally...')
print('END')



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

#=============自己抛出错误，会导致后面的程序不运行=================
# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)		# 自己抛出错误
#     return 10 / n

# foo('0')

#===============使用断言来代替print===========
def fooAssertion(s):
    n = int(s)
    assert n != 0, 'n为0，出错!'
    return 10 / n

def main():
    print('fooAssertion')
    fooAssertion('0')

main()