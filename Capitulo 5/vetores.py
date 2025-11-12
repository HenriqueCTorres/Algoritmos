# Introdução Vetores e Matrizes - Vetores

# Definição da variável
v = [1, 2, 3, 4, 5]

# Definição do laço e Teste
media = 0
for i in range(0, 5):
  v[i] = int(input("Digite a nota: "))
  media = media + v[i]
media = media / 5
print(media)
