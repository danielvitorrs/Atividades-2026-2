# Exercicio 36: busca linear em dez inteiros.
numeros = []
for posicao in range(1, 11):
    numeros.append(int(input(f"Numero {posicao}: ")))
alvo = int(input("Numero a procurar: "))
encontrado = False
for numero in numeros:
    if numero == alvo:
        encontrado = True
        break
print("Numero encontrado." if encontrado else "Numero nao encontrado.")
