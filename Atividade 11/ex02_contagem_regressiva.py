# Exercicio 2: contagem regressiva ate zero.
numero = int(input("Digite um numero inteiro positivo: "))
while numero < 0:
    numero = int(input("Valor invalido. Digite um numero positivo: "))
while numero >= 0:
    print(numero)
    numero -= 1
