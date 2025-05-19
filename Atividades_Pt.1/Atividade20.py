n1 = int(input("Fala Um Numero Ai: "))
n2 = int(input("Fala Outro Numero Ai: "))

tipo = input("Qual Tipo De Operação Sera Usada(+,-,*,/): ")

if tipo == "+":
    soma = n1 + n2
    print(soma)


elif tipo == "-":
    subtracao = n1 - n2
    print(subtracao)


elif tipo == "*":
    multiplicacao = n1 *n2
    print(multiplicacao)
    
    
elif tipo == "/":
    divisao = n1 / n2
    print(divisao)


else:
    print("Nothing")