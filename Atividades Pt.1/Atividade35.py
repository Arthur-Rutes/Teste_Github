pontos = int(input("Quantos Pontos Você Recebeu: "))

if pontos < 0:
    print("Impossível.")


elif pontos > 0 and pontos <= 49:
    print("Você Fracassou No Teste.")


elif pontos >= 50 and pontos <= 59:
    print("Sua Nota Final Foi 1.")


elif pontos >= 60 and pontos <= 69:
    print("Sua Nota Final Foi 2.")


elif pontos >= 70 and pontos <= 79:
    print("Sua Nota Final Foi 3.")


elif pontos >= 80 and pontos <= 89:
    print("Sua Nota Final Foi 4.")


elif pontos >= 90 and pontos <= 100:
    print("Sua Nota Final Foi 5.")
    

elif pontos > 100:
    print("Impossível.")