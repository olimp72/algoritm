# Определить, какое число в массиве встречается чаще всего.

# Variant 2

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
        if i in d_array:
            d_array[i] += 1
        else:
            d_array[i] = 1
        if d_array[i] > max_value:
            num = i
            max_value = d_array[i]
    return num, max_value


print(timeit.timeit('main(10)', number=100, globals=globals()))  # 0.003223799983970821
print(timeit.timeit('main(100)', number=100, globals=globals()))  # 0.030028400011360645
print(timeit.timeit('main(1000)', number=100, globals=globals()))  # 0.2978889999212697
print(timeit.timeit('main(10000)', number=100, globals=globals()))  # 2.727665799902752
cProfile.run('main(10000)')

max_item, max_value = main(10)
if max_value > 1:
    print(f'Число {max_item} встречается {max_value} раз(а)')
else:
    print('Нет повторяющихся чисел')

"""
         82700 function calls in 0.061 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.061    0.061 <string>:1(<module>)
        1    0.004    0.004    0.061    0.061 les_4_task_1_2.py:10(main)
        1    0.006    0.006    0.056    0.056 les_4_task_1_2.py:15(<listcomp>)
    10000    0.012    0.000    0.017    0.000 random.py:239(_randbelow_with_getrandbits)
    10000    0.022    0.000    0.043    0.000 random.py:292(randrange)
    10000    0.007    0.000    0.051    0.000 random.py:366(randint)
    30000    0.005    0.000    0.005    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.061    0.061 {built-in method builtins.exec}
    10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12695    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
