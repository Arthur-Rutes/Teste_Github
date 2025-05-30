def lista_telefonica():
    agenda = {}  
 
    while True:
        comando = input("Comando (1 busca, 2 adiciona, 3 sai): ")
 
        if comando == "1":
            nome = input("nome: ")
            if nome in agenda:
                print("número:", agenda[nome])
            else:
                print("nenhum número")
 
        elif comando == "2":
            nome = input("nome: ")
            numero = input("número: ")
            agenda[nome] = numero
            print("ok!")
        elif comando == "3":
            print("saindo...")
            print(agenda)
            break
        else:
            print("Comando inválido. Tente novamente.")          
lista_telefonica()

