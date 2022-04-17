# Определить, какое число в массиве встречается чаще всего.

# Variant 3
from sys import getsizeof
from random import randint


def main(n):
    min_num = 0
    max_num = 100
    array = [randint(min_num, max_num) for _ in range(n)]
    print(array)
    num = array[0]
    max_value = 1
    for i in range(n - 1):
        temp_value = 1
        for j in range(i + 1, n):
            if array[i] == array[j]:
                temp_value += 1
        if temp_value > max_value:
            max_value = temp_value
            num = array[i]
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
