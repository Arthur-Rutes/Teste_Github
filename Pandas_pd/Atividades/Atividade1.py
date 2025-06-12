import pandas as pd

url_filmes = "netflix_titles.csv"

df_filmes = pd.read_csv(url_filmes)

print(f"7 Primeiras Linhas: {df_filmes.head(8)}")
print("")

print(df_filmes.info())
print("")

print(f"Linhas: {df_filmes.shape[0]} Colunas: {df_filmes.shape[1]}")
print("")

print(df_filmes.describe())