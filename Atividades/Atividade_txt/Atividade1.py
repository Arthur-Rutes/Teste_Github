def frutas():
    venda = {}

    try:
        with open("atividades/arquivos/frutas.csv") as novo_arquivo:
            for linha in novo_arquivo:
                linha = linha.replace("\n","")
                if linha:
                    partes = linha.split(";")
                    venda[partes[0]] = float(partes[1])
            
    except FileNotFoundError:
        print("Arquivo Pedido Não Encontrado")

    except ValueError:
        print("Erro Ao Converter O Preço Para Float")


    return venda

print(frutas())