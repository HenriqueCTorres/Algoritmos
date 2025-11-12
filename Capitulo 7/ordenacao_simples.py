# Introdução a Ordenação de Vetores - Ordenação Simples

# Definição da variável
v = [5, 12, 2, 17, 23, 1]
n = 6
print(v)

# Definição do laço e Teste
for i in range(1, n):
  for j in range(i + 1, n):
    if v[i] > v[j]:
      c = v[i]
      v[i] = v[j]
      v[j] = c

print(f"O maior número: {v[j]}")
