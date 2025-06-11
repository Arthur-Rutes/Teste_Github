import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
df_copy = df_filmes.copy()
#1 E 2
df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
df_filmes['Rating_Metascore_Diff'] = df_filmes['IMDB_Rating'] - (df_filmes['Meta_score'] / 10)
print(df_filmes[['Series_Title', 'IMDB_Rating', 'Meta_score', 'Rating_Metascore_Diff']].head())
#3 Pode Se Usar O 'columns'
df_copy = df_filmes.drop('Overview', axis=1)
print(df_copy.head())
#4 Renomeando Com Inplace=True.
df_filmes.rename(columns={'No_of_Votes': 'Numero_Votos'}, inplace=True)
print(df_filmes.columns.tolist())
