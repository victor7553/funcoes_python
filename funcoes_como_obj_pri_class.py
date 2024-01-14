from typing import Callable, Dict
from numbers import Number


# funcao lambda dentro da func

func = lambda:'resultado da funcao'

print(func())

calc: Dict[str, Callable] = {

  'soma': lambda x, y: x + y,
  'sub': lambda x, y: x - y,
  'mult': lambda x, y: x * y,
  'div': lambda x, y: x / y

}

print(calc['soma'](2,2))
print(calc['sub'](2,2))
print(calc['mult'](2,2))
print(calc['div'](2,2))


# funções nomeadas

def soma(x: Number, y:Number) -> Number:
  return x + y

def sub(x: Number, y:Number) -> Number:
  return x - y

def mult(x: Number, y:Number) -> Number:
  return x * y

def div(x: Number, y:Number) -> Number:
  return x / y

calc_noemado = {

  'soma': soma,
  'sub': sub,
  'mult': mult,
  'div': div
}

print(soma(1, 2))

# escolho a posicao [] e somo ()
somas = [

  lambda x: x + 0,
  lambda x: x + 1,
  lambda x: x + 2

]

print(somas[1](2))


def soma_1(x: Number) -> Number:
  return x + 1


print(soma_1(1))