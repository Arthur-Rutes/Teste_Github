ano = int(input("Algum Ano Aí: "))


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse Daí É Bissexto Pai.")

else:
    print("Esse Dai Não É Bissexto Não Pai.")