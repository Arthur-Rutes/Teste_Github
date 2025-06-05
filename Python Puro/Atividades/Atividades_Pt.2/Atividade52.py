import random

segredo = random.randint(1,100)

while True:
    aleatorio = int(input("Número: "))
    
    if aleatorio > segredo:
        print("Número é maior que o segredo.")
        
    elif aleatorio < segredo:
        print("Número é menor que o segredo.")
        
    else:
        print("Você acertou o segredo")
        break
    