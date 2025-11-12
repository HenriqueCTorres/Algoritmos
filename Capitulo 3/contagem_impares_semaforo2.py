# Contagem de ímpares - Semáforo - 04

# Definição da variável
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))

# Teste
if a % 2 == 0 and b % 2 == 0:
  print("Verde")
else:
  if a % 2 == 1 and b % 2 == 1:
    print("Vermelho")
  else:
    print("Amarelo")