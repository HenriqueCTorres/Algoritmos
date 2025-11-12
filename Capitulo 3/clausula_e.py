# Algoritmo maior de 3 - Cláusula "E" -> "and"

# Definição da variável
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a > b and a > c:
  print(f'O número maior é: {a}')
elif b > a and b > c:
  print(f'O número maior é: {b}')
else:
  print(f'O número maior é: {c}')