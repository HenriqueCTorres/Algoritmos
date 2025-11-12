# Ordenação de Vetores - Ordenação de Seleção

# Definição da variável
v = [5, 12, 2, 17, 23, 1]
n = 6
print(v)

# Definição do laço e Teste
for i in range(1, n):
  min = i
  for j in range(i + 1, n):
    if v[j] < v[min]:
      min = j
  c = v[min]
  v[min] = v[i]
  v[i] = c

print(f"O maior número: {v[i]}")
