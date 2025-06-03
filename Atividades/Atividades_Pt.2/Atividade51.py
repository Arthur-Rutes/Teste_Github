import re

while True:
    senha = input("Escreva uma senha: ")
    TotalCaracter = int(len(senha))
    validacao1 = (re.search("[A-Z]", senha))
    validacao2 = (re.search("[a-z]", senha))
    validacao3 = (re.search("[0-9]", senha))
    
    if TotalCaracter < 8:
        print("A senha terá que ter pelo menos 8 caractéres")

    
    elif validacao1 == None:
        print("A senha tem que conter pelo menos uma letra maiuscula.")

        
    elif validacao2 == None:
        print("A senha tem que conter pelo menos uma letra minúscula.")
 

    elif validacao3 == None:
        print("A senha tem que conter pelo menos um número.")

    
    else:
        print("Senha criada com sucesso.")
        break