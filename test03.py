import os

path = 'C:\\Users\\180714-4\\Desktop\\新建文本文档.txt'
with open(path) as f:
    line = f.readlines()
    print(line)
    # print(b)

lines = [x.rstrip() for x in open(path)]
# print(lines)