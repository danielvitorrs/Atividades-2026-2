# Exercicio 10: encontra o maior valor; zero encerra e nao participa.
maior = None
while True:
    numero = int(input("Digite um inteiro (0 para encerrar): "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero
if maior is None:
    print("Nenhum numero foi informado antes do zero.")
else:
    print(f"Maior numero: {maior}")
