# Второй — без использования «Решета Эратосфена».
from math import ceil, log
import timeit
import cProfile


def prime(idx):
    if idx == 1:
        return 2
    n = ceil(2 * idx * log(idx))
    i = 2
    lst_prime = []
    while i <= n:
        flag = True
        j = 2
        while flag and j < i:
            if not i % j:
                flag = False
            j += 1
        if flag:
            lst_prime.append(i)
        i += 1
    return lst_prime[idx - 1]


print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.008794400026090443
print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 1.5903860999969766
print(timeit.timeit('prime(1000)', number=100, globals=globals()))  # 232.17841709998902
# print(timeit.timeit('prime(10000)', number=100, globals=globals()))  # Когда нибудь...
cProfile.run('prime(10000)')
print(prime(100))

"""
         16687 function calls in 370.839 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  370.839  370.839 <string>:1(<module>)
        1  370.816  370.816  370.839  370.839 les_4_task_2_2.py:6(prime)
        1    0.000    0.000  370.839  370.839 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
    16681    0.023    0.000    0.023    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""