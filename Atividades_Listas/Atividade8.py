import re
def cadastro_de_senhas():
    senhas = []
#Esse Daqui É O while De Repetição
    while len(senhas) < 5:
        criar = input("Cadastre Senhas (Max 5): ")
        

        if len(criar) >= 8:
            senhas.append(criar)
            print("Senha Criada Com Sucesso.")
        
        if re.search("[0-9]", criar) != None:
            senhas.append(criar)
            print("Senha Criada Com Sucesso.")
            
        else:
            print("Senha Inválida, A Senha Deve Conter Pelo Menos 8 Carácteres E 1 Número.")

print("Senhas Válidas")
# i = 0
# #Esse É O while Que Vai Contar O Número De Total De Senhas Erradas Ou Certas
# while i < len(senhas):
#     print(senhas[i])
#     i += 1
            
# cadastro_de_senhas()