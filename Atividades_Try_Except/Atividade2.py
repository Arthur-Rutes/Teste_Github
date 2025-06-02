try:
    num_str = input("Digite Um Número: ")
    num_int = int (num_str)
    resultado = 10000 / num_int
    print(f"10000 Dividido Por {num_int} É {resultado}")

except ValueError:
    print("Erro: Entrada Invalida. Por Favor, Digite Um Numero.")

except ZeroDivisionError:
    print("Erro: Não É Possível Dividir Por Zero.")

#Else Só Vai Ser Executado Se Não Houver Nenhum Erro Na Execução.
else:
    print("Deu Tudo Certo.")

#Executa Mesmo Se Houver Um Erro Ou Não No Try.
finally:
    if num_int == 0:
        num_str = input("Digite Um Número: ")
        