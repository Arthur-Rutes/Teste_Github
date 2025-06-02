def lista_telefonica():
    agenda = {}

    while True:
        comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
         
        if comando == "1":
            nome = input("nome: ")
            if nome in agenda:
                print("números:")
                i = 0
                while i < len(agenda[nome]):
                    print(agenda[nome][i])
                    i += 1
            else:
                print("nenhum número")
 
        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            #Caso o nome já esteja presente no dicionario, ele só vai adicionar o novo numero do usuario.
            if nome in agenda:
                agenda[nome].append(numero)
            else:
                agenda[nome] = [numero]
            print("ok!")

        elif comando == "3":
            print("saindo...")
            print(agenda)
            break

        else:
            print("Comando inválido. Tente novamente.")

lista_telefonica()