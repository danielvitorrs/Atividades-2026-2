# Exercicio 45: Bubble Sort crescente, sem sort() ou sorted().
numeros = [int(valor) for valor in input("Digite dez inteiros separados por espaco: ").split()]
while len(numeros) != 10:
    print("Informe exatamente dez valores.")
    numeros = [int(valor) for valor in input("Digite dez inteiros separados por espaco: ").split()]
for fim in range(len(numeros) - 1, 0, -1):
    houve_troca = False
    for indice in range(fim):
        if numeros[indice] > numeros[indice + 1]:
            numeros[indice], numeros[indice + 1] = numeros[indice + 1], numeros[indice]
            houve_troca = True
    if not houve_troca:
        break
print("Lista ordenada:", numeros)
