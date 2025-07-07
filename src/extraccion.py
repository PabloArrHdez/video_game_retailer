import pandas as pd

df_video_games = pd.read_csv('Data/video_games_sales.csv')
df_all_games = pd.read_csv('Data/all_video_games(cleaned).csv')
df = pd.read_csv('Data/video_games_sales_completo.csv')

def descripcioon(df_video_games):
    print("Primeras filas del dataset")
    print(df_video_games.head(10))
    print("\nDimensiones del dataset:")
    print(f"Filas: {df_video_games.shape[0]}, Columnas: {df_video_games.shape[1]}")
    print("\nValores nulos por columna:")
    print(df_video_games.isnull().sum())

def descripcion(df):
    print(df['Ventas_Clase'].value_counts())
    print("Forma del dataframe combinado:", df.shape)
    print(df.isnull().sum())
    print(df.columns.unique())
    for clase in ['Normal', 'Alta', 'Muy Alta']:
        subset = df[df['Ventas_Clase'] == clase]
        minimo = subset['Global_Sales'].min()
        maximo = subset['Global_Sales'].max()
        print(f"{clase}: entre {minimo:.2f} y {maximo:.2f} millones de unidades vendidas.")