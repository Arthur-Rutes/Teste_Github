capital = float(input("Quanto Você Quer Investir: "))
taxa = int(input("Quais São As Taxas De Juros Anuais? "))
tempo = int(input("Quanto Tempo Passara Investindo? "))
juros = capital * (taxa / 100) * tempo
montante = capital + juros
print(f"Com O Capital De: {capital}, A Taxa De {taxa}, Ao Fim De {tempo} Ano(s), Você Terá Á Juros Simples: {montante}")