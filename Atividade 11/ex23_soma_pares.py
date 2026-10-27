# Exercicio 23: soma dos pares de 1 a 100.
soma = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero
print(f"Soma dos numeros pares: {soma}")
