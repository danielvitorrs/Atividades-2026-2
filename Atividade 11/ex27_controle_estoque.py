# Exercicio 27: registra retiradas sem permitir estoque negativo.
estoque = int(input("Quantidade inicial em estoque: "))
while estoque < 0:
    estoque = int(input("A quantidade nao pode ser negativa. Informe novamente: "))
while estoque > 0:
    print(f"Estoque atual: {estoque}")
    retirada = int(input("Quantidade a retirar: "))
    if retirada <= 0:
        print("A retirada deve ser positiva.")
    elif retirada > estoque:
        print("Retirada maior que o estoque disponivel.")
    else:
        estoque -= retirada
print("Estoque zerado.")
