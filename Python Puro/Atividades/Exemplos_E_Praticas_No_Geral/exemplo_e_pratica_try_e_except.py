# try:
#     num_str = input("Digite Um Número: ")
#     num_int = int (num_str)
#     resultado = 10 / num_int
#     print(f"10 Dividido Por {num_int} É {resultado}")

# except ValueError:
#     print("Erro: Entrada Invalida. Por Favor, Digite Um Numero.")

# except ZeroDivisionError:
#     print("Erro: Não É Possível Dividir Por Zero.")

# except Exception as e:
#     print(f"Ocorreu Um Erro Inesperado {e}")

# #Else Só Vai Ser Executado Se Não Houver Nenhum Erro Na Execução.
# else:
#     print("Deu Tudo Certo.")

# #Executa Mesmo Se Houver Um Erro Ou Não No Try.
# finally:
#     if num_int == 0:
#         num_str = input("Digite Um Número: ")

#||---------------------------------------------||#

arquivo = None


try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print("Arquivo Lido Com Sucesso.")

except FileNotFoundError:
    print("Erro Arquivo Não Encontrado.")

except Exception as e:
    print(f"Erro Ao Ler O Arquivo {e}.")
    
else:
    print("Processamento Do Arquivo Concluido Com Sucesso.")

finally:
    if arquivo:
        arquivo.close()
        print("Arquivo Fechado")