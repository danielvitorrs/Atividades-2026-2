# Exercicio 35: ignora nomes que comecam com A.
nomes = []
for posicao in range(1, 11):
    nomes.append(input(f"Nome {posicao}: ").strip())
print("Nomes que nao comecam com A:")
for nome in nomes:
    if nome.upper().startswith("A"):
        continue
    print(nome)
