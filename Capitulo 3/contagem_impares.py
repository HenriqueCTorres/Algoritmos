# Contagem de ímpares - 01

# Definição da variável
s = 0
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a % 2 == 1:
  s = s + 1
if b % 2 == 1:
  s = s + 1
if c % 2 == 1:
  s = s + 1
print(f'A soma de todos números ímpares é: {s}')