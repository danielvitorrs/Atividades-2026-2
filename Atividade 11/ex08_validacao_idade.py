# Exercicio 8: aceita somente idades entre 0 e 120.
idade = int(input("Digite a idade: "))
while idade < 0 or idade > 120:
    print("Idade invalida.")
    idade = int(input("Digite uma idade entre 0 e 120: "))
print(f"Idade registrada: {idade}")
