# Exercicio 20: potencia por multiplicacoes sucessivas, sem **.
base = float(input("Base: "))
expoente = int(input("Expoente inteiro nao negativo: "))
while expoente < 0:
    expoente = int(input("Expoente invalido. Digite um valor nao negativo: "))
resultado = 1
for _ in range(expoente):
    resultado *= base
print(f"Resultado: {resultado}")
