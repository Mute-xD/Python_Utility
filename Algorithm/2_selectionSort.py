"""
选择排序
时间复杂度：⚪(n^2)
"""
import numpy as np
import random

unsortedData = np.arange(100)
random.shuffle(unsortedData)
print(unsortedData[:10])


def smallestIndex(array):
    current_smallest = array[0]
    current_index = 0
    for i in range(len(array)):
        if current_smallest > array[i]:
            current_smallest = array[i]
            current_index = i
    return current_index


def sorting(array):
    sorted_array = []
    array_counting = array.copy()
    for i in range(len(array_counting)):
        smallest_index = smallestIndex(array)
        sorted_array.append(array.pop(smallest_index))
    return sorted_array


sortedArray = sorting([10, 10, 11, 11, 12])
print(sortedArray)
