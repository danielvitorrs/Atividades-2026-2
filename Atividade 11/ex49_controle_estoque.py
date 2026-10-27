# Exercicio 49: cadastro, quantidade, busca e ordem alfabetica.
produtos = []
while True:
    print("\n1 - Cadastrar produto\n2 - Listar em ordem alfabetica\n3 - Buscar por nome\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        nome = input("Nome do produto: ").strip()
        while not nome:
            nome = input("Nome vazio. Digite novamente: ").strip()
        quantidade = int(input("Quantidade: "))
        while quantidade < 0:
            quantidade = int(input("A quantidade nao pode ser negativa: "))
        produto = None
        for item in produtos:
            if item["nome"].casefold() == nome.casefold():
                produto = item
                break
        if produto:
            produto["quantidade"] += quantidade
            print("Quantidade do produto atualizada.")
        else:
            produtos.append({"nome": nome, "quantidade": quantidade})
            print("Produto cadastrado.")
    elif opcao == "2":
        ordenados = sorted(produtos, key=lambda item: item["nome"].casefold())
        if not ordenados:
            print("Nenhum produto cadastrado.")
        for item in ordenados:
            print(f"{item['nome']}: {item['quantidade']} unidade(s)")
    elif opcao == "3":
        busca = input("Nome do produto: ").strip()
        encontrado = None
        for item in produtos:
            if item["nome"].casefold() == busca.casefold():
                encontrado = item
                break
        if encontrado:
            print(f"{encontrado['nome']}: {encontrado['quantidade']} unidade(s)")
        else:
            print("Produto nao encontrado.")
    else:
        print("Opcao invalida.")
print("Sistema encerrado.")
