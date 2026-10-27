# Exercicio 32: le dez valores e ignora os negativos.
soma = 0
for posicao in range(1, 11):
    numero = int(input(f"Digite o {posicao}o inteiro: "))
    if numero < 0:
        continue
    soma += numero
print(f"Soma dos valores nao negativos: {soma}")
