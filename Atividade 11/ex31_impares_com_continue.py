# Exercicio 31: ignora pares e apresenta impares com continue.
for numero in range(1, 101):
    if numero % 2 == 0:
        continue
    print(numero)
