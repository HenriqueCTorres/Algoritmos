# Bhaskara

# Definição da variável
x1 = 0
x2 = 0
delta = 0
raiz = 0
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a == 0:
  print("Não existe raiz")

delta = b * b - 4 * a * c

if delta < 0:
  print("A equação não tem raízes reais")
else:
  print("A equação tem raízes reais")