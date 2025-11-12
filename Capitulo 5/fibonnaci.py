# Vetores e Matrizes - Fibonacci

# Definição da variável
v = []

# Definição do laço e Teste
n = int(input("Digite até qual número de Fibonacci você deseja ver: "))
a = 0
b = 1

for i in range(n):
    v.append(str(a))
    c = a + b
    a = b
    b = c

print(' '.join(v))
