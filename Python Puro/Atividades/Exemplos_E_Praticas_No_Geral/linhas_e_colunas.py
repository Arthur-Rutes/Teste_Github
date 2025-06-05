# numero = int(input("Qual Seu Numero: "))
# contador = 0
# elemento = ""
# coluna = 0

#Concatenar = Juntar#

# while contador < numero: # esse é para linhas
#     while coluna < numero: # esse é para colunas
#         elemento += "letra"
#         coluna += 1
#     print(elemento)
#     contador += 1

#---------------------------------------------------------------------------#

numero = int(input("Qual Seu Numero: "))
contador = 0

while contador < numero: #Numero De Linhas
    elemento = ""
    coluna = 0 
    while coluna < numero: #Definição Dos Elementos Nas Linhas
        if (coluna + contador) % 2 == 0:
            elemento += "0"
        else:
            elemento += "1"
        coluna += 1
    print(elemento)
    contador += 1