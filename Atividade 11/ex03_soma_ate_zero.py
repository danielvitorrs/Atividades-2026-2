# Exercicio 3: soma valores ate que zero seja informado.
soma = 0
while True:
    numero = int(input("Digite um numero (0 para encerrar): "))
    if numero == 0:
        break
    soma += numero
print(f"Soma: {soma}")
