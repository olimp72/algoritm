# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint, choice


def quicksort(arr, l, r):
    if l >= r:
        return
    else:
        q = choice(arr[l:r + 1])
        i = l
        j = r
        while i <= j:
            while arr[i] < q:
                i += 1
            while arr[j] > q:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                quicksort(arr, l, j)
                quicksort(arr, i, r)
        return arr[0], arr[-1]


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_num, max_num = quicksort(array.copy(), 0, SIZE - 1)
idx_min_num = array.index(min_num)
idx_max_num = array.index(max_num)
print(f'Минимальный элемент arr[{idx_min_num}] = {min_num}')
print(f'Максимальный элемент arr[{idx_max_num}] = {max_num}')
array[idx_min_num], array[idx_max_num] = array[idx_max_num], array[idx_min_num]
print(array)
