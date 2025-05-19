dinheiro = float(input("Qual Valor Para Conversão: "))
#Taxa De Cambio = 5,75 R$
taxa = float(5.75)

conversao = round(dinheiro / taxa)

print(f"R$ {dinheiro} Passa Pela Taxa De {taxa} Converte Em Dolar: {conversao}")