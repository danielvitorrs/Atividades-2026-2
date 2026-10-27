# Exercicio 15: contabiliza votos 1, 2 e 3; zero encerra.
votos = {1: 0, 2: 0, 3: 0}
while True:
    try:
        voto = int(input("Vote em 1, 2 ou 3 (0 para encerrar): "))
    except ValueError:
        print("Digite um numero inteiro.")
        continue
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Opcao invalida; voto nao contabilizado.")
print("Resultado da votacao:")
for opcao, total in votos.items():
    print(f"Opcao {opcao}: {total} voto(s)")
