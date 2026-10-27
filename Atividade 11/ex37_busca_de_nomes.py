# Exercicio 37: pesquisa nome em uma lista de alunos.
alunos = []
for posicao in range(1, 11):
    alunos.append(input(f"Nome do aluno {posicao}: ").strip())
busca = input("Nome a pesquisar: ").strip()
encontrado = False
for aluno in alunos:
    if aluno.casefold() == busca.casefold():
        encontrado = True
        break
print("Aluno cadastrado." if encontrado else "Aluno nao cadastrado.")
