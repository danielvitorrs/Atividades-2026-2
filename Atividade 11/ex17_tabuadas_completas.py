# Exercicio 17: tabuadas de 1 a 10.
for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")
    for fator in range(1, 11):
        print(f"{numero} x {fator} = {numero * fator}")
