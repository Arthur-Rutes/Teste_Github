maiores = {}
try:
    with open("atividades/arquivos/dados.csv") as L:
        for linha in L:
            if linha:
                partes = linha.split(",")
                maiores[partes[0]] = int(partes[1])





except FileNotFoundError:
    print("Arquivo Solicitado Não Encontrado")