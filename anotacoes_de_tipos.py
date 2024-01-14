# ANOTAÇÕES DE TIPO

from numbers import Number
from typing import Union, Any, List, Dict, Sequence, Text


somavael = Union[Number, str, list]

def soma(x: somavael, y: somavael) -> somavael:
  return x + y


def identidade(val: Any) -> Any:
  return val

def meu_sum(l: List[Number]) -> Number:
  return sum(l)

print(meu_sum([1, 2, 3]))


def cadastro_usuario(nome: str, idade: int, gostos: List[str]) -> Dict [str, Union[str, int, list[str]]]:
  return {
    'nome': nome,
    'idade': idade,
    'gostos': gostos
  }


print(cadastro_usuario('vitor', 25, ['jogar bola', 'comer açai']))

def meu_min(seq: Sequence):
  return min(seq)

def converter_para_reais(valor: Text):
  ...