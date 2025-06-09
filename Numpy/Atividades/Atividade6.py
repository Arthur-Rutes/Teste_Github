import numpy as np
def somar_matrizes(m1,m2):
    if np.shape(m1) == np.shape(m2):
        return m1 + m2
    else:
        return "Erro: As Matrizes Devem Ser Do Mesmo Tamanho."

matriz1 = np.array([[1,8],[6,2],[7,3]])
matriz2 = np.array([[4,5],[5,3],[8,6]])

print(somar_matrizes(matriz1,matriz2))