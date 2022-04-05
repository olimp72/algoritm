# Определить, какое число в массиве встречается чаще всего.
#
# Variant 1

from random import randint
import timeit
import cProfile


def main(n):
    min_num = 0
    max_num = 100
    num = 0
    max_value = 0
    array = [randint(min_num, max_num) for _ in range(n)]
    # print(array)
    d_array = {}
    for i in array:
        d_array[i] = d_array.get(i, 0) + 1
        if d_array[i] > max_value:
            num = i
            max_value = d_array[i]
    return num, max_value


print(timeit.timeit('main(10)', number=100, globals=globals()))  # 0.0027932999655604362
print(timeit.timeit('main(100)', number=100, globals=globals()))  # 0.02530300000216812
print(timeit.timeit('main(1000)', number=100, globals=globals()))  # 0.28069719998165965
print(timeit.timeit('main(10000)', number=100, globals=globals()))  # 2.388124300050549
cProfile.run('main(10000)')

max_item, max_value = main(10)
if max_value > 1:
    print(f'Число {max_item} встречается {max_value} раз(а)')
else:
    print('Нет повторяющихся чисел')

"""
         92543 function calls in 0.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.065    0.065 <string>:1(<module>)
        1    0.006    0.006    0.065    0.065 les_4_task_1_1.py:10(main)
        1    0.006    0.006    0.057    0.057 les_4_task_1_1.py:15(<listcomp>)
    10000    0.012    0.000    0.017    0.000 random.py:239(_randbelow_with_getrandbits)
    10000    0.022    0.000    0.044    0.000 random.py:292(randrange)
    10000    0.007    0.000    0.051    0.000 random.py:366(randint)
    30000    0.005    0.000    0.005    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.065    0.065 {built-in method builtins.exec}
    10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.002    0.000    0.002    0.000 {method 'get' of 'dict' objects}
    12538    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
