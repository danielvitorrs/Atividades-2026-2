# Exercicio 43: ordenacao crescente usando sorted().
numeros = []
for posicao in range(1, 11):
    numeros.append(int(input(f"Numero {posicao}: ")))
print("Ordem crescente:", sorted(numeros))
