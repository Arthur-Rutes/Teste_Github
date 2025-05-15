p1 = (input("Quem É A 1°Pessoa? "))
p2 = (input("Quem É A 2°Pessoa? "))
i1 = int(input("Qual A Idade Da 1°Pessoa? "))
i2 = int(input("Qual A Idade Da 2°Pessoa? "))

if i1 > i2:
    print(f"O(A) {p1} É Mais Velho Do Que O(A) {p2}")
elif i2 > i1:
    print(f"O(A) {p2} É Mais Velho Do Que O(A) {p1}")
else:
    print("Ambos Tem A Mesma Idade")