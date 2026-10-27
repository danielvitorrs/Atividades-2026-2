# Exercicio 18: soma dez numeros inteiros.
soma = 0
for posicao in range(1, 11):
    soma += int(input(f"Digite o {posicao}o numero: "))
print(f"Soma total: {soma}")
