numeros = [7, 5, 1, 9, 3, 4, 6]

def lista_estrela(lista: list):    
    for i in lista:
        estrelas = "*" * i
        print(estrelas)
        

lista_estrela(numeros)