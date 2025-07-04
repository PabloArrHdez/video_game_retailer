import pandas as pd
import numpy as np
import re

df_video_games = pd.read_csv('Data/video_games_sales.csv')
df_all_games = pd.read_csv('Data/all_video_games(cleaned).csv')


def limpieza (df_video_games):
    df_video_games1 = df_video_games.drop_duplicates()
    df_video_games2 = df_video_games1.dropna(subset=['Year', 'Publisher'])
    df_video_games_limpio = df_video_games2[df_video_games2['Global_Sales'] > 0] # & df_video_games2['Global_Sales'] < 40
    df_video_games_limpio['Year'] = df_video_games_limpio['Year'].astype(int)
    return df_video_games_limpio.to_csv('Data/video_games_sales_limpio.csv', index=False)

def transformacion (df_video_games_limpio):
    q90 = df_video_games_limpio['Global_Sales'].quantile(0.90)
    q60 = df_video_games_limpio['Global_Sales'].quantile(0.60)
    def clasificar_ventas(ventas):
        if ventas >= q90:
            return 'Muy Alta'
        elif ventas >= q60:
            return 'Alta'
        else:
            return 'Normal'
    df_video_games_limpio['Ventas_Clase'] = df_video_games_limpio['Global_Sales'].apply(clasificar_ventas)

def resumen (df_video_games_limpio):
    print(f"Filas: {df_video_games_limpio.shape[0]}, Columnas: {df_video_games_limpio.shape[1]}")
    print(df_video_games_limpio.dtypes)
    return df_video_games_limpio.to_csv('Data/video_games_sales_limpio.csv', index=False)

def transformacion (df_video_games_limpio,df_all_games):
    df_video_games_limpio['Title'] = df_video_games_limpio['Name'].str.strip().str.lower()
    df_all_games['Title'] = df_all_games['Title'].str.strip().str.lower()
    df_all_games_limpio = df_all_games[['Title', 'Product Rating', 'User Score', 'User Ratings Count', 'Platforms Info']]
    return df_all_games_limpio

def union (df_video_games_limpio, df_all_games_limpio):
    df_video_games_unido = pd.merge(df_video_games_limpio, df_all_games_limpio, on='Title', how='left')
    return df_video_games_unido

def transformacion (df_video_games_unido):
    df_video_games_unido.drop(columns=['Rank','Title', 'Platforms Info'], inplace=True)
    return df_video_games_unido

def rellenar_valores_nulos(df_video_games_unido):
    df_video_games_unido['User Ratings Count'] = (
        df_video_games_unido.groupby(['Platform', 'Genre'])['User Ratings Count']
            .transform(lambda x: x.fillna(x.median())))
    df_video_games_unido['User Ratings Count'] = df_video_games_unido['User Ratings Count'] \
        .fillna(df_video_games_unido['User Ratings Count'].median())
    df_video_games_unido['User Ratings Count'] = df_video_games_unido['User Ratings Count'].round().astype(int)
    return df_video_games_unido

def eliminacion_registros(platform_counts):
    platform_counts = df_video_games_unido['Platform'].value_counts()
    platforms_to_remove = platform_counts[platform_counts < 20].index.tolist()
    df_video_games_unido = df_video_games_unido[~df_video_games_unido['Platform'].isin(platforms_to_remove)].copy()
    return df_video_games_unido

def renombrar_registros(df_video_games_unido):
    platform_rename = {
    '2600': 'Atari 2600',
    'DS': 'Nintendo DS',
    'GB': 'Game Boy',
    'GBA': 'Game Boy Advance',
    'GC': 'GameCube',
    'GEN': 'Sega Genesis',
    'N64': 'Nintendo 64',
    'NES': 'Nintendo Entertainment System',
    'PC': 'PC',
    'PS': 'PlayStation',
    'PS2': 'PlayStation 2',
    'PS3': 'PlayStation 3',
    'PS4': 'PlayStation 4',
    'PSP': 'PlayStation Portable',
    'PSV': 'PlayStation Vita',
    'SAT': 'Sega Saturn',
    'SNES': 'Super Nintendo Entertainment System',
    'Wii': 'Nintendo Wii',
    'WiiU': 'Nintendo Wii U',
    'X360': 'Xbox 360',
    'XB': 'Xbox',
    'XOne': 'Xbox One',
    'DC': 'Dream Cast',
    '3DS': 'Nintendo 3DS',
    }
    df_video_games_unido['Platform'] = df_video_games_unido['Platform'].replace(platform_rename)
    df_video_games_unido.rename(columns={'Product Rating': 'Nota PEGI'}, inplace=True)
    df_video_games_unido = df_video_games_unido[df_video_games_unido['Nota PEGI'] != 'Rated RP For Rate Pending'].copy()
    nota_pegi_rename = {
    'Rated E For Everyone': '3',
    'Rated M For Mature': '18',
    'Rated T For Teen': '16',
    'Rated E +10 For Everyone +10': '12',
}
    df_video_games_unido['Nota PEGI'] = df_video_games_unido['Nota PEGI'].replace(nota_pegi_rename)
    return df_video_games_unido

def clasificar_consola(plataforma):
    mercado_activo = [
    'PlayStation 4','PC', 
    'Xbox One']
    mercado_secundario = [
    'Nintendo 3DS',
    'PlayStation Vita']
    if plataforma in mercado_activo:
        return 'Consola Activa'
    elif plataforma in mercado_secundario:
        return 'Consola Secundaria'
    else:
        return 'Consola Obsoleta'
    
def añadimos_columna(df_video_games_unido):
    df_video_games_unido['Estado_Consola'] = df_video_games_unido['Platform'].apply(clasificar_consola)
    return df_video_games_unido


def assign_launch_price(row):
    platform_prices_eur = {
    'PlayStation 4': 69.99,
    'Xbox One': 69.99,
    'PC': 49.99,
    'PlayStation 3': 59.99,
    'Xbox 360': 59.99,
    'Nintendo Wii U': 59.99,
    'Nintendo Wii': 49.99,
    'Nintendo DS': 39.99,
    'Nintendo 3DS': 39.99,
    'PlayStation 2': 49.99,
    'PlayStation Portable': 39.99,
    'Nintendo Entertainment System': 49.99,
    'Super Nintendo Entertainment System': 59.99,
    'Game Boy': 39.99,
    'PlayStation': 49.99,
    'Game Boy Advance': 39.99,
    'Nintendo 64': 59.99,
    'Xbox': 59.99,
    'Atari 2600': 29.99,
    'GameCube': 49.99,
    'Sega Genesis': 49.99,
    'Dream Cast': 49.99,
    'PlayStation Vita': 49.99,
    'Sega Saturn': 59.99,
    }
    platform = row['Platform']
    return platform_prices_eur.get(platform)

def añadir_columna(df_video_games_unido):
    df_video_games_unido['Price'] = df_video_games_unido.apply(assign_launch_price, axis=1)
    return df_video_games_unido

def assign_launch_price_platform(row):
    price_dict = {
    'Nintendo Wii': 249,
    'Nintendo Entertainment System': 199,  
    'Game Boy': 113.5,
    'Nintendo DS': 149,
    'Xbox 360': 299,
    'PlayStation 3': 599,
    'PlayStation 2': 399,
    'Super Nintendo Entertainment System': 299,
    'Game Boy Advance': 120,
    'Nintendo 3DS': 250,
    'PlayStation 4': 399,
    'Nintendo 64': 210,
    'PlayStation': 299,
    'Xbox': 299,
    'PC': 230,
    'Atari 2600': 199,
    'PlayStation Portable': 249,
    'Xbox One': 499,
    'GameCube': 199,
    'Nintendo Wii U': 299, 
    'Sega Genesis': 199,
    'Dream Cast': 240,
    'PlayStation Vita': 249,
    'Sega Saturn': 399
}
    platform = row['Platform']
    return price_dict.get(platform)

def añadir_columna(df_video_games_unido):
    df_video_games_unido['Price_Platform'] = df_video_games_unido.apply(assign_launch_price_platform, axis=1)
    return df_video_games_unido

def imputar_user_score(df_video_games_unido,row):
    if pd.isna(row['User Score']):
        media = df_video_games_unido[
            (df_video_games_unido['Platform'] == row['Platform']) &
            (df_video_games_unido['Genre'] == row['Genre'])
        ]['User Score'].mean()
        return media
    else:
        return row['User Score']

def añadir_columna(df_video_games_unido):
    df_video_games_unido['User Score'] = df_video_games_unido.apply(imputar_user_score, axis=1)
    df_video_games_unido['User Score'].fillna(df_video_games_unido['User Score'].mean(), inplace=True)
    return df_video_games_unido

def imputar_pegi(df_video_games_unido,row):
    if pd.isna(row['Nota PEGI']):
        subset = df_video_games_unido[
            (df_video_games_unido['Platform'] == row['Platform']) &
            (df_video_games_unido['Genre'] == row['Genre'])
        ]['Nota PEGI']
        moda = subset.mode()
        return moda[0] if not moda.empty else np.nan
    else:
        return row['Nota PEGI']
    
def añadir_columna(df_video_games_unido):
    df_video_games_unido['Nota PEGI'] = df_video_games_unido.apply(imputar_pegi, axis=1)
    df_video_games_unido['Nota PEGI'].fillna(df_video_games_unido['Nota PEGI'].mode()[0],inplace=True)
    return df_video_games_unido

def añadir_columna(df_video_games_unido):
    year_lanzamiento = {
    'Atari 2600': 1977, 'Nintendo DS': 2004, 'Game Boy Advance': 2001,
    'GameCube': 2001, 'Sega Genesis': 1988, 'Nintendo 64': 1996, 'Nintendo Entertainment System': 1983, 'PC': 1980,
    'PlayStation': 1994, 'PlayStation 2': 2000, 'PlayStation 3': 2006, 'PlayStation 4': 2013, 'PlayStation Portable': 2004, 
    'PlayStation Vita': 2011, 'Sega Saturn': 1994, 'Super Nintendo Entertainment System': 1990,
    'Nintendo Wii': 2006, 'Nintendo Wii U': 2012, 'Xbox 360': 2005, 'Xbox': 2001, 'Xbox One': 2013,
    'Game Boy': 1989, 'Dream Cast': 1998, 'Nintendo 3DS': 2011
}
    df_video_games_unido['Year_Consola'] = df_video_games_unido['Platform'].map(year_lanzamiento)
    return df_video_games_unido

def asignar_playtime(row):
    playtime_dict = {
    ('Action', 'Nintendo Wii'): 10,
    ('Adventure', 'Nintendo Wii'): 20,
    ('Fighting', 'Nintendo Wii'): 4,
    ('Misc', 'Nintendo Wii'): 2,
    ('Platform', 'Nintendo Wii'): 10,
    ('Puzzle', 'Nintendo Wii'): 5,
    ('Racing', 'Nintendo Wii'): 6,
    ('Role-Playing', 'Nintendo Wii'): 40,
    ('Shooter', 'Nintendo Wii'): 8,
    ('Simulation', 'Nintendo Wii'): 20,
    ('Sports', 'Nintendo Wii'): 1,
    ('Strategy', 'Nintendo Wii'): 40,
    ('Action', 'Nintendo Entertainment System'): 2,
    ('Adventure', 'Nintendo Entertainment System'): 4,
    ('Platform', 'Nintendo Entertainment System'): 3,
    ('Puzzle', 'Nintendo Entertainment System'): 3,
    ('Racing', 'Nintendo Entertainment System'): 1,
    ('Role-Playing', 'Nintendo Entertainment System'): 18,
    ('Shooter', 'Nintendo Entertainment System'): 1,
    ('Sports', 'Nintendo Entertainment System'): 1,
    ('Strategy', 'Nintendo Entertainment System'): 10,
    ('Misc', 'Nintendo Entertainment System'): 1,
    ('Action', 'Game Boy'): 1,
    ('Adventure', 'Game Boy'): 15,
    ('Platform', 'Game Boy'): 1.5,
    ('Racing', 'Game Boy'): 1,
    ('Role-Playing', 'Game Boy'): 20,
    ('Action', 'Nintendo DS'): 7,
    ('Adventure', 'Nintendo DS'): 15,
    ('Fighting', 'Nintendo DS'): 2,
    ('Misc', 'Nintendo DS'): 3,
    ('Platform', 'Nintendo DS'): 6,
    ('Puzzle', 'Nintendo DS'): 10,
    ('Racing', 'Nintendo DS'): 5,
    ('Role-Playing', 'Nintendo DS'): 25,
    ('Shooter', 'Nintendo DS'): 6,
    ('Simulation', 'Nintendo DS'): 5,
    ('Sports', 'Nintendo DS'): 2,
    ('Strategy', 'Nintendo DS'): 18,
    ('Action', 'PlayStation 2'): 15,
    ('Action', 'PlayStation 3'): 12,
    ('Action', 'Nintendo Wii U'): 15,
    ('Adventure', 'Nintendo Wii U'): 37,
    ('Fighting', 'Nintendo Wii U'): 2,
    ('Misc', 'Nintendo Wii U'): 3,
    ('Platform', 'Nintendo Wii U'): 9,
    ('Puzzle', 'nintendo Wii U'): 6,
    ('Racing', 'Nintendo Wii U'): 6,
    ('Role-Playing', 'Nintendo Wii U'): 70,
    ('Shooter', 'Nintendo Wii U'): 6,
    ('Sports', 'Nintendo Wii U'): 1,
    ('Strategy', 'Nintendo wii U'): 8,
    ('Fighting', 'PC'): 3,
    ('Platform', 'PC'): 5,
    ('Puzzle', 'PlayStation 4'): 5,
    ('Racing', 'PlayStation 4'): 6,
    ('Role-Playing', 'PlayStation 4'): 50,
    ('Shooter', 'PlayStation 4'): 8,
    ('Simulation', 'PlayStation 4'): 20,
    ('Sports', 'PlayStation 4'): 1,
    ('Strategy', 'PlayStation 4'): 40,
    ('Action', 'Xbox One'): 15,
    ('Adventure', 'Xbox One'): 37,
    ('Fighting', 'Xbox One'): 2,
    ('Misc', 'Xbox One'): 3,
    ('Platform', 'Xbox One'): 9,
    ('Puzzle', 'Xbox One'): 6,
    ('Racing', 'Xbox One'): 6,
    ('Role-Playing', 'Xbox One'): 70,
    ('Shooter', 'Xbox One'): 6,
    ('Sports', 'Xbox One'): 1,
    ('Strategy', 'Xbox One'): 8
    }
    genre = str(row['Genre']).strip()
    platform = str(row['Platform']).strip()
    return playtime_dict.get((genre, platform), np.nan)

def clasificar_modo_juego(genero):
    multijugador_comun = {
    'Sports': True,
    'Platform': False,
    'Racing': True,
    'Role-Playing': False,
    'Puzzle': False,
    'Misc': True,
    'Shooter': True,
    'Simulation': False,
    'Action': True,
    'Fighting': True,
    'Adventure': False,
    'Strategy': True
    }
    if multijugador_comun.get(genero, True):
        return 'Multijugador'
    else:
        return 'Individual'
def añadir_columna(df_video_games_unido):
    df_video_games_unido['Modo Juego'] = df_video_games_unido['Genre'].apply(clasificar_modo_juego)
    return df_video_games_unido

def calculo_año_lanzamiento (df_video_games_unido):
    df_video_games_unido['Años_desde_lanzamiento_consola'] = df_video_games_unido['Year'] - df_video_games_unido['Year_Consola']
    df_video_games_unido['Precio_relativo'] = df_video_games_unido['Price'] / df_video_games_unido['Price_Platform']
    return df_video_games_unido

def categorizar_pegi(nota):
    if nota <= 7: return 'Infantil'
    elif nota < 16: return 'Adolescente'
    else: return 'Adulto'

def añadir_columna(df_video_games_unido):
    df_video_games_unido['PEGI_categoria'] = df_video_games_unido['Nota PEGI'].apply(categorizar_pegi)
    return df_video_games_unido

def categorizar_duracion (df_video_games_unido):
    df_video_games_unido['Duracion_juego_cat'] = pd.cut(df_video_games_unido['Play Time'], bins=[0, 5, 20, float('inf')], 
                                  labels=['Corto', 'Medio', 'Largo'])
    return df_video_games_unido

def extraer_nombre_base(nombre):
    nombre = nombre.lower()
    nombre = re.sub(r'\(.*?\)|\[.*?\]', '', nombre)  # eliminar paréntesis
    nombre = re.sub(r'[-_:]', ' ', nombre)  # quitar guiones y dos puntos
    nombre = re.sub(r'\b(remaster(ed)?|hd|ultimate|edition|goty|game of the year|definitive|complete|deluxe)\b', '', nombre)
    nombre = re.sub(r'\b([ivx]+|\d{1,2})\b', '', nombre)  # quitar romanos y números
    nombre = re.sub(r'[^a-zA-Z\s]', '', nombre)  # eliminar símbolos
    nombre = re.sub(r'\s+', ' ', nombre).strip()
    return nombre

def añadir_columna(df_video_games_unido):
    df_video_games_unido['Nombre_Base'] = df_video_games_unido['Name'].apply(extraer_nombre_base)
    conteo = df_video_games_unido['Nombre_Base'].value_counts()
    df_video_games_unido['Es_Saga'] = df_video_games_unido['Nombre_Base'].apply(lambda x: 1 if conteo.get(x, 0) > 1 else 0)
    df_video_games_unido['Tipo_Saga'] = df_video_games_unido['Es_Saga'].apply(lambda x: 'Saga' if x == 1 else 'No saga')
    return df_video_games_unido

def añadir_columnas(df_video_games_unido):
    recesion = {
    1980, 1981, 1982, 1983, 1991, 1992, 2001,
    2008, 2009, 2020
    }
    df_video_games_unido['Situacion_Economica'] = df_video_games_unido['Year'].apply(
    lambda x: 'Recesion' if x in recesion else 'Crecimiento'
    )
    return df_video_games_unido