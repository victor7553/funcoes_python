

from operator import add, mul, sub, itemgetter
from functools import reduce

print(reduce(add, [1, 2 ,3, 4, 5]))
print(reduce(sub, [1, 2 ,3, 4, 5]))
print(reduce(mul, [1, 2 ,3, 4, 5]))

palavras = ['amar', 'casar', 'falar', 'abacaxi', 'xixi']


print(sorted(palavras, key=itemgetter(1)))

