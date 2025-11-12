# Ordenação de Vetores - Bubble Sort - Olhar no W3Schools

# Definição da variável
v = [5, 12, 2, 17, 23, 1]
n = 6
u = n
print("O Vetor antigo é: ", v)

# Definição do laço e Teste
n = len(v)
for i in range(n-1):
  for j in range(n-i-1):
    if v[j] > v[j+1]:
      v[j], v[j+1] = v[j+1], v[j]
      print("O vetor na", i, "º tentavi é: ", v)

print(f"O Vetor arrumado ficará: {v}")
