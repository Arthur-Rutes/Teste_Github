quantidade = int(input("Tamanho Do Tabuleiro: "))

def xadrez(tamanho):
    linha = 0
    while linha < tamanho:
        coluna = 0
        linha_texto = ""
        while coluna < tamanho:
            if (linha + coluna) % 2 == 0:
                linha_texto += "1"
            else:
                linha_texto += "0"
            coluna += 1
        print(linha_texto)
        linha += 1

xadrez(quantidade)