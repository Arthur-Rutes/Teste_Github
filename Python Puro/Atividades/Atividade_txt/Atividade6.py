def escrever_diario():
    data = input("Digite A Data: ")
    
    descricao = input("Digite A Descrição Da Entrada Do Diario:\n")
    
    entrada = {
        "Data": data,
        "Descrição": descricao      
    }
    
    with open("diario.txt", "a", enconding="utf-8") as arquivo:
        arquivo.write(str(entrada) + "\n")
    
    
    print("Entrada Adicionada Com Sucesso!")

escrever_diario()