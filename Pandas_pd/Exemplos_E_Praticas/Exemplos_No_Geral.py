import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
try:
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

    # Filmes Que Tem Gênero 'Action'.

    # filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)]
    # print("\nFilmes Que Contem O Genero 'Action'")
    # print(filmes_acao[['Series_Title','Genre']].head())


    # Criar Uma Nova Coluna.
    # df_filmes['Rating_x_10'] = df_filmes['IMDB_Rating'] * 10
    # print("O Dataframe Agora Tem Uma Nova Coluna: ")
    # print(df_filmes.head())
    # print("")

    # Conversão Da Coluna Gross Para Float E Ignorando Erros Caso Falhar.
    # df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')


    # Agora, Convertido O Numero Gross Em Numero, É Mais Seguro Fazer A Comparação.
    # df_filmes['Alta_Receita'] = df_filmes['Gross'] > 1000
    # print("DataFrame Com Nova Coluna 'Alta_Receita' (Primeiras Linhas)")
    # print(df_filmes.head())
    # print("")

    # Drop.
    # Método Drop Remove Uma Linha (Registro) Ou Coluna.
    # axis = 1 | Exclui A Coluna.
    # df_filmes = df_filmes.drop('Poster_Link', axis=1)
    # print(df_filmes.head())
    # print("")

    # axis = 0 | Excluí O Registro
    # df_filmes = df_filmes.drop(4,axis=0)
    # print(df_filmes.head())
    # print("")

    # Lidando Com Dados Ausentes.
    # Verificar Dados Ausentes Com .isna() .sum()

    # print("Contagem De Valores Ausentes Por Coluna: ")
    # print(df_filmes.isna().sum())
    # print("")

    # Removendo Linhas/Colunas.
    # Criando Uma Cópia Para Não Modificar O Arquivo Original.

    # df_sem_nan_linhas = df_filmes.copy()

    # Removendo Todas As Linhas Que Contenham Qualquer Valor 'nan' (nan = Not A Number).
    # df_sem_nan_linhas.dropna(inplace=True)
    # print(f"Número De Linhas Originais: {len(df_filmes)}")
    # print("")
    # print(f"Número De Linhas Após Drop: {len(df_sem_nan_linhas)}")
    # print("")

    # Removendo Colunas Que Tenham Qualquer Registro 'nan'
    # df_sem_nan_colunas = df_filmes.dropna(axis=1)
    # print(f"Colunas Originais: {df_filmes.columns.tolist()}")
    # print("")
    # print(f"Colunas Após Dropna: {df_sem_nan_colunas.columns.tolist()}")

    # Contando As Frequencias De Colunas.
    # contagem_diretores = df_filmes['Director'].value_counts()
    # print("")
    # print("Os 10 Diretores Mais Frequentes: ")
    # print(contagem_diretores.head(15))
    # print("")
    # Ordenando Filmes Pela Nota (IMDB_Rating)
    # df_ordem_nota = df_filmes.sort_values(by='IMDB_Rating',ascending=False)
    # print("Top 5 Filmes Por Nota (IMDB_Rating): ")
    # print(df_ordem_nota)
    # print("")
    # Anscending 'False' = Decrescente | Ascending 'True' = Crescente.
    df_ordenado_duas_col = df_filmes.sort_values(by=['Released_Year','Gross'],ascending=[False,True])
    print("Top 5 Filmes Por Ano E Gross:")
    print(df_ordenado_duas_col.head())
    print("")
    
    df_filmes['Gross'] = df_filmes['Gross'].str.replace(',','')
    df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
    df_filmes['IMDB_Rating'] = pd.to_numeric(df_filmes['IMDB_Rating'], errors='coerce')
    
    # Calculando A Média De 'IMDB' E 'GROSS' Para Cada 'Released_Year'.
    metricas_por_ano = df_filmes.groupby('Released_Year').agg(
        Media_Rating = ('IMDB_Rating','mean'),
        Media_Receita = ('Gross','mean'),
        Total_Filmes = ('Series_Title','count'),
    )
    print(metricas_por_ano)
    print("")
    # Salvando Em Um Arquivo CSV Sem O Indice.
    df_filmes.to_csv('filmes_mais_legais_do_site.csv', index=False)
    print("DataFrame Salvo Em 'filmes_mais_legais_do_site.csv'")
    
    
except Exception as e:
    print(f"Erro:{e}")