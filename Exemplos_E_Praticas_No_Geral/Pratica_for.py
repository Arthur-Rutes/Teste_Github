# nome = input("Digite alguma coisa aí: ")

# #"digito" É Como A Variável Definida Para Cada Letra Do Input "nome".
# for digito in nome:
#     #Para Fazer Ficar Na Mesma Linha.
#     print(digito,end="*")
#     #Para Deixar Cada Palavra Em Uma Linha
#     #print(digito + "*")


#2°Prática
numero = int(input("Insira um numero(Positivo > 0) aí: "))

for i in range(-numero, numero + 1):
    
    if i != 0:
        print(i,end="\/")
    
