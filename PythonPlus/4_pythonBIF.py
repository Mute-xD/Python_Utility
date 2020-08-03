
# abs() 函数返回数字的绝对值
print("abs(-45) : ", abs(-45))  # 45
print("abs(100.12) : ", abs(100.12))  # 100.12

# dict() 函数用于创建一个字典
dict()  # {}
dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # {'three': 3, 'two': 2, 'one': 1}
dict([('one', 1), ('two', 2), ('three', 3)])  # {'three': 3, 'two': 2, 'one': 1}

# help() 函数用于查看函数或模块用途的详细说明
help(list.append)

# min() 方法返回给定参数的最小值，参数可以为序列
min(80, 100, 1000)  # 80

# setattr() 函数对应函数 getattr(),用于设置属性值,该属性不一定是存在的
class A:
    name = 'mute'
a = A()
setattr(a, 'age', 20)
print(a.age)  # 20

# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
# 元素除了是 0、空、False 外都算 True
all(['a', 'b', 'c', 'd'])  # True
all(['a', 'b', '', 'd'])  # False

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
dir()  # ['A','__builtins__','__doc__','__file__','__loader__','__name__','__package__','a']

# hex() 函数用于将一个指定数字转换为 16 进制数
hex(255)  # '0xff'

# next() 返回迭代器的下一个项目,要和生成迭代器的iter() 函数一起使用
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
myslice = slice(5)
arr = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[myslice]  # [0, 1, 2, 3, 4]

# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True
any(['a', 'b', '', 'd'])  # True
any([0, '', False])  # False

# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
divmod(8, 2)  # (4, 0)
divmod(7, 2)  # (3, 1)

# id() 函数返回对象的唯一标识符，标识符是一个整数  CPython 中 id() 函数用于获取对象的内存地址
a = 'mute'
id(a)

# sorted() 函数对所有可迭代的对象进行排序操作
sorted([5, 2, 3, 1, 4])  # [1, 2, 3, 4, 5]

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)  # 1 one    2 two    3 three

# input() 函数接受一个标准输入数据，返回为 string 类型
a = input("input:")  # input:123
type(a)  # <class 'str'>

#  staticmethod 返回函数的静态方法,该方法不强制要求传递参数
class C:
    @staticmethod
    def func():
        print('mute');
C.func()  # mute  无需实例化

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
x = 7
eval('3 * x')  # 21

# int() 函数用于将一个字符串或数字转换为整型
int(3.6)  # 3
int('12',16)  # 18    （16进制）

# open() 函数用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError
# 使用 open() 函数一定要保证关闭文件对象，即调用 close() 函数
# 实例略

# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
# type() 不会认为子类是一种父类类型，不考虑继承关系  isinstance() 会认为子类是一种父类类型，考虑继承关系
a = 2
isinstance (a,int)  # True
isinstance (a,(str,int,list))  # True

# sum() 方法对系列进行求和计算
sum([0,1,2])  # 3
a = np.array([[1,2],[3,4]])
np.sum(a, axis=1, keepdims=True)  # array([[3], [7]])
np.sum(a, axis=1)  # array([3, 7])

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中
def isOdd(n):
    if n % 2 is 1:
        return True
tmpList = filter(isOdd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmpList)  # [1, 3, 5, 7, 9]

# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))  # True

# pow() 方法返回x的y次方的值
math.pow(100, 2)  # 1000.0

# super() 函数是用于调用父类(超类)的一个方法
class A:
    def add(self, x):
        y = x + 1
        print(y)
class B(A):
    def add(self, x):
        super().add(x)
b = B()
b.add(2)  # 3

# iter() 函数用来生成迭代器
list1 = [1, 2, 3]
for i in iter(list1):
    print(i)  # 1  2  3
# print() 方法用于打印输出，最常见的一个函数
print("www","mutexxd","cn",sep=".")  # www.mutexxd.cn
print("Loading",end = "")
for i in range(5):
    print(".",end = '',flush = True)
    time.sleep(0.5)  # 虚假的loading

# callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功
# 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True
class B:
    def __call__(self):
        print('callable')
callable(B)  # True
b = B()
callable(b)  # True

# format() 函数增强了字符串格式化的功能
"{1} {0} {1}".format("hello", "world")  # 'world hello world'

# len() 方法返回对象（字符、列表、元组等）长度或项目个数
str = "mute"
len(str)  # 4

# property() 函数的作用是在新式类中返回属性值
class C:
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
class Parrot:
    def __init__(self):
        self._voltage = 100000
    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self, val):
        self._voltage = val
    # @voltage.getter
    # def voltage(self):
    #     return self._voltage
parrot = Parrot()
print(parrot.voltage)  # 只读属性
parrot.voltage = 100
print(parrot.voltage)

# chr() 用一个整数作参数，返回一个对应的字符
chr(0x30)  # 0
chr(97)  # a

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
a = frozenset(range(10))  # frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表
# list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表
list(range(0, 30, 5))  # [0, 5, 10, 15, 20, 25]
list(range(5))  # [0, 1, 2, 3, 4]
for i in range(5):
    print(i)  # 1   2   3   4   5

# vars() 函数返回对象object的属性和属性值的字典对象
print(vars(Parrot))  # ...__init__ at 0x000002273421C4C8>, 'voltage': <property object at 0x00000227342CBE08>...

# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
class A(object):
    bar = 1
    def func1(self):
        print ('func1')
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()
A.func2()

# getattr() 函数用于返回一个对象属性值
a = A()
getattr(a, 'bar')  # 1
getattr(a, 'bar', 'NotFound')  # NotFound

# locals() 函数会以字典类型返回当前位置的全部局部变量
def func(arg):
    temp = 1
    print(locals())
    return 0
func(5)  # {'arg': 5, 'temp': 1}

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
a = [1,2,3]
b = [4,5,6]
zippedList = list(zip(a,b))  # [(1, 4), (2, 5), (3, 6)]
a1, a2 = zip(*zip(a,b))
list(a1)  # [1, 2, 3]
list(a2)  # [4, 5, 6]

# globals() 函数会以字典类型返回当前位置的全部全局变量
# 实例略

# map() 会根据提供的函数对指定序列做映射
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
def square(x) :
    return x ** 2
map(square, [1, 2, 3, 4, 5])  # [1, 4, 9, 16, 25]

# reversed 函数返回一个反转的迭代器
str = 'mute'
reversed(str)  # 'etum'

# __import__() 函数用于动态加载类和函数 如果一个模块经常变化就可以使用 __import__() 来动态载入

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
complex(1, 2)  # 1 + 2j
complex("1-2j")  # 1 - 2j  注意无空格

# hasattr() 函数用于判断对象是否包含对应的属性
class B:
    x = 10
b = B()
hasattr(b, 'x')  # True
hasattr(b, 'c')  # False

# max() 方法返回给定参数的最大值，参数可以为序列
max(80, 100, 1000)  # 1000

# round() 方法返回浮点数 x 的四舍五入值，准确的说保留值将保留到离上一位更近的一端（四舍六入）  精度要求高的，不建议使用该函数
round(70.23456)  # 70
round(80.264, 2)  # 80.26

# delattr 函数用于删除属性
class B:
    x = 100
b = B()
delattr(B, 'x')
# 相当于
del B.x

# hash() 用于获取取一个对象（字符串或者数值等）的哈希值  常用作校验
#
print(hash('mute'))
print(hash('mutexxd'))

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
strSet = set('mutexxxd')  # {'m', 'd', 'x', 'u', 't', 'e'}

# EOF
