# Exercicio 11: pede a senha ate que esteja correta.
senha_correta = "python123"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso autorizado.")
        break
    print("Senha incorreta. Tente novamente.")
