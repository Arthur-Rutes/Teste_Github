from math import sqrt

while True:
    inteiro = int(input("Digite Um Número Inteiro: "))
    if inteiro == 0:
        print("Encerrando O Programa.")
        break
    elif inteiro < 0:
        print("Número Inválido.")
    else:
        raiz = sqrt(inteiro)
        print(f"A Raiz Quadrada De {inteiro} É {raiz}, Beleza Pai.")