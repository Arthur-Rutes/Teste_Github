num = [18, 85, 2016]

try:
    divisor = int(input("Qual Vai Ser O Divisor: "))
    print(num)
    numero = int(input("Qual Número: "))
    divisao = num[numero] / divisor

except ZeroDivisionError:
    print("Erro: Nada É Divísivel Por Zero.")

except IndexError:
    print("Erro: Indice Inexistente.")

except Exception as e:
    print(f"Erro: {e}")

else:
    print(f"{num[numero]} Dividido Por {divisor} É {divisao}")