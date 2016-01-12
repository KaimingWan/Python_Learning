# encoding=utf-8
__author__ = 'Kaiming'
Date = '2015/9/15 0015'

import subprocess

# #调用外部方法采用subprocess.call(['method_name','args'])
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# 调用的外部方法接受输入采用communicate
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b' set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
