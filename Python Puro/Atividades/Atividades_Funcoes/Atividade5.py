#Definir A Função
def Repetir(palavra, tamanho):
    #Variavel Que Multiplica A String Pelo Numero Passado Como Parametro
    string_total = (palavra * tamanho)
    #Variavel Que Inicia Em Zero Para Posteriormente Ser Usado Como Controle
    linha = 0
    while linha < tamanho:
        coluna = 0
        letras = " "
        while coluna < tamanho:
            posicao = linha * tamanho + coluna
            letras += string_total[posicao]
            coluna += 1
        print(letras)
        linha += 1

Repetir("Pneumonia", 7)