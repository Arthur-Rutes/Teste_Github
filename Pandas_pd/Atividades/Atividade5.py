import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
try:
    df_filmes = df_filmes.drop('Poster_Link', axis=1)
    
    #1
    contagem_directors = df_filmes['Director'].value_counts()
    print(f"Os 5 Maiores Diretores Da Lista Inteira {contagem_directors.head(5)}")
    print("")
    #2
    df_filmes['Runtime'] = df_filmes['Runtime'].str.replace('min','')
    df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'], errors='coerce')
    ordem_duracao = df_filmes.sort_values(by=['Runtime'], ascending=False)
    print(f"Top 10 Filmes Mais Longos Do IMDB:\n{ordem_duracao.head(10)}")
    print("")
    #3
    df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
    meta_certificate = df_filmes.sort_values(by=['Certificate','Meta_score'],ascending=[True,False])
    print(f"Top 5 Filmes Certificados Por Meta_score:\n{meta_certificate.head(5)}")
    print("")
except Exception as err:
    print(f"Erro Detectado: {err}")