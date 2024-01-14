
from operator import add, mul, itemgetter
from functools import partial, reduce

soma_2 = partial(add, 2)

print(soma_2(0)) # return 2


reduce(add, [1, 2, 3, 4, 5])
reduce(mul, [1, 2, 3, 4, 5])

somatorio = partial(reduce, add)
multiplicar = partial(reduce, mul)

print(somatorio([1, 2]))
print(multiplicar([1, 2, 3, 4, 5]))


def func(a, b, c, d, databes= None):
  return databes, a, b, c, d


func_postgres = partial(func, database='postgres')

print(func_postgres(1, 2, 3, 4, ''))