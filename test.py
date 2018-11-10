seq = [(1, 2, 3), (4, 5, 6), (6, 7, 8)]
for a, b, c in seq:
    print("a={0},b={1},c={2}".format(a, b, c))

values = 1, 2, 4
a, b, *rest = 8, 9, values
print(a, b)
print(rest)
print(rest[0][0])

a = (1, 2, 2, 2, 5, 6, 8)
print(a.count(2))

b = ["foo", "too", "far"]
print(list(a))
b[1] = "hello"
print(b)

b.append("word")
print(b)
b.insert(1, 'hi')
print(b)
b.pop(1)
print(b)
b.remove("foo")
print(b)

c = [2, 3, 1]
b.extend(c)
print(b)

c.sort()
print(c)

import bisect
gg = bisect.bisect(c, 2)
print(gg)
bisect.insort(c, 2)
print(c)

map = {}
for index, value in enumerate(b):
    map[value] = index
print(map)

# sorted() 返回一个新的列表

d = sorted(c)
print(d)

# zip()可以将多个列表、元组或其他序列组合成一个列表：

seq1 = ['foo', 'far', 'jie']
seq2 = ['cat', 'pig', 'dog']
seq3 = ['rose', 'flower', 'year']

hh = list(zip(seq1, seq2, seq3))
print(hh)

# 可以同时迭代多个序列

for i, (a, b, c) in enumerate(zip(seq1, seq2, seq3)):
    print("{0}: {1},{2},{3}".format(i, a, b, c))

# reversed可以向后迭代一个序列
print(list(reversed(range(10))))

dict1 = {"cat": "small", "dog": "big", 1: 'value'}
dict1[7] = "word"
print(dict1)
dict1.pop(7)
print(dict1)
del dict1["cat"]
print(dict1)
print(list(dict1.keys()))
print(list(dict1.values()))
# update将字典融合,它是改变原字典，会将原来的覆盖
dict1.update({'b': 'foo', 'c': 'far'})
print(dict1)

# 用序列创建字典
mapping = {}
for key, value in zip(seq1, seq2):
    mapping[key] = value
print(mapping)

# 因为字典本质上是2元元组的集合， dict可以接受2元元组的列表
mapping = dict(zip(range(5), reversed(range(5))))

# 逻辑
if key in mapping:
    value = mapping[key]
else:
    value = 1

# 可以写为
value = mapping.get(key, 1)

words = [
    "apple", 'bananle', 'origin', 'qiezi', 'tianqi', 'autom', 'ban', 'car',
    'deng', 'uuu', 'ooo', 'qieziqeizi'
]

by_letter = {}

for word in words:
    if word[0] not in by_letter:
        by_letter[word[0]] = [word]
    else:
        by_letter[word[0]].append(word)

print(by_letter)

# setdefault

for word in words:
    by_letter.setdefault(word[0], []).append(word)

# defaultdict
from collections import defaultdict

by_letter = defaultdict(list)  # 把值改为列表形式
for word in words:
    by_letter[word[0]].append(word)

# 集合
a = [1, 2, 3, 5, 5, 6, 4, 2, 6, 3, 4]
a = set(a)
print(a)
b = {1, 5, 6, 8, 9}
# 集合合并可以使用union或|
c = a.union(b)  # 不改变原来的大，返回了一个新的集合
print(c)
d = b | a
print(d)

# 交集 用 &


# 列表推导式
# [expr for val in collection if condition]
strings = ['a', 'as', 'bat', 'car','dove','python']
ll = [x.upper() for x in strings if len(x)>2]
print(ll)
# 集合推到与列表相似，只不过要用尖括号
unique_lengths = {len(x) for x in strings}
print(unique_lengths)

loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)

name1 = [name for name in ['Steven'] if name.count('e')>=2]
print(name1)

print('hello,world')