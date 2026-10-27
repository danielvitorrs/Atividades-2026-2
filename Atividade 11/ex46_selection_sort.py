# Exercicio 46: Selection Sort crescente.
numeros = [int(valor) for valor in input("Digite numeros separados por espaco: ").split()]
for inicio in range(len(numeros) - 1):
    indice_menor = inicio
    for indice in range(inicio + 1, len(numeros)):
        if numeros[indice] < numeros[indice_menor]:
            indice_menor = indice
    numeros[inicio], numeros[indice_menor] = numeros[indice_menor], numeros[inicio]
print("Lista ordenada:", numeros)
