tentativas = 0
pin_correto = "4321"


while True:
    pin = input("Digite O Código PIN: ")
    tentativas += 1
    
    if pin == pin_correto:
        print(f"PIN Correto! Você Errou {tentativas} Vez(es) Antes De Acertar")
        
        






#INCOMPLETO