# Contagem de ímpares - Semáforo - 03

# Definição da variável
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))

# Teste
if a % 2 == 0 and b % 2 == 0:
  print("Verde")
if a % 2 == 1 and b % 2 == 1:
  print("Vermelho")
if [a % 2 == 1 and b % 2 == 0] or [a % 2 == 0 and b % 2 == 1]:
  print("Amarelo")