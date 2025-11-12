# Algoritmo maior de 3 - Princípio da Ordenação

# Definição da variável
d = 0
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a > b:
  d = a
  a = b
  b = d
if b > c:
  d = b
  b = c
  c = d
print(f'O número maior é: {c}')