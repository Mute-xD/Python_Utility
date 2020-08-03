"""
快速排序
时间复杂度：⚪(n log2 n)
"""
import random
import numpy as np

unsortedData = np.arange(100)
random.shuffle(unsortedData)
print(unsortedData[:10])


def quickSort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    else:
        mid = unsorted[0]
        smaller = [i for i in unsorted[1:] if i <= mid]  # (<=) 用于处理重复数据
        bigger = [i for i in unsorted[1:] if i > mid]
        return quickSort(smaller) + [mid] + quickSort(bigger)


print(quickSort(unsortedData))
print(quickSort([10, 10, 11, 11, 12]))
