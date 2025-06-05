num = [8, -23, 6, -4, -31, 12, -78, -10, 5]
def soma_positivos(lista):
    soma = 0
    for num in lista:
        if num > 0:
            soma += num
    return soma
     
print(soma_positivos(num))  
    
    