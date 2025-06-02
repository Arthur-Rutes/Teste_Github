try:
    numero = int(input("Diga-nos Um Número: "))

except ValueError:
    print("Erro:'Número' Pedido Errado.")

finally:
    print("Número Válido.")
    
