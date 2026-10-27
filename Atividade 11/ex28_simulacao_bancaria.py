# Exercicio 28: depositos e saques com saldo atualizado.
saldo = float(input("Saldo inicial: R$ "))
while saldo < 0:
    saldo = float(input("O saldo inicial nao pode ser negativo. Informe novamente: R$ "))
while True:
    print("\n1 - Depositar\n2 - Sacar\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao not in {"1", "2"}:
        print("Opcao invalida.")
        continue
    valor = float(input("Valor: R$ "))
    if valor <= 0:
        print("O valor deve ser positivo.")
    elif opcao == "1":
        saldo += valor
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
    print(f"Saldo atual: R$ {saldo:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")
