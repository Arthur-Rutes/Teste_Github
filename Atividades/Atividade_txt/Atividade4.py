try:

    with open("atividades/arquivos/numeros.txt") as arquivo:
        i = 0
        for linha in arquivo:
            i += 1            
    print(f"O Arquivo Contém {i} Linha(s).")
except FileNotFoundError:
    print("Arquivo Solicitado Não Encontrado")
except Exception as e:
    print(f"Erro Inesperado: {e}")