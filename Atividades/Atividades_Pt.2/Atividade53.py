import re

saldo = 500


while True:
    print(f"Seu saldo atual é R$ {saldo}")
    saque = int(input("Quanto você quer sacar: "))
    
    if saque % 10 != 0:
        print("O valor deve ser múltiplo de 10.")
    elif saque > saldo:
        print("Saldo insuficiente.")
    elif saque <= 0:
        print("Valor inválido")
    else:
        saldo -= saque
        print(f"Saque de R$ {saque} realizado com sucesso!")
        print(f"Saldo Restante: R$ {saldo}")