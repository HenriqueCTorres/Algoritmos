# Introdução a função

# Definição da variável
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))

# Definição da função
def funcao1 (a: int, b: int) -> int:
  soma = a + b
  return soma

def impar_ou_par (a: int):
  if a % 2 == 0:
    resultado = "Par"
    return resultado
  else:
    resultado = "Ímpar"
    return resultado

# Teste
print(funcao1(a, b))
print(impar_ou_par(a))