# Exercicio 50: cadastro e analise com buscas comparadas.
numeros = []
for posicao in range(1, 21):
    numeros.append(int(input(f"Numero {posicao}: ")))

while True:
    print("\n1 - Media\n2 - Maior e menor\n3 - Ordem crescente\n4 - Ordem decrescente")
    print("5 - Busca linear\n6 - Busca binaria\n7 - Comparar buscas\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        print(f"Media: {sum(numeros) / len(numeros):.2f}")
    elif opcao == "2":
        maior = menor = numeros[0]
        for numero in numeros[1:]:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        print(f"Maior: {maior}; menor: {menor}")
    elif opcao == "3":
        print("Ordem crescente:", sorted(numeros))
    elif opcao == "4":
        print("Ordem decrescente:", sorted(numeros, reverse=True))
    elif opcao in {"5", "6", "7"}:
        alvo = int(input("Numero a pesquisar: "))
        comparacoes_lineares = 0
        indice_linear = None
        if opcao in {"5", "7"}:
            for indice, numero in enumerate(numeros):
                comparacoes_lineares += 1
                if numero == alvo:
                    indice_linear = indice
                    break
        if opcao == "5":
            print(f"Busca linear: indice {indice_linear}; comparacoes: {comparacoes_lineares}.")
        else:
            ordenados = sorted(numeros)
            inicio, fim = 0, len(ordenados) - 1
            indice_binario = None
            comparacoes_binarias = 0
            while inicio <= fim:
                meio = (inicio + fim) // 2
                comparacoes_binarias += 1
                if ordenados[meio] == alvo:
                    indice_binario = meio
                    break
                if ordenados[meio] < alvo:
                    inicio = meio + 1
                else:
                    fim = meio - 1
            if opcao == "6":
                print(f"Busca binaria: indice na lista ordenada {indice_binario}; comparacoes: {comparacoes_binarias}.")
            else:
                print(f"Busca linear: indice original {indice_linear}; comparacoes: {comparacoes_lineares}.")
                print(f"Busca binaria: indice na lista ordenada {indice_binario}; comparacoes: {comparacoes_binarias}.")
    else:
        print("Opcao invalida.")
print("Sistema encerrado.")
