aleatorio = input("Escreva qualquer palavra: ")

largura_total = 30

linha_borda = "*" * largura_total

espacos_total = largura_total - len(aleatorio)

espacos_esquerda = espacos_total // 2

espacos_direita = espacos_total - espacos_esquerda - 2


if len(aleatorio) % 2 == 0:
    linha_central = "*" + " " * espacos_esquerda + aleatorio + " " * espacos_direita + "*"

else:
    linha_central = "*" + aleatorio + "*"
    
print(linha_borda)
print(linha_central)
print(linha_borda)