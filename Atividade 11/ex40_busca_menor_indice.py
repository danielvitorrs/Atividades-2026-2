# Exercicio 40: menor valor e indice sem usar min().
numeros = []
for posicao in range(1, 21):
    numeros.append(int(input(f"Numero {posicao}: ")))
menor = numeros[0]
indice_menor = 0
for indice in range(1, len(numeros)):
    if numeros[indice] < menor:
        menor = numeros[indice]
        indice_menor = indice
print(f"Menor valor: {menor}; indice: {indice_menor}")
