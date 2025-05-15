palavra = input("Escreva algo aí: ")

Penultimo = len(palavra) - 2

if palavra[Penultimo] == palavra[1]:
    print(f"O {palavra[Penultimo]} e {palavra[1]} são iguais.")

else:
    print(f"O {palavra[Penultimo]} e {palavra[1]} não são iguais.")