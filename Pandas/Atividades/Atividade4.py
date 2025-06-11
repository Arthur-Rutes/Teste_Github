import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
df_filmes_completo = df_filmes.copy()
df_filmes_preenchido_media = df_filmes.copy()
#1
print(df_filmes.isna().sum())
print("")
#2
df_filmes_completo.dropna(inplace=True)
print(f"Número De Linhas Originais: {len(df_filmes)}")
print("")
print(f"Número De Linhas Após Drop: {len(df_filmes_completo)}")
print("")
#3
