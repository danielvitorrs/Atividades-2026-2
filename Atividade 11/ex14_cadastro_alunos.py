# Exercicio 14: cadastra nomes ate o usuario encerrar.
alunos = []
while True:
    nome = input("Nome do aluno: ").strip()
    while not nome:
        nome = input("O nome nao pode ficar vazio. Digite novamente: ").strip()
    alunos.append(nome)
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    while continuar not in {"s", "n"}:
        continuar = input("Responda s ou n: ").strip().lower()
    if continuar == "n":
        break
print("Alunos cadastrados:")
for aluno in alunos:
    print(f"- {aluno}")
