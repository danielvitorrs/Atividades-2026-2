# Exercicio 6: calcula a media ate a sentinela -1.
soma = 0.0
quantidade = 0
while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    if not 0 <= nota <= 10:
        print("A nota deve estar entre 0 e 10.")
        continue
    soma += nota
    quantidade += 1
if quantidade:
    print(f"Media: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota valida foi informada.")
