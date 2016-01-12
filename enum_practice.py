__author__ = 'Kaiming'

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

type(Enum)
type(Month)
print(isinstance(Month.Jan, Month))
print(isinstance(Month.Jan, Enum))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
