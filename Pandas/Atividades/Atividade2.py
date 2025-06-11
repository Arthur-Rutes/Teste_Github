import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
#1

filmes_selecionados = df_filmes[["Series_Title","Director","Released_Year"]]
print(filmes_selecionados.head())
print("")
#2

infos_filmes = df_filmes.iloc[10:16, 0:4]
print(infos_filmes)
print("")
#3
# Cria Uma Cópia Do DataFrame Com A Coluna 'IMDB_Rating' Como Índice (Sem Alterar O Original).

df_temp = df_filmes.set_index('IMDB_Rating')
# Seleciona Os Filmes De Rank 1 A 5 E Mostra Apenas 'Title' E 'Revenue(Millions) Ou Gross Nesse Caso.'

print(df_temp[['Series_Title','Gross']].head())
print("")

#4
# Converter A Coluna 'Released_Year' Para Numérico, Caso Ainda Não Esteja.
df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce')


filmes_pos_2016 = df_filmes[df_filmes['Released_Year'] >= 2016][['Series_Title', 'Released_Year']]
print(filmes_pos_2016.head(15))