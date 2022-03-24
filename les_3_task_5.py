# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
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
        return arr


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
sum_num = 0
quicksort(array, 0, SIZE - 1)
for i in array[1:-1]:
    sum_num += i
print(sum_num)
print(array)
