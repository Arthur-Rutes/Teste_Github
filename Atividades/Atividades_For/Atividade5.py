parte1 = [7, 8, 6, 4, 11, 5, 24]
parte2 = [8, 1, 2, 5, 6, 17, 47]

def lista_soma(lista1, lista2):
    soma = []

    for i in range(len(parte1)):
        aumento = parte1[i] + parte2[i]
        soma.append(aumento)
    return soma

print(lista_soma(parte1, parte2))