# Exercicio 25: maior, menor e media das notas de dez alunos.
notas = []
for posicao in range(1, 11):
    nota = float(input(f"Nota do aluno {posicao} (0 a 10): "))
    while not 0 <= nota <= 10:
        nota = float(input("Nota invalida. Digite um valor de 0 a 10: "))
    notas.append(nota)
print(f"Maior nota: {max(notas):.2f}")
print(f"Menor nota: {min(notas):.2f}")
print(f"Media da turma: {sum(notas) / len(notas):.2f}")
