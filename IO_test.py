__author__ = 'Kaiming'


# P1 打开文件、读文件、关闭文件的典型方法

try:
    f = open('./test.txt', 'r')
    print(f.read())

finally:
    if f:
        f.close()


# P2 推荐的简洁写法，不必显式的关闭文件描述符
# open返回的对象在python中称作file-like 对象，可以是字节流、网络流、自定义流等
with open('./test.txt', 'r') as f:
    # 按行读取
    for line in f.readlines():
        print(line.strip())

# P3 直接读取二级制的图片、视频文件

# with open('D:/banner.jpg','rb') as f2:
#     for line in f2.readlines():
#         print(line.strip())


# P4 可以指定编码读取相应的数据,还可以忽略非法编码

with open('./test.txt', 'r', encoding='gbk', errors='ignore') as f3:
    for line in f3.readlines():
        print(line.strip())

# P5 写文件的流程和读文件是一样的 代开文件、写入内容、关闭文件

# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newlines mode (deprecated)
# with open('D:/test12.txt','a+') as f4:
#     for line in f4.readlines():
#         print(line.strip())
#     f4.write('a new line2!')



# P6 StringIO和BytesIO分别对字符串和二进制内容进行内存的读写


from io import StringIO # 类似java里面的字符流

f1 = StringIO()
f1.write('Hello World!')
s = f1.getvalue()  # 用getvalue才能获取值，不能用readlines()
print(s)

from io import BytesIO #类似java里面的字节流，处理二进制数据
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()		# 可以用read方法像读文件一样读取
