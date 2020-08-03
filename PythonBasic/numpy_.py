import numpy as np
###########################################################
# array = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]])
# print(array)
# print(array.ndim)  # 矩阵维度
# print(array.shape)  # 矩阵形状
# print(array.size)  # 矩阵大小
# print(array.dtype)  # 矩阵元素数据类型(int)
##########################################################

# a = np.array([1, 2, 3], dtype=np.int32)
# print(a.dtype)
# b = np.array([4, 5, 6], dtype=float)
# print(b.dtype)
# c = np.array([1, 2, 3])  # 一维
# print(c)
# d = np.array([[1, 2, 3],  # 二维
#               [4, 5, 6]])
# print(d)
# zero = np.zeros((3, 3))  # 全零矩阵
# print(zero)
# one = np.ones((3, 3))  # 单位矩阵
# print(one)
# empty = np.empty((3, 3))  # 空矩阵（可以做除数）???
# print(empty)
# e = np.arange(10)  # 0 ~ 9
# print(e)
# f = np.arange(4, 12)  # 4 ~ 11
# print(f)
# g = np.arange(1, 20, 3)
# print(g)
# h = np.arange(8).reshape(2, 4)  # 改变形状
# print(h)
#################################################################

# arr1 = np.array([[1, 2, 3],
#                  [4, 5, 6]])
# arr2 = np.array([[1, 1, 2],
#                  [2, 3, 3]])
# print(arr1)
# print(arr2)
# print(arr1 + arr2)  # 矩阵加法
# print(arr1 - arr2)  # 矩阵减法
# print(arr1 * arr2)  # 矩阵叉乘
# print(arr1 ** arr2)  # 矩阵求幂
# print(arr1 / arr2)  # 矩阵除法
# print(arr1 % arr2)  # 矩阵取余
# print(arr1 // arr2)  # 矩阵取整
# print(arr1 + 2)  # 所有元素 + 2
# arr3 = arr1 > 3  # 矩阵元素判断
# print(arr3)
# arr4 = np.ones((3, 5))
# print(np.dot(arr1, arr4))  # 矩阵点乘
# print(arr1.dot(arr4))
# print(arr1.T)  # 矩阵转置
# print(np.transpose(arr1))
################################################################

# rand = np.random.random((3, 2))  # 0 ~ 1 随机数
# rand = np.random.normal(size=(3, 2))  # 三行两列标准正态
# rand = np.random.randint(0, 10, size=(3, 2))  # 0 ~ 10
# print(rand)
#
# print(np.sum(rand))  # 求和
# print(np.min(rand))  # 求最小
# print(np.max(rand))  # 求最大
#
# print(np.sum(rand, axis=0))  # 列求和
# print(np.sum(rand, axis=1))  # 行求和
#
# print(np.argmin(rand))  # 最小值位置
# print(np.argmax(rand))  # 最大值位置
#
# print(np.mean(rand))  # 元素均值
# print(rand.mean())  # 元素均值
# print(np.median(rand))  # 中位数
# print(np.sqrt(rand))  # 元素开方
#
# print(np.sort(rand))  # 矩阵内排序
# print(np.clip(rand, 2, 8))  # 元素范围限制（于2 ~ 8）
##############################################################

# arr1 = np.arange(2, 14)
# print(arr1)
# print(arr1[2])  # 同 C/C++
# print(arr1[1:4])
# print(arr1[2:-1])
# print(arr1[:5])
# print(arr1[-2:])
# arr2 = arr1.reshape(3, 4)
# print(arr2)
# print(arr2[1])
# print(arr2[1][1])
# print(arr2[1, 1])  # 同上
# print(arr2[:, 1])
# for i in arr2:
#     print(i)  # 逐行
# for i in arr2.T:
#     print(i)  # 逐列
# for i in arr2.flat:
#     print(i)  # 逐个
#############################################################################

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.vstack((arr1, arr2))  # 垂直合并
# print(arr3)
# print(arr3.shape)
#
# arr4 = np.hstack((arr1, arr2))  # 水平合并
# print(arr4)
# print(arr4.shape)
#
# arr = np.concatenate((arr1, arr2), axis=0)  # axis = 0 : 纵向合并，维度形状必须匹配
# print(arr)
#
# # 一维 array 无法转置
# print(arr1.T)
# arr1_1 = arr1[np.newaxis, :]  # 在列上升维
# print(arr1_1)
# print(arr1_1.shape)
# print(arr1_1.T)
# arr1_2 = arr1[:, np.newaxis]  # 在行上升维
# print(arr1_2)
# print(arr1_2.shape)
# arr1_3 = np.atleast_2d(arr1)  # 自动升二维
# print(arr1_3)
##################################################################

# arr1 = np.arange(12).reshape((3, 4))
# '''
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# '''
# print(arr1)
# arr2, arr3 = np.split(arr1, 2, axis=1)  # 切分, axis = 1:水平
# print(arr2)
# print(arr3)
# arr4, arr5, arr6 = np.split(arr1, 3, axis=0)  # 切分, axis = 0:垂直
# print(arr4)
# print(arr5)
# print(arr6)
# # 不均等切分会出错
# arr7, arr8, arr9 = np.array_split(arr1, 3, axis=1)  # 实现不等切分
# print(arr7)
# print(arr8)
# print(arr9)
# arrv1, arrv2, arrv3 = np.vsplit(arr1, 3)  # 垂直切分
# print(arrv1)
# print(arrv2)
# print(arrv3)
# arrh1, arrh2 = np.hsplit(arr1, 2)  # 水平切分
# print(arrh1)
# print(arrh2)
######################################################################

arr1 = np.array([1, 2, 3])
arr2 = arr1  # 浅拷贝，共享内存
arr2[0] = 5
print(arr1)
print(arr2)  # 值一样，类似指针（别名）

arr3 = arr1.copy()  # 深拷贝
arr3[0] = 10
print(arr1)
print(arr3)
