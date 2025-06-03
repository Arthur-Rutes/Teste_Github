def lista_crescente():
    numeros = []

    while True:
        nimero = int(input("Digite Um Numero: "))
        numeros.append(nimero)
        if len(numeros) > 1 and numeros[-1] < numeros[-2]:
            break
    
    numeros_ordenados = sorted(numeros)
    print("Números Digitados (Ordem Crescente):", numeros_ordenados)

lista_crescente()