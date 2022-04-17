"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка
"""
from random import randint


def bubble_sort(arr):
    for i in range(SIZE - 1):
        for j in range(SIZE - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


SIZE = 10
MIN_NUM = -100
MAX_NUM = 100
array = [randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)
bubble_sort(array)
print(array)
