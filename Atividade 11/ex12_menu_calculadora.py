# Exercicio 12: menu de operacoes basicas.
while True:
    print("\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        print("Programa encerrado.")
        break
    if opcao not in {"1", "2", "3"}:
        print("Opcao invalida.")
        continue
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    if opcao == "1":
        resultado = a + b
    elif opcao == "2":
        resultado = a - b
    else:
        resultado = a * b
    print(f"Resultado: {resultado}")
