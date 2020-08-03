# Python 正则表达式
import re

string1 = 'This is Mute-xD`s test on regex with python'
print(re.match(r'Mute-xD', string1))
# re.match 起始位置开始匹配（None） flags= 正则标志位
print(re.search(r'Mute-xD', string1))
# re.search 扫描整个字符串并返回第一个成功的匹配  (<re.Match object; span=(8, 15), match='Mute-xD'>) flags= 正则标志位
print(re.search(r'Mute-xD', string1).group())  # Mute-xD
"""
re.match与re.search的区别
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配
"""
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串 repl : 替换的字符串，也可为一个函数
# string : 要被查找替换的原始字符串 count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配 flags : 编译时用的匹配模式，数字形式
string2 = '123-4567-8901 # 这是一个电话号码'
number = re.sub(r'#.*$', '', string2)
print(number)
print(re.sub(r'\D', '', number))


def double(matched):
    val = int(matched.group('value'))
    return str(val * 2)


string3 = 'ABC 1234 DEF 5678'
print(re.sub(r'(?P<value>\d+)', double, string3))

"""
正则表达式修饰符
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定
如 re.I | re.M 被设置成 I 和 M 标志
re.I  使匹配对大小写不敏感
re.L  做本地化识别（locale-aware）匹配
re.M  多行匹配，影响 ^ 和 $
re.S  使 . 匹配包括换行在内的所有字符
re.U  根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X  该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
"""
re.compile(r'(?P<value>\d+)')  # 将str(正则表达式)编译为对象
pattern = re.compile(r'\d+')
print(pattern.match('one12twothree34four'))  # None
print(pattern.match('one12twothree34four', 2, 10))  # None
match = pattern.match('one12twothree34four', 3, 10)  # <_sre.SRE_Match object at 0x10a42aac0>  match 对象

print(match.group())  # 12 匹配到的  or  match.group(0)
print(match.start())  # 3
print(match.end())  # 5
print(match.span())  # (3, 5)

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
match = pattern.match('Hello World Wide Web')  # <re.Match object; span=(0, 11), match='Hello World'>

print(match.group())  # Hello World
print(match.span())  # (0, 11)
print(match.group(1))  # Hello
print(match.span(1))  # (0, 5)
print(match.group(2))  # World
print(match.span(2))  # (6, 11)
print(match.groups())  # ('Hello', 'World')

pattern = re.compile(r'\d+')  # findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
print(pattern.findall('Mute 123 xD 456'))  # ['123', '456']
print(pattern.findall('Mute123xD456', 0, 10))  # ['123', '4']

it = re.finditer(r"\d+", "12a32bc43jf3")  # 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
for match in it:
    print(match)

# split 方法按照能够匹配的子串将字符串分割后返回列表
print(re.split(r'\W+', 'Mute, MutexD, MutexDD.'))  # ['Mute', 'MutexD', 'MutexDD', '']
print(re.split(r'(\W+)', 'Mute, MutexD, MutexDD.'))  # ['Mute', ', ', 'MutexD', ', ', 'MutexDD', '.', '']
print(re.split(r'\W+', 'Mute, MutexD, MutexDD.', 1))  # ['Mute', 'MutexD, MutexDD.']  maxSplit=1 最大分割次数
# 未找到的不会分割
re.RegexFlag  # re.compile() 返回 RegexObject 对象
re.MatchObject
# group() 返回被 RE 匹配的字符串 start() 返回匹配开始的位置 end() 返回匹配结束的位置 span() 返回一个元组包含匹配 (开始,结束) 的位置
