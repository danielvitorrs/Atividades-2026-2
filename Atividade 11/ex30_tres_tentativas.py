# Exercicio 30: bloqueia apos tres senhas incorretas.
senha_correta = "python123"
for tentativa in range(1, 4):
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso autorizado.")
        break
    restantes = 3 - tentativa
    if restantes:
        print(f"Senha incorreta. Tentativas restantes: {restantes}.")
else:
    print("Acesso bloqueado.")
