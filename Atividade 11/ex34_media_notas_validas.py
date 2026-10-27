# Exercicio 34: le dez notas, ignorando valores fora de 0 a 10.
soma = 0.0
quantidade = 0
for posicao in range(1, 11):
    nota = float(input(f"Nota {posicao}: "))
    if nota < 0 or nota > 10:
        print("Nota ignorada.")
        continue
    soma += nota
    quantidade += 1
if quantidade:
    print(f"Media das notas validas: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota valida foi informada.")
