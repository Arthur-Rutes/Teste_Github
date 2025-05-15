senha = int(input("Crie Uma Senha: "))

while True:
    confirmacao = int(input("Redigite A Senha: "))
    if confirmacao == senha:
        print("Senha Correta.")
        break
    else:
        print("Senha Incorreta. Tente Novamente.")