# Introdução a Pesquisa Sequencial - Direta

# Definição da variável
v = [5, 12, 2, 17, 23, 1, 18]
n = 7
print("O número que queremos achar é: 17")

# Definição do laço e Teste
achei = 0
i = 0
for i in range(len(v)):
  if v[i] == 17:
    print("A posição em que o elementos está é: ", i)