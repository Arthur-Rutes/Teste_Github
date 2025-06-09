import pandas as pd

# #Criando Uma Série
# idade = pd.Series([1,2,3,4,5,6])
# print(idade)
# print("")
# idades_nomes = pd.Series([1,2,3,4,5,6],index=['Ana','Jonas','Roger','Lucas','Zack','Ed'])
# print(idades_nomes)



#Dta Frames
# dados_alunos = {
#     'nome':['Ana','Jonas','Roger','Lucas','Zack','Ed'],
#     'idade':[1,2,8,7,4,15],
#     'curso':['Engenharia','Medicina','Psicologia','Direito','Biologia','Arquitetura']
    
# }

# df_alunos = pd.DataFrame(dados_alunos)
# print(df_alunos)

url_filmes = "IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
print(df_filmes)
print("")

# Head() E Tail().

# Head

print("Primeiras 5 Linhas Do DataFrame De Filmes:")
print(df_filmes.head())
print("")

# Tail.

print("Ultimas 5 Linhas Do DataFrame De Filmes:")
print(df_filmes.tail())
print("")

# Info.

print("\n Informções Sobre O DataFrame")
print(df_filmes.info())
print("")

print(f"O DataFrame De Filmes Tem {df_filmes.shape[0]} Linhas E {df_filmes.shape[1]} Colunas")
print("")

# Describe.
# Gera Estatistica Do Data Frame.

print("Estatistica Descritiva Do DataFrame:")
print(df_filmes.describe())
print("")

# Index
# Traz Informações Sobre Os Índices Das Linhas

print("Informações Do Índice")
print(df_filmes.index)
print