# Exercicio 47: Insertion Sort e estado da lista apos cada insercao.
numeros = [int(valor) for valor in input("Digite numeros separados por espaco: ").split()]
for indice in range(1, len(numeros)):
    valor = numeros[indice]
    posicao = indice - 1
    while posicao >= 0 and numeros[posicao] > valor:
        numeros[posicao + 1] = numeros[posicao]
        posicao -= 1
    numeros[posicao + 1] = valor
    print(f"Apos inserir {valor}: {numeros}")
print("Lista ordenada:", numeros)
