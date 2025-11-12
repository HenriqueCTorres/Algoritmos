# Algoritmo maior de 3 - Variável Auxiliar

# Definição da variável
maior = 0
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
if a > b:
  maior = a
else:
  maior = b
if c > maior:
  maior = c
print(f'O número maior é: {maior}')