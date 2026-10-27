# Exercicio 33: apresenta valores de 1 a 100 exceto multiplos de 3.
for numero in range(1, 101):
    if numero % 3 == 0:
        continue
    print(numero)
