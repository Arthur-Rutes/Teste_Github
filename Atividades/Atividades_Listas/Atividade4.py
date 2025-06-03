notas = []
aprovadas = []
#Enquanto Tamanho Da Lista "notas" For Menor Que 5 Vai Repetir O While
while len(notas) < 5:
    #Input De Entrada Do Usúario
    nota = int(input("Qual A Nota: "))
    #Adiciona A Nota Do Input Na Lista "notas"
    notas.append(nota)
    #If Que Verifica Se A Nota É Maior Que 6
    if nota >= 6:
        #Adiciona A Nota A Uma Nova Lista Se A Nota For Maior Que 6
        aprovadas.append(nota)
#Ao Final Do Script, Ele Exibe As Notas Aprovadas Maior Que 6        
print(f"Notas Aprovadas: {aprovadas}")