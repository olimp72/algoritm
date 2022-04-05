# Определить, какое число в массиве встречается чаще всего.
from random import randint
SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 100
max_item = 0
max_value = 0
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
d_array = {i: 0 for i in range(MAX_ITEM)}
for i in array:
    d_array[i] = d_array.get(i, 0) + 1
for item, value in d_array.items():
    if value > max_value:
        max_item = item
        max_value = value
print(f'Число {max_item} встречается {max_value} раз(а)')
