# Vetores e Matrizes - Matriz
# No python não tem também como criar Matriz

# Definição da variável
def gerar_matriz (n_linhas, n_colunas):
    return [[" "]*n_colunas for _ in range(n_linhas)]

# Definição do laço e Teste
n_linhas = int(input("Digite o total de linhas: "))
n_colunas = int(input("Digite o total de colunas: "))

print(gerar_matriz(n_linhas, n_colunas))