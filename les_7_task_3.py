"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""
from random import randint


def sort_counter(arr):  # Сортировка подсчетом
    min_num, max_num = min(arr), max(arr)
    in_min_num = min_num
    if min_num < 0:
        abs_min_num = abs(min_num)
        arr = [item + abs_min_num for item in arr]
        in_min_num, max_num = min(arr), max(arr)

    counter_arr = [0] * (max_num - in_min_num + 1)
    for item in arr:
        counter_arr[item - in_min_num] += 1
    pos = 0
    for idx, item in enumerate(counter_arr):
        num = idx + in_min_num
        for i in range(item):
            arr[pos] = num
            pos += 1
    if min_num < 0:
        abs_min_num = abs(min_num)
        arr = [item - abs_min_num for item in arr]
    return arr


m = int(input(f'Введите любое натуральное число: '))
size = 2 * m + 1
MIN_NUM = 0
MAX_NUM = 100
array = [randint(MIN_NUM, MAX_NUM) for _ in range(size)]
print(array)
print(sort_counter(array))
print(f'Медиана массива: {array[size // 2]}')
