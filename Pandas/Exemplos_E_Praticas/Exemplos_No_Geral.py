import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)

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


# print(df_filmes)
# print("")

# # Head() E Tail().

# # Head

# print("Primeiras 5 Linhas Do DataFrame De Filmes:")
# print(df_filmes.head())
# print("")

# # Tail.

# print("Ultimas 5 Linhas Do DataFrame De Filmes:")
# print(df_filmes.tail())
# print("")

# # Info.

# print("\n Informções Sobre O DataFrame")
# print(df_filmes.info())
# print("")

# print(f"O DataFrame De Filmes Tem {df_filmes.shape[0]} Linhas E {df_filmes.shape[1]} Colunas")
# print("")

# # Describe.
# # Gera Estatistica Do Data Frame.

# print("Estatistica Descritiva Do DataFrame:")
# print(df_filmes.describe())
# print("")

# # Index.
# # Traz Informações Sobre Os Índices Das Linhas.

# print("Informações Do Índice")
# print(df_filmes.index)


# Selecionando A Coluna 'Title'.

# filmes_selecionados = df_filmes[["Series_Title","Genre","IMDB_Rating"]]
# print(f"\nDataFrame Com Titulo, Gênero E Nota.")
# print(filmes_selecionados.head())
# print("")

# Selecionando A Primeira Linha.
# Iloc É Usado Para Selecionar Linhas Por Indice Numérico.

# primeiro_filme = df_filmes.iloc[0]
# print("\nPrimeiro Filme (Linha Completa): ")
# print(primeiro_filme)
# print("")

# Selecionando As 3 Primeiras Linhas.

# tres_primeiros = df_filmes.iloc[0:3]
# print("\n3 Primeiros Filme (Linhas Completa): ")
# print(tres_primeiros)
# print("")

# Selecionando Linhas E Colunas Especificas.
# selecao_especifica = df_filmes.iloc[[0,5],[1,4]]
# print("\nPrintando Uma Seleção Específica, Linha 0 E 5 E Coluna 1 E 4.")
# print(selecao_especifica)
# print("")

# Selecionando Dados Com .index.
# Localiza Os Dados Pelos Rótulos.

# df_filmes_idx = df_filmes.set_index("Series_Title")
# print("\nDefinimos O Indice Agora Como Series Titles")
# print(df_filmes_idx.head())
# print("")

# poderoso = df_filmes_idx.loc["The Godfather"]
# print("\nDados Do Filme: The Godfather: ")
# print(poderoso)
# print("")

# Filtrar Os Dados Baseados Em Condições (Boolean Indexing)

# df_filmes_bem_avaliados = df_filmes[df_filmes["IMDB_Rating"] >= 9]
# print("\nFilmes Com Nota >= 9 (Primeiras Linhas)")
# print(df_filmes_bem_avaliados["Series_Title"].head())

# Filmes Que Tem Gênero 'Action'

# filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)]
# print("\nFilmes Que Contem O Genero 'Action'")
# print(filmes_acao[['Series_Title','Genre']].head())