import numpy as np
def gerar_array_intervalo():
    n1 = int(input("Qual Será O Primeiro Numero: "))
    n2 = int(input("Qual Será O Segundo Numero: "))
    contagem = np.arange(n1,n2+1)
    print(contagem)

gerar_array_intervalo()