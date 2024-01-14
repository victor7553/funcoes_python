
# EMAPACOTAMENTO E DESEMPACOTAMENTO DE ARGUMENTOS


# def meu_sum(*args, **kwargs):  args só funciona com argumentos posicionais

def meu_sum(*grupo_pos, **grupo_nomeado): # conta os primeiros parametros como argumento

  #EMPACOTAMENTO
  print(grupo_pos, grupo_nomeado)
  print(type(grupo_pos), type(grupo_nomeado))
  return grupo_pos, grupo_nomeado
  
print(meu_sum(1, 2, 3, 4, 5, c= 1, d = 2))

# adicionando argumentos na fução
def meu_sum(x, y, a= 1, b=2, *grupo_pos, **grupo_nomeado): # conta os primeiros parametros como argumento
  print(grupo_pos, grupo_nomeado)
  print(type(grupo_pos), type(grupo_nomeado))
  return grupo_pos, grupo_nomeado
  
print(meu_sum(1, 2, 3, 4, 5, 6, c= 1, d = 2)) # para um cria uma tupla  e para outro cria um dicionario / não pode repetir o mesmo nome nos nomeados

#DESEMPACOTAMENTO

lista = [-1, 2, 3, 4, 5]

def meu_min(a, b, c, d, *args): # empacotou
  return min((a, b, c, d, *args)) # desempacotou

print(meu_min(*lista))


dicionario = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4
  
}

def meu_max(a=0, b=0, c=0, d=0):
  return max((a, b, c, d))

print(meu_max(**dicionario))

l = [1, 2, 3]
d = {'d': 1, 'e': 2}


def meu_mix(a, b, c, d=0, e=0):
  return a, b, c, d, e

print(meu_mix(*l, **d))