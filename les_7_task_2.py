"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform


def merge(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


def merge_sort(arr):
    if len(arr) > 1:
        arr1 = merge_sort(arr[:len(arr) // 2])
        arr2 = merge_sort(arr[len(arr) // 2:])
        return merge(arr1, arr2)
    else:
        return arr


SIZE = 10
MIN_NUM = 0
MAX_NUM = 50
array = [uniform(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)
print(merge_sort(array))
