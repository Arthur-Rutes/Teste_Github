nota1 = int(input("Nota Do 1°Semestre "))
nota2 = int(input("Nota Do 2°Semestre "))

media = (nota1 + nota2) / 3

if media >= 7:
    print("Parabéns Você Foi Aprovado")
else:
    print("Putz Você Está Reprovado")