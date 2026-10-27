# Exercicio 42: compara o numero de comparacoes das duas buscas.
numeros = []
for posicao in range(1, 21):
    numeros.append(int(input(f"Digite o {posicao}o inteiro da lista ordenada: ")))
if any(numeros[i] > numeros[i + 1] for i in range(len(numeros) - 1)):
    print("A lista precisa estar em ordem crescente.")
else:
    alvo = int(input("Numero a procurar: "))
    comparacoes_lineares = 0
    indice_linear = None
    for indice, valor in enumerate(numeros):
        comparacoes_lineares += 1
        if valor == alvo:
            indice_linear = indice
            break

    comparacoes_binarias = 0
    inicio, fim = 0, len(numeros) - 1
    indice_binario = None
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_binarias += 1
        if numeros[meio] == alvo:
            indice_binario = meio
            break
        if numeros[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    print(f"Busca linear: {comparacoes_lineares} comparacao(oes); indice {indice_linear}.")
    print(f"Busca binaria: {comparacoes_binarias} comparacao(oes); indice {indice_binario}.")
