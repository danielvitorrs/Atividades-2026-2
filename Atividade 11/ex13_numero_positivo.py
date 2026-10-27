# Exercicio 13: continua pedindo ate receber inteiro positivo.
numero = int(input("Digite um inteiro positivo: "))
while numero <= 0:
    numero = int(input("Valor invalido. Tente novamente: "))
print(f"Numero positivo recebido: {numero}")
