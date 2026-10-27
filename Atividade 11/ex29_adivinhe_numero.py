# Exercicio 29: tentativas para encontrar o numero secreto.
numero_secreto = 13
while True:
    palpite = int(input("Adivinhe o numero secreto (1 a 20): "))
    if not 1 <= palpite <= 20:
        print("Digite um numero entre 1 e 20.")
    elif palpite < numero_secreto:
        print("O numero secreto e maior.")
    elif palpite > numero_secreto:
        print("O numero secreto e menor.")
    else:
        print("Acertou!")
        break
