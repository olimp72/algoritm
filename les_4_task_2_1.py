# Первый — с помощью алгоритма «Решето Эратосфена».
from math import ceil, log
import timeit
import cProfile


def eratosthenes(idx):
    if idx == 1:
        return 2
    n = ceil(2 * idx * log(idx))
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, n, i):
                sieve[j] = 0
    return [i for i in sieve if i != 0][idx - 1]


print(timeit.timeit('eratosthenes(10)', number=100, globals=globals()))  # 0.002655099960975349
print(timeit.timeit('eratosthenes(100)', number=100, globals=globals()))  # 0.04403739992994815
print(timeit.timeit('eratosthenes(1000)', number=100, globals=globals()))  # 1.1434245998971164
print(timeit.timeit('eratosthenes(10000)', number=100, globals=globals()))  # 11.518441599910147
cProfile.run('eratosthenes(10000)')
print(eratosthenes(100))

"""
         7 function calls in 0.121 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004    0.121    0.121 <string>:1(<module>)
        1    0.014    0.014    0.014    0.014 les_4_task_2_1.py:14(<listcomp>)
        1    0.104    0.104    0.117    0.117 les_4_task_2_1.py:6(eratosthenes)
        1    0.000    0.000    0.121    0.121 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""