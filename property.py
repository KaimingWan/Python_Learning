__author__ = 'Kaiming'


class Screen(object):
    # getter的作用
    @property
    def width(self):
        return self.__width

    # setter的作用
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('请输入数字')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('请输入数字')
        else:
            self.__height = value

    @property
    def resolution(self):
        return self.width * self.height


# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
