def verificao(disponiveis):

    while True:
        desejo = input("O Que Desejas ('sair' Para Encerrar): ")
        if desejo == "sair":
            print("Encerrando Verificação")
            break
        
        if desejo in disponiveis:
            print("Produto Disponivel.")
        else:
            print("Produto Não Disponivel")


disponiveis = ["caneta", "lapis", "borracha", "caderno"]            
verificao(disponiveis)
#Encerrou A Verificação Da 1°Lista De Produtos "disponiveis"
outros = ["cadeira", "mouse", "teclado", "fones"]
verificao(outros)
#Aqui Encerra A 2°Lista De Produtos "outros"