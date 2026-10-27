# Exercicio 9: fatorial calculado com while.
numero = int(input("Digite um inteiro nao negativo: "))
while numero < 0:
    numero = int(input("Valor invalido. Digite um inteiro nao negativo: "))
resultado = 1
contador = 1
while contador <= numero:
    resultado *= contador
    contador += 1
print(f"{numero}! = {resultado}")
