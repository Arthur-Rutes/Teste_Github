#Var.count("")
#conta quantas vezes uma string ou inteiro tem dentro de um conjunto de dados

# string_teste = "Com quantos paus se fazem varias canoas se só paus fossem necessarios para fazer uma canoa."

# print(string_teste.count("se"))

#List.count()

# lista_teste = [5,9,7,1,3,4,6,25,5,3,1,5,7,5]
# print(lista_teste.count(7))

#Replace("", "")

# palavras_testes = "Oi, Oi, oi Amigos"
# novas_palavras = palavras_testes.replace("Oi", "Olá")
# print(novas_palavras)


#Pratica 1
argumento = "Três pratos de trigo para três tigres tristes"
def mais_caracteres(texto):
    maior_contagem = 0
    maior_caractere = ""
    
#For Usado Para Contagem Dos Caracteres.
    for i in argumento:
        contagem = argumento.count(i)
        if contagem > maior_contagem:
            maior_contagem = contagem
            maior_caractere = i
    
    return maior_caractere

#Replace Foi Usado Para Tirar Os Espaços Entre As Palavras.
print(mais_caracteres(argumento.replace(" ","")))