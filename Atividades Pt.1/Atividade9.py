conta = int(input("Qual O Valor Da Sua Conta: "))

gorjeta = int(input("Quanto Sera A Gorjeta(%): "))


totalGorjeta = (conta * gorjeta) / 100

totalConta = conta + totalGorjeta

print(f"Gorjeta: {totalGorjeta}, Conta Total: {totalConta}")