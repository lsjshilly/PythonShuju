import numpy as np

# Generate some randm data
data = np.random.rand(2, 3)
print(data)
print(data * 10)
print(data + data)

# 创建ndarray
# 创建数组最简单的方法就是使用array函数，它接收一切序列性的对象
data1 = [6, 7, 8, 9, 10, 5.5, 6.3]
arr1 = np.array(data1)
print(arr1)
# 嵌套序列
print()
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.shape)

# np.array 会尝试为新建的数组推断出适合保存的数据类型

print(arr1.dtype)
print(arr2.dtype)

# zeros ones 分别创建全是0或1的指定形状的数组，
# empty创建一个没有任何具体自的数组
print(np.zeros((1, 10), dtype='float64'))

# arrange 是python内置函数range的数组版
print(np.arange(15))

# 常用函数说明

# arary  将输入数据（列表，元组或其他序列类型）转换为ndarray，要慢慢推断出dtype，要么指定dtype
# assarray 将输入转换为ndarray， 如果输入本身就是ndarray则不进行复制
# arange  类似于range 但赶回的是ndarray 而不是列表
# ones，ones_like 指定形状数组创建全为1的数组，one_like以另一个数组的形状和dtype创建数组
# zeros, zeros_like 类似于上面
# empty empty_like
# full full_like
# eye identity 创建一个正方的NXN的单位矩阵

# 通过astype方法讲一个数组从一个dtype转换为另一个dtype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)

# Numpy数组的运算
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# 大小相等的数组之间的任何算术运算都会讲运算应用到元素级

print(arr * arr)
print(arr - arr)

# 数组与标量的运算也会传递到各个元素
print(1 / arr)

# 大小相同的数组之间的比较会生产不布尔数组：
arr2 = np.array([[0, 4, 5], [7, 3, 12]])
print(arr2 > arr)

# NumPy 基本的索引和切片

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)  # [ 0  1  2  3  4 12 12 12  8  9]
# 数组的切片是原始数组的视图，对数组切片的修改都会反映到原始数组上
arr_slice = arr[5:8]
print(arr_slice)  # [12 12 12]
arr_slice[1] = 32

print(arr_slice)  # [12 32 12]
print(arr)  # [ 0  1  2  3  4 12 32 12  8  9]

# 切片[:]给数组中的所有值赋值
arr_slice[:] = 64
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
# 以下两种方式等价
print(arr2d[0][2])
print(arr2d[0, 2])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d.shape)

print(arr3d[0])
# 标量值和数组都可以被赋值给arr3d【0】
old_values = arr3d[0].copy()

arr3d[0] = 45
print(arr3d)

arr3d[0] = old_values
print(arr3d)

print(arr3d[1, 0])

# 切片索引
# 一维数组同python列表
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("arr2d = ")
print(arr2d)
# arr2d[:2]选取前两行
print(arr2[:2])

# 传入多个索引
print(arr2d[:2, 1:])
# 整数索引与切片混合，
# 去第二行的前两列
print(arr2d[1, :2])
print(arr2d[:2, 2])
# :表示去整个轴
print(arr2d[:, :1])

# 布尔型索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 使用random.rand生成随机正太分布的矩阵
data = np.random.randn(7, 4)
# 布尔数组的长度必须与被索引数组的行数一致
print(names == 'Bob')
print(data[names == 'Bob'])

# 索引列
print(data[names == 'Bob', 2:])
# 选出Bob以外的其他值，既可以使用（！=），也可以使用~对条件进行否定
data[~(names == "Bob")]
cond = names == 'Bob'
data[~cond]
mask = (names == 'Bob') | (names == 'Will')
data[mask]

# 通过布尔型数组设置值是一种常用的手段
data[data < 0] = 0
# 通过一维布尔数组设置整行或整列的值也很简单
data[names != 'Joe'] = 1

# 花式索引
# 利用整数数组进行索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)

# 以特定顺序索引， 只需传入一个用于指定顺序的整数列表或ndarray即可
print()
print(arr[[4, 3, 0, 6]])
# 使用复数索引将从末尾开始
print()
print(arr[[-1, -3, -7]])

# 一次传入多个索引，返回元素对应各个索引元组
arr = np.arange(32).reshape((8, 4))
print(arr)
print()
print(arr[[1, 2, 3, 4], [0, 1, 1, 2]])
print(arr[[1, 2, 3, 4]][[0, 1, 1, 2]])

# 如下的截取方法
print()
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

# 数组转置与轴对称
arr = np.arange(15).reshape((3, 5))
print(arr)

print(arr.T)

arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))  # 3*3的矩阵

# 对于高维数组，transpose 需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1, 0, 2)))

print(arr.swapaxes(1, 2))  # 将一对轴进行交换

