try:
    with open("atividades/arquivos/dados.csv") as L:
        with open("dados_maiores.csv", "w") as arquivo_saida:
            for linha in L:
                linha = linha.replace("\n","")
                if linha:
                    # Split Serve Para Dividir Os Argumentos Das Linhas.
                    partes = linha.split(",")
                    nome = partes[0]
                    idade = partes[1]
                    if int(idade) >= 18:
                        arquivo_saida.write(linha + "\n")
    print("Arquivo 'dados_maiores.csv' Foi Criado Com Sucesso.")


except ValueError:
    print("Erro: Conflito De Valores (str,int)")

except FileNotFoundError:
    print("Arquivo Solicitado Não Encontrado")