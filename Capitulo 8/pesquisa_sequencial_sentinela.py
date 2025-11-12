# Pesquisa Sequencial - Com Sentinela

# Definição do laço e Teste
def busca_sentinela(arr, x):
    n = len(arr)
    # Adiciona o elemento a ser procurado no final
    arr.append(x)

    i = 0
    while arr[i] != x:
        i += 1

    # Remove a sentinela para não alterar o array original
    arr.pop()

    # Se o elemento for encontrado no último índice (da sentinela),
    # ele não estava originalmente na lista.
    if i == n:
        return -1  # Elemento não encontrado
    else:
        return i  # Elemento encontrado no índice i

# Exemplo de uso
lista = [10, 20, 80, 30, 60, 50]
valor_a_buscar = 60

posicao = busca_sentinela(lista, valor_a_buscar)

if posicao != -1:
    print(f"O elemento {valor_a_buscar} foi encontrado na posição {posicao}")
else:
    print(f"O elemento {valor_a_buscar} não foi encontrado")

valor_a_buscar = 100
posicao = busca_sentinela(lista, valor_a_buscar)

if posicao != -1:
    print(f"O elemento {valor_a_buscar} foi encontrado na posição {posicao}")
else:
    print(f"O elemento {valor_a_buscar} não foi encontrado")