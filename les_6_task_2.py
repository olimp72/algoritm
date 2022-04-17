# Определить, какое число в массиве встречается чаще всего.

# Variant 2
from sys import getsizeof
from random import randint


def main(n):
    min_num = 0
    max_num = 100
    num = 0
    max_value = 0
    array = [randint(min_num, max_num) for _ in range(n)]
    print(array)
    d_array = {}
    for i in array:
        if i in d_array:
            d_array[i] += 1
        else:
            d_array[i] = 1
        if d_array[i] > max_value:
            num = i
            max_value = d_array[i]
    if max_value > 1:
        print(f'Число {num} встречается {max_value} раз(а)')
    else:
        print('Нет повторяющихся чисел')
    return locals()


var = main(10)
sum_size = 0
for item, value in var.items():
    if hasattr(value, '__iter__'):
        for i in value:
            sum_size += getsizeof(i)
    sum_size += getsizeof(value)
print(sum_size)
