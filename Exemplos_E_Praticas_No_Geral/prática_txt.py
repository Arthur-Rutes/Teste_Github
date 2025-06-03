try:
    with open("atividades/arquivos/numeros.txt") as arquivo:
        maior = 0
        for linha in arquivo:
            numero = int(linha)
            if numero > maior:
                maior = numero
        print("Maior Número:", maior)

except FileNotFoundError:
    print("Arquivo Não Encontrado No .")
except ValueError:
    print("Erro: O Arquivo Contem Dados Que Não São Inteiros.")
    