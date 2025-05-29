# nome = input("Digite alguma coisa aí: ")

# #"digito" É Como A Variável Definida Para Cada Letra Do Input "nome".
# for digito in nome:
#     #Para Fazer Ficar Na Mesma Linha.
#     print(digito,end="*")
#     #Para Deixar Cada Palavra Em Uma Linha
#     #print(digito + "*")


#1°Prática
# numero = int(input("Insira um numero(Positivo > 0) aí: "))

# for i in range(-numero, numero + 1):
    
#     if i != 0:
#         print(i,end="|")
#------------------------------------------------------------------#
#------------------------------------------------------------------#
#------------------------------------------------------------------#
#Lista Bidimensional
#[x]=Linha [y]=Coluna
# lista_bidimensional= [[0,1,2,3],
#                       [3,9,7,1],
#                       [8,3,4,7],
#                       [6,3,2,9]]
#print(lista_bidimensional[x][y])
# print(lista_bidimensional[3][1])

#Prática 1

# lista = [[1,2,3,4],
#          [4,3,2,1],
#          [3,1,2,4],
#          [2,4,1,3]]

# def conta_elementos_match(matriz, elemento):
    
#     contagem = 0
#     for linha in matriz:
#         for item in linha:
#             if item == elemento:
#                 contagem += 1

#     return contagem

# print(conta_elementos_match(lista,3))

#Prática 2

sudoku = [
[9, 0, 0, 0, 8, 0, 3, 0, 0],
[0, 0, 0, 2, 5, 0, 7, 0, 0],
[0, 2, 0, 3, 0, 0, 0, 0, 4],
[0, 9, 4, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 7, 3, 0, 5, 6, 0],
[7, 0, 5, 0, 6, 0, 4, 0, 0],
[0, 0, 7, 8, 0, 3, 9, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 2]
]

def jogo_sudoku(tabela):

    for linha in tabela:
        for item in linha:
            if item == 0:
                print("_ ", end="")
            else:
                print(item,"",end="")
        print("")

jogo_sudoku(sudoku)