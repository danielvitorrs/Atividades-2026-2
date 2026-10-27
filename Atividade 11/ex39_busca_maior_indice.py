# Exercicio 39: maior valor e indice sem usar max().
numeros = []
for posicao in range(1, 21):
    numeros.append(int(input(f"Numero {posicao}: ")))
maior = numeros[0]
indice_maior = 0
for indice in range(1, len(numeros)):
    if numeros[indice] > maior:
        maior = numeros[indice]
        indice_maior = indice
print(f"Maior valor: {maior}; indice: {indice_maior}")
