import pandas as pd
try:
    url_filmes = "IMDB-Movie-Data.csv"
    df_filmes = pd.read_csv(url_filmes)
    df_filmes_completo = df_filmes.copy()
    df_filmes_preenchido_media = df_filmes.copy()
    #1
    print("Valores Ausentes Após Preenchimento: ")
    print(df_filmes[['Gross', 'Meta_score']].isna().sum())
    print("")
    #2
    df_filmes_completo = df_filmes.dropna()
    print(f"Número De Linhas Originais: {len(df_filmes)}")
    print("")
    print(f"Número De Linhas Após Remoção: {len(df_filmes_completo)}")
    print("")
    #3 | 'fillna' = Preencher Valores Inexistentes
    # Garantindo que as colunas estão numéricas
    df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
    df_filmes_completo['Gross'] = pd.to_numeric(df_filmes_completo['Gross'], errors='coerce')
    df_filmes_completo['Meta_score'] = pd.to_numeric(df_filmes_completo['Meta_score'], errors='coerce')
    print(df_filmes_completo['Gross'])
    # Criando uma cópia do DataFrame original
    df_filmes_preenchido_media = df_filmes_completo.copy()
    
    # Preenchendo os NaNs
    df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
    df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].mean())
    
    # Verificando se ainda existem NaNs nessas colunas
    print("\nValores ausentes após preenchimento:")
    print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())

except Exception as e:
    print(f"Erro: {e}")