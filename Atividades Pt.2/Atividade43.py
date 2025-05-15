ano = int(input("Diga-nos Um Ano: "))


while True:
    ano += 1
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400==0):
        print(f"{ano} É Um Ano Bissexto.")
        break