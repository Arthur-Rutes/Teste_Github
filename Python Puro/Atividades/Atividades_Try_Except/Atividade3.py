frutas = ["Banana", "Goiaba", "Dragonfruit", "Abacaxi", "Maçã"]

try:
    comprar = int(input("Fale Um Número: "))
    print (frutas[comprar])
    
except IndexError:
    print("Índice Fora Do Alcance.")

except ValueError:
    print("Valor Inválido")