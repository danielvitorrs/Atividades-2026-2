# Exercicio 48: cadastro, notas, medias e busca linear de alunos.
alunos = []
while True:
    print("\n1 - Cadastrar aluno\n2 - Listar alunos\n3 - Pesquisar aluno\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        nome = input("Nome: ").strip()
        while not nome:
            nome = input("Nome vazio. Digite novamente: ").strip()
        notas = []
        for posicao in range(1, 4):
            nota = float(input(f"Nota {posicao} (0 a 10): "))
            while not 0 <= nota <= 10:
                nota = float(input("Nota invalida. Digite de 0 a 10: "))
            notas.append(nota)
        alunos.append({"nome": nome, "notas": notas})
        print("Aluno cadastrado.")
    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"{aluno['nome']}: media {media:.2f}")
    elif opcao == "3":
        busca = input("Nome a pesquisar: ").strip()
        encontrado = None
        for aluno in alunos:
            if aluno["nome"].casefold() == busca.casefold():
                encontrado = aluno
                break
        if encontrado:
            media = sum(encontrado["notas"]) / len(encontrado["notas"])
            print(f"{encontrado['nome']} - notas: {encontrado['notas']} - media: {media:.2f}")
        else:
            print("Aluno nao encontrado.")
    else:
        print("Opcao invalida.")
print("Sistema encerrado.")
