#dicionario

#Usado para armazenar dados no formato: Chave:valor
#são ordenados
#mutáveis
#Não permite elementos duplicados

# meu_dicionario = {}
# meu_dicionario["apina"] = "Macaco"
# meu_dicionario["nome"] = "Jonas"
# meu_dicionario["troxa"] = "Pessoa"

# print(meu_dicionario)
# print(meu_dicionario["nome"])

# palavra = input("Digite uma palavra: ")


# if palavra in meu_dicionario:
#     print("Tradução:", meu_dicionario[palavra])
    
# else:
#     print("Palavra Não Encontrada")
    
    
    
# resultado = {}
# resultado["Mario"] = 5
# resultado["Julia"] = 10

# soma = resultado["Mario"] + resultado["Julia"]

# print(soma)


#Imprimir Chave Avalor


# dicionario = {}

# dicionario["apina"] = "Macaco"
# dicionario["banana"] = "Amarelo"
# dicionario["cembalo"] = "Cravo"

# for chave in dicionario:
#     print("Chave:", chave)
#     print("Valor:", dicionario[chave])





#Popular

# lista_palavras = [
#   "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#   "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#   "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
# ]


# def contagens(minha_lista):
#     palavras = {}
#     for palavra in minha_lista:
#         if palavra not in palavras:
#             palavras[palavra] = 0
#         palavras[palavra] += 1
            
#     return palavras

# print(contagens(lista_palavras))


#Prática
# def histogram(palavra):
#     contar = {}
# #For Que Serve Para Contar As Letras Das Palavras.
#     for letra in palavra:
#         if letra in contar:
#             contar[letra] += 1
#         else:
#             contar[letra] = 1
# #For Que Serve Para Printar Tudo Do Jeito Certo.
#     for letra in contar:
#         print(letra + ": " + "*" * contar[letra])



# histogram("Rubbles From Stone")

# Deletando Chaves #
# del #
# staff = {"Alan":"Professor", "Emily":"Aluna", "Davi":"Professor"}
# del staff["Alan"]
# print(staff)


# pop #
# pop pode ser usado para armazenar a entidade "deletada" #
# deletado = staff.pop("Emily")

# print(deletado)


#Estruturar dados com o dicionario
Pessoa1 = {"Nome":"Peppa Pig","Altura":135,"Peso":105,"Idade":14}
Pessoa2 = {"Nome":"Lilo Stitch","Altura":50,"Peso":35,"Idade":200}
Pessoa3 = {"Nome":"Ariel","Altura":175,"Peso":200,"Idade":15}

Pessoas = [Pessoa1, Pessoa2, Pessoa3]

for pessoa in Pessoas:
    print(f"Nome: {pessoa["Nome"]}")
    print(f"Idade: {pessoa["Idade"]}")
    print(f"Altura: {pessoa["Altura"]}")
    print(f"Peso: {pessoa["Peso"]}")
    print(" ")
    
# altura_combinada = 0

# for pessoa in Pessoas:
#     altura_combinada += pessoa["Altura"]

# print(f"Altura combinada: {altura_combinada}")