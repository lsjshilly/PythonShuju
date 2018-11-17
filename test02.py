# 函数有位置参数课关键字参数，关键字参数必须位于位置参数之后
# 其中的z为关键字参数


def my_funciton(a, b, z=1):
    if a > b:
        print(a * b + z)
    else:
        print(a - b + z)


my_funciton(5, 2, z=5)
my_funciton(2, 5, 3)
my_funciton(2, 5)

# 命名空间作用域局部函数
# 任何在函数中赋值的变量默认都是被分配到局部命名空间中的。局部命名空间是在函数创建时被调用的，函数参数会立即填入该命名空间
a = []


def func():
    for i in range(5):
        a.append(i)


func()
print(a)  # 打印的不是空列表

b = 5


def func2():
    b = 7


func2()
print(b)  # 打印值为5


def func3():
    global b
    b = 7


func3()
print(b)  # 打印值为7

# /*******************************************************************/
# 多值返回方式 可以返回元组或字典


def fun4():
    a = 5
    b = 6
    c = 7
    return a, b, c


a, b, c = fun4()
print(a, b, c)


def fun5():
    a = 5
    b = 6
    c = 7
    return {'a': a, 'b': b, 'c': c}


gg = fun5()
print(gg['a'])

states = [
    ' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
    'south carolina##', 'West virginia?'
]

import re


def clean_data(strings):
    data = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        data.append(value)
    return data


data = clean_data(states)
print(data)

# 第二种方法则试将所有要做的操作放到一个列表中


def remove_punctuation(value):
    return re.sub('[?#!]', '', value)


ops = [str.strip, remove_punctuation, str.title]


def clean_data2(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


data2 = clean_data2(states, ops)
print(data2)

# map函数，用于在一组数据上应用一个函数

for x in map(remove_punctuation, states):
    print(x)

# lambada 匿名函数
equiv_anon = lambda x: x**2
print(equiv_anon(3))


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [1, 4, 5, 3, 6]
some_list = apply_to_list(ints, lambda x: x**2)
print(some_list)

states.sort()
print(states)

# 柯里化：部分参数应用


def add_numbers(x, y):
    return x + y


add_five = lambda y: add_numbers(5, y)

# 内置的functools模块可以调用partial函数，将上述过程简化
from functools import partial
add_five = partial(add_numbers, 5)

# 生成器
# 一般的函数执行之后会返回单个值，而生成器则是以延迟的方式返回一个值序列
# 即毎返回一个值后暂停，直到下一个值请求时再继续
# 创建一个生成器，只需要将函数中的return 替换为 yeild即可


def squres(n=10):
    print("生产从1到{0}的平方数".format(n))
    for i in range(n):
        yield i**2


b = squres(10)
for x in b:
    print(x, end=" ")

# 生成器表达式  类似于列表，字典集合推导式的生成器
gen = (x**2 for x in range(100))

# 与下面的等价


def _make_gen():
    for x in range(100):
        yield x**2


gen = _make_gen()

# 生成器表达式也可以取代列表推导式，作为函数参数
print()
t = sum(x for x in range(201))
print("从1加到200的和为：%d" % t)

d = dict((i, i**2) for i in range(10))
print(d)

import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))

# 异常处理 可用元组包含多个异常


def attempt_float(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return x


bb = attempt_float((1, 2))
print(bb)
'''
try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()
'''


def attempt_to_float(x):
    try:
        dd = float(x)
    except (ValueError, TypeError):
        print("输入不准确")
        dd = x
    else:
        print("转换成功")
    finally:
        return dd


d = attempt_to_float(['sd'])
print(d)