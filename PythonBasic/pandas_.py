import pandas as pd
import numpy as np

# s1 = pd.Series([4, -7, -5, -3])  # 创建一个series, 索引为默认值
# print(s1)
# print(s1.index)  # series 的索引
#
# s2 = pd.Series([4.0, 6.5, -0.5, 4.2], index=['d', 'b', 'a', 'c'])
# print(s2)
# print(s2['a'])  # -0.5
# print(s2[['a', 'b', 'c']])
# print('b' in s2)  # True
# # series 定长的有序字典
# dic1 = {'what': 1, 'the': 2, 'fuck': 3}
# s3 = pd.Series(dic1)
# print(s3)
#
# # DataFrame
# data = {'grade': [105, 104, 103], 'score': [100, 99, 98]}
# df1 = pd.DataFrame(data)
# print(df1)
# df2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(df2)
# df3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['a', 'c', 'b'], columns=['11', '2', '33', '4'])
# # index= 行标, columns= 列标
# print(df3)
#
# print(df1.columns)  # 列
# print(df1.index)  # 行
# print(df1.values)  # 值
# print(df1.describe())  # 数据特征描述
# print(df1.T)  # 转置
# print(df3.sort_index(axis=1))  # 按列排序
# print(df3.sort_values(by=44))  # 按某一列排序
##################################################################################################################

# date = pd.date_range('20200101', periods=6)  # 日期
# df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=date, columns=['A', 'B', 'C', 'D'])
# print(df1)
# print(df1['A'])  # 将DataFrame的一列转为Series
# print(df1.A)  # same
# print(df1[0:2])  # 前两行
# print(df1['20200102':'20200104'])  # 使用索引
# # 通过标签提取数据
# print(df1.loc['20200102'])
# print(df1.loc['20200101', ['A', 'C']])
# print(df1.loc[:, ['A', 'C']])  # .loc(行, 列)
# # 通过位置提取数据
# print(df1.iloc[2])  # .iloc(行, 列)
# print(df1.iloc[1:3, 2:4])
# print(df1.iloc[[1, 2, 4], [1, 3]])
# # 混合标签位置提取数据
# print(df1.ix[2:4, ['A', 'C']])
# print(df1.ix['20200102':'20200104', 2:4])
#
# print(df1.A > 6)  # True False
####################################################################################################################

# date = np.arange(20200101, 20200107)
# df1 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=date, columns=['A', 'B', 'C', 'D'])
# print(df1)
# print(df1.iloc[2, 2])
# df1.iloc[2, 2] = 100  # 对单个位置赋值
# print(df1)
# df1.loc[20200102, 'B'] = 200
# print(df1)
# df1[df1.A > 10] = 0  # A > 10, 行格式化为 0
# print(df1)
# df1.A[df1.A == 0] = 1  # A == 0, A 格式化为 1
# print(df1)
# df1['E'] = 10  # 添加一列
# print(df1)
# df1['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=date)
# print(df1)
# df1.loc[20200107, ['A', 'B', 'C']] = [1, 2, 3]
# print(df1)
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=['A', 'B', 'C', 'D', 'E', 'F'])
# s1.name = 'Series1'
# df2 = df1.append(s1)
# print(df2)
# df1.insert(1, 'G', df2['E'])  # 在 1 号位 插入索引为 G 的 df2 中的 E 列
# print(df1)
#
# g = df1.pop('G')  # pop G 列
# df1.insert(6, 'G', g)  # 在 6 号位插入
# print(df1)
# del df1['G']  # 删除 G
# print(df1)
# df2 = df1.drop(['A', 'B'], axis=1)  # 删除 A B 列
# print(df1)  # df1 不变
# print(df2)  # df2 中 A B 列被删除
# df2 = df1.drop([20200107], axis=0)  # 删除 20200107 行
# print(df1)
# print(df2)
############################################################################################################

# date = np.arange(20200101, 20200105)
# df1 = pd.DataFrame(np.arange(12).reshape((4, 3)), index=date, columns=['A', 'B', 'C'])
# print(df1)
# df2 = pd.DataFrame(df1, index=date, columns=['A', 'B', 'C', 'D', 'E'])
# print(df2)
# s1 = pd.Series([3, 4, 6], index=date[:3])
# s2 = pd.Series([32, 5, 2], index=date[1:])
# df2['D'] = s1
# df2['E'] = s2
# print(df2)
# '''
#           A   B   C    D     E
# 20200101  0   1   2  3.0   NaN
# 20200102  3   4   5  4.0  32.0
# 20200103  6   7   8  6.0   5.0
# 20200104  9  10  11  NaN   2.0
# '''
# print(df2.dropna(axis=0, how='any'))  # 删除空值 how = ['any', 'all'] any 存在空值 all 全为空值
# print(df2.fillna(value=0))  # 填充空值
# print(df2.isnull())
# print(np.any(df2.isnull()))  # df2 中是否存在任一空值 (True / False)
# print(np.all(df2.isnull()))  # df2 中是否全是空值 (True / False)
################################################################################################################

# file = pd.read_csv("./pandasRes/people.csv")
# print(file)
# file.iloc[2, 0] = '深圳'
# print(file)
# file.to_csv("./pandasRes/people2.csv")  # 写入
####################################################################################################################

# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])
# df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])
# df3 = pd.DataFrame(np.arange(24, 36).reshape((3, 4)), columns=['A', 'B', 'C', 'D'])
# print(df1)
# print(df2)
# print(df3)
# df4 = pd.concat([df1, df2, df3], axis=0)  # 纵向合并
# print(df4)
# df4 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # 忽略原 index
# print(df4)
# df5 = pd.concat([df1, df2, df3], axis=1)  # 横向合并
# print(df5)
#
# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['A', 'B', 'C', 'F'])
# df2 = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), columns=['A', 'C', 'D', 'E'])  # 注意改动
# print(df1)
# print(df2)
# df6 = pd.concat([df1, df2], join='outer', ignore_index=True, sort=False)  # outer : 缺少的填充null
# print(df6)
# '''
#     A    B   C     D     E     F
# 0   0  1.0   2   NaN   NaN   3.0
# 1   4  5.0   6   NaN   NaN   7.0
# 2   8  9.0  10   NaN   NaN  11.0
# 3  12  NaN  13  14.0  15.0   NaN
# 4  16  NaN  17  18.0  19.0   NaN
# 5  20  NaN  21  22.0  23.0   NaN
# '''
# df7 = pd.concat([df1, df2], join='inner', ignore_index=True, sort=False)  # inner : 只合并都存在的部分
# print(df7)
# '''
#     A   C
# 0   0   2
# 1   4   6
# 2   8  10
# 3  12  13
# 4  16  17
# 5  20  21
# '''
#
# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=['A', 'B', 'C', 'F'])
# df2 = pd.DataFrame(np.arange(12, 24).reshape((4, 3)), columns=['A', 'C', 'D'])  # 注意改动
# print(df1)
# print(df2)
# df8 = pd.concat([df1, df2], axis=1).reindex(df1.index)  # df1.index 为标准， 没有对应的会被舍弃
# print(df8)
# '''
#      A    B     C     F   A   C   D
# 0  0.0  1.0   2.0   3.0  12  13  14
# 1  4.0  5.0   6.0   7.0  15  16  17
# 2  8.0  9.0  10.0  11.0  18  19  20
# '''
##########################################################################################################

# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# res = pd.merge(left, right, on="key")  # 基于 Key 合并
# print(res)
#
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K3'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
# print(res)
# '''
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K0   K1   A1   B1  NaN  NaN
# 2   K1   K0   A2   B2   C1   D1
# 3   K1   K0   A2   B2   C2   D2
# 4   K2   K1   A3   B3  NaN  NaN
# 5   K3   K0  NaN  NaN   C3   D3
# '''
# res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
# print(res)
# '''
#   key1 key2   A   B   C   D
# 0   K0   K0  A0  B0  C0  D0
# 1   K1   K0  A2  B2  C1  D1
# 2   K1   K0  A2  B2  C2  D2
# '''
# res = pd.merge(left, right, on=['key1', 'key2'], how='left')
# print(res)
# '''
#   key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K0   K1  A1  B1  NaN  NaN
# 2   K1   K0  A2  B2   C1   D1
# 3   K1   K0  A2  B2   C2   D2
# 4   K2   K1  A3  B3  NaN  NaN
# '''
# res = pd.merge(left, right, on=['key1', 'key2'], how='right')
# print(res)
# '''
#   key1 key2    A    B   C   D
# 0   K0   K0   A0   B0  C0  D0
# 1   K1   K0   A2   B2  C1  D1
# 2   K1   K0   A2   B2  C2  D2
# 3   K3   K0  NaN  NaN  C3  D3
# '''
# res = pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator=True)  # 开启描述
# print(res)
# '''
#   key1 key2    A    B    C    D      _merge
# 0   K0   K0   A0   B0   C0   D0        both
# 1   K0   K1   A1   B1  NaN  NaN   left_only
# 2   K1   K0   A2   B2   C1   D1        both
# 3   K1   K0   A2   B2   C2   D2        both
# 4   K2   K1   A3   B3  NaN  NaN   left_only
# 5   K3   K0  NaN  NaN   C3   D3  right_only
# '''
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                      'B': ['B0', 'B1', 'B2']},
#                     index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                       'D': ['D0', 'D2', 'D3']},
#                      index=['K0', 'K2', 'K3'])
# print(left)
# print(right)
# res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# print(res)
# '''
#       A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3
# '''
# boys = pd.DataFrame({'k': ['k0', 'k1', 'k2'], 'age': [1, 2, 3]})
# girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
# print(boys)
# print(girls)
# res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')  # 同样的数据加标签
# print(res)
# '''
#     k  age_boy  age_girl
# 0  k0      1.0       NaN
# 1  k1      2.0       NaN
# 2  k2      3.0       NaN
# 3  K0      NaN       4.0
# 4  K0      NaN       5.0
# 5  K3      NaN       6.0
# '''
#################################################################################################

import matplotlib.pyplot as plt
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 累加
data.plot()
plt.show()

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=['A', 'B', 'C', 'D'])  # 4 组 1000 个
data = data.cumsum()
print(data.head())  # 前五行
data.plot()
plt.show()

ax = data.plot.scatter(x='A', y='B', color='Blue', label='Class 1')
data.plot.scatter(x='A', y='C', color='Green', label='Class 2', ax=ax)
plt.show()
