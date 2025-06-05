#Funciona
numeros = []

while True:
    sla = int(input(f"Digite O {len(numeros)+1}° Numero: "))
    numeros.append(sla)
    
    if len(numeros) > 5:
        break