import re

while True:
    p1 = input("Digite uma palavra: ")
    p2 = input("Digite outra palavra: ")

    if len(p1) != len(p2):
        print("Suas palavras não contém a mesma quantidade letra")
        
    else:
        print("As duas palavras teem a mesma quantidade de letra")
        break