
# funcao anonima recebendo parametros

anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2

print(anonima(1))
print(anonima_plus(2,2))


# parametro posicional

def soma_posicional(x, y):
  return x + y

print(soma_posicional(1, 3))

# parametro nomeado

def soma_nomeado(x=4, y=3):

  print(f'X: {x} Y: {y}')
  return x + y

print(soma_nomeado(y=4)) # posso renomear

# parametro nomeado

def soma_explicitamente_nomeados(*, x=4, y=3): # * pra tras so pode ser chamada de maneira nomeada / a posição do * importa

  print(f'X: {x} Y: {y}')
  return x + y

print(soma_explicitamente_nomeados(x=3, y=3))

# parametros posicionais com /

def soma_explicitamente_nomeados(x=4, y=3, /): # antes da barra só recebe parametros posicionais

  print(f'X: {x} Y: {y}')
  return x + y

print(soma_explicitamente_nomeados(1, 2))

# somando misturando parametros

def soma_tudo_mix(x, y, /, z, *, w):
  return sum((x, y, z, w))

print(soma_tudo_mix(1, 3, 3, w= 2))
print(soma_tudo_mix(1, 3, z=3, w= 2))