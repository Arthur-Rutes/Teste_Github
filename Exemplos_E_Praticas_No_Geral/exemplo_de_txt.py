# try:
#     with open("atividades/arquivos/letra.txt") as novo_arquivo:
#         for linha in novo_arquivo:
#             print(linha)

# except FileNotFoundError:
#     print("Arquivo Inexistente.")

#----------------------------------#

# with open("atividades/arquivos/pessoas.csv") as novo_arquivo:
#     for linha in novo_arquivo:
#         linha = linha.replace("\n","")
#         partes = linha.split(";")
#         nome = partes[0]
#         notas = partes[1:]
#         print("Nome: ", nome)
#         print("Notas: ", notas)

#with open("teste.txt", "a") Adiciona Algo No Arquivo
#with open("teste.txt", "w") Faz Um Novo Arquivo Só Com As Informações Pedidas
#with open("teste2.txt", "x") Cria Um Novo Arquivo
# with open("atividades/arquivos/teste.txt", "w") as arquivo:
#     f = arquivo
#     f.write("Sem Lol Aqui")


