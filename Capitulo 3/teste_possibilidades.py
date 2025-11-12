# Algoritmo maior de 3 - Teste de possibilidades

# Definição da variável
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a > b and b > c:
  print(f'O número maior é: {a}')
elif a > c and c > b:
  print(f'O número maior é: {a}')
elif b > a and b > c:
  print(f'O número maior é: {b}')
elif b > c and c > a:
  print(f'O número maior é: {b}')
elif c > a and a > b:
  print(f'O número maior é: {c}')
else:
  print(f'O número maior é: {c}')