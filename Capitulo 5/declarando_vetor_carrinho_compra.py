# Vetores e Matrizes - Carrinho de Compra

# Definição da variável
v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definição do laço e Teste
media = 0
for i in range(0, 10):
  v[i] = int(input("Digite o preço: "))
  media = media + v[i]
media = media / 5
print(media)
