# Contagem de ímpares - 02

# Definição da variável
s = 0
a = int(input("Digite o seu número A: "))
b = int(input("Digite o seu número B: "))
c = int(input("Digite o seu número C: "))

# Teste
s = a % 2 + b % 2 + c % 2
print(f'A soma de todos números ímpares é: {s}')