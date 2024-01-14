from typing import Callable, Any

#Twice reaplica a função no resultado recebido

soma_2 = lambda val: val + 2

def reaplica(func: callable, val: Any) -> Any:
  return func(func(val))

print(reaplica(soma_2, 1))

print(soma_2(1))



def seleciona(op: str) -> Callable:
  ops = {

    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,

  }

  return ops[op]

print(seleciona('soma')(1, 2))


palavras = ['amar', 'casar', 'falar', 'abacaxi', 'xixi']

print(sorted(palavras))

# pegar apartir da segunda posição

print(sorted(palavras, key=lambda string: string[1]))

# multiplicando palavras 

print(list(map (lambda val: val*2, palavras)))

# palavras que rimam

print(list(filter(lambda x: x[-2:] == 'ar', palavras)))