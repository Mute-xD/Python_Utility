"""
二分查找
时间复杂度：⚪(log n)
"""
import random
import numpy as np


def guess():
    target = random.randint(0, 99)
    array = np.arange(100)
    index = trying(array, target)
    return index


def trying(array, target):
    high = array[array.size - 1]
    low = 0
    mid = high // 2
    while low <= high:
        if array[mid] > target:
            high = mid - 1
            mid = (high + low) // 2
        elif array[mid] < target:
            low = mid + 1
            mid = (high + low) // 2
        elif array[mid] == target:
            index = mid
            return index
    else:
        return "NotFound"


print(guess())
print(trying(np.array([1, 3, 5, 7, 9]), 5))
