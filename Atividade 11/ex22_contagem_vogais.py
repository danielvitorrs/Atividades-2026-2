# Exercicio 22: conta vogais, sem diferenciar maiusculas e acentos.
import unicodedata

palavra = input("Digite uma palavra: ")
normalizada = unicodedata.normalize("NFD", palavra.lower())
quantidade = 0
for caractere in normalizada:
    if caractere in "aeiou":
        quantidade += 1
print(f"Quantidade de vogais: {quantidade}")
