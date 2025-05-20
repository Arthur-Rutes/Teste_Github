def linha (n, texto):
    if texto == "":
        caracteres = "*"
    else:
        caracteres = texto[0]
        
    print(caracteres * n)
    
def caixa_de_hashtags(altura):
    contador = 0
    while contador < altura:
        linha(10, "#")
        contador += 1

caixa_de_hashtags(100)