# Exercicio 38: mostra o indice em que o valor aparece.
numeros = [int(valor) for valor in input("Digite inteiros separados por espaco: ").split()]
alvo = int(input("Valor a procurar: "))
indice_encontrado = None
for indice, numero in enumerate(numeros):
    if numero == alvo:
        indice_encontrado = indice
        break
if indice_encontrado is None:
    print("Valor nao encontrado.")
else:
    print(f"Valor encontrado no indice {indice_encontrado}.")
