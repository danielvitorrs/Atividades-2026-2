# Exercicio 44: ordenacao decrescente usando sort().
numeros = []
for posicao in range(1, 16):
    numeros.append(int(input(f"Numero {posicao}: ")))
numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)
