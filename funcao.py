# FUNCAO SEMPRE VAI RETORNA ALGUMA COISA

# funcao nomeada

def func_nomeada():
  return 'OI'

print(func_nomeada())

# funcao anonima

anonima = lambda: 'OI'

print(anonima())

# print(type(anonima)) tipo class function

# funcao classe

class FuncaoClasse:
  def __call__(self):
    return 'OI'

print(FuncaoClasse()())

# retornando funcao como objeto

minhaFuncaoClasse = FuncaoClasse()

print(minhaFuncaoClasse())

print (type(FuncaoClasse()))