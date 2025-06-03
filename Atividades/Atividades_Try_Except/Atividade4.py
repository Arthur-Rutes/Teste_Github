arquivo = None

try:
    arquivo = open("random.txt", "r")
    conteudo = arquivo.read()
    print("Arquivo Lido Com Sucesso.")


except FileNotFoundError:
    print("Arquivo Não Encontrado.")

finally:
    if arquivo:
        arquivo.close()
        print("Arquivo Fechado.")
