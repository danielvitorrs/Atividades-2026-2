# Exercicio 19: media de cinco notas e situacao do aluno.
soma = 0.0
for posicao in range(1, 6):
    nota = float(input(f"Digite a {posicao}a nota (0 a 10): "))
    while not 0 <= nota <= 10:
        nota = float(input("Nota invalida. Digite um valor de 0 a 10: "))
    soma += nota
media = soma / 5
print(f"Media: {media:.2f}")
print("Aprovado." if media >= 7 else "Reprovado.")
