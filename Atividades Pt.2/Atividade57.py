texto = input("Escreva algo bacana ai: ")

if len(texto) < 20: #Errado
    asteriscos = "*" * (20 - len(texto)) #Errado
    resultado = asteriscos + texto #Errado
    
else:
    resultado = texto[:20]
    print("Resultado Formatado:", resultado)
    
    #Exercicio Está 50% Errado