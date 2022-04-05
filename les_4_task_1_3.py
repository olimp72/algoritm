# Определить, какое число в массиве встречается чаще всего.

# Variant 2

from random import randint
import timeit
import cProfile


def main(n):
    min_num = 0
    max_num = 100
    array = [randint(min_num, max_num) for _ in range(n)]
    # print(array)
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
    return num, max_value


print(timeit.timeit('main(10)', number=100, globals=globals()))  # 0.0034918999299407005
print(timeit.timeit('main(100)', number=100, globals=globals()))  # 0.09879439999349415
print(timeit.timeit('main(1000)', number=100, globals=globals()))  # 8.676252500037663
# print(timeit.timeit('main(10000)', number=100, globals=globals()))  # Устал ждать
cProfile.run('main(10000)')


max_item, max_value = main(10)
if max_value > 1:
    print(f'Число {max_item} встречается {max_value} раз(а)')
else:
    print('Нет повторяющихся чисел')

"""
         82737 function calls in 9.384 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.384    9.384 <string>:1(<module>)
        1    9.328    9.328    9.384    9.384 les_4_task_1_3.py:10(main)
        1    0.006    0.006    0.056    0.056 les_4_task_1_3.py:13(<listcomp>)
    10000    0.012    0.000    0.016    0.000 random.py:239(_randbelow_with_getrandbits)
    10000    0.023    0.000    0.043    0.000 random.py:292(randrange)
    10000    0.007    0.000    0.051    0.000 random.py:366(randint)
    30000    0.005    0.000    0.005    0.000 {built-in method _operator.index}
        1    0.000    0.000    9.384    9.384 {built-in method builtins.exec}
    10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12732    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

#  Выполнено три варианта задания:
#     1 - линейная асимптотика
#     2 - линейная асимптотика
#     3 - квадратичная асимптотика
# Выбор в пользу 2 варианта.
# При примерно равном быстродействии за счет более простого кода и меньшего количества вызова функций.