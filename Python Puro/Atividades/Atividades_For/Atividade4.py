positivos = [13, 41, 22, 64, 55, 81, 2, 4, 7, 9, 37, 93]

def numeros_pares(lista):
    pares = []
# % = Módulo
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

print(numeros_pares(positivos))