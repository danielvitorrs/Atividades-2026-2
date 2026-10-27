# Exercicio 41: busca binaria em lista ordenada de vinte valores.
numeros = []
for posicao in range(1, 21):
    numeros.append(int(input(f"Digite o {posicao}o inteiro da lista ordenada: ")))
if any(numeros[i] > numeros[i + 1] for i in range(len(numeros) - 1)):
    print("A lista precisa estar em ordem crescente.")
else:
    alvo = int(input("Numero a procurar: "))
    inicio, fim = 0, len(numeros) - 1
    indice_encontrado = None
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if numeros[meio] == alvo:
            indice_encontrado = meio
            break
        if numeros[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    if indice_encontrado is None:
        print("Numero nao encontrado.")
    else:
        print(f"Numero encontrado no indice {indice_encontrado}.")
