banco_filmes = []


def add_filme(database,nome,diretor,ano,duracao):
    filmes = {"nome":nome,"diretor":diretor,"ano":ano,"duracao":duracao}


    database.append(filmes)
    print(banco_filmes)

while True:
    escolha = input("Deseja adicionar mais filmes a lista ou parar por aqui(Sim Ou Não)? ")

    if escolha == "Sim":
       nome = input("Nome Do Filme: ")
       diretor = input("Nome Do Diretor(a): ")
       ano = int(input("Qual Ano O Filme Foi Lançado: "))
       duracao = int(input("Qual A Duração Total Do Filme(Min): "))
       add_filme(banco_filmes, nome, diretor, ano, duracao) 



    elif escolha == "Não":
        print("Ok Aqui Esta A Lista Completa:")
        print(banco_filmes)
        break


    else:
        print("Comando Invalido.")