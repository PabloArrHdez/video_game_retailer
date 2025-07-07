import pandas as pd
import numpy as np
import re
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import src.extraccion as ext
import src.transformacion as trs
import src.modelo as mdl

if __name__ == "__main__":
    df_video_games = pd.read_csv('Data/video_games_sales.csv')
    df_all_games = pd.read_csv('Data/all_video_games(cleaned).csv')
    df = pd.read_csv('Data/video_games_sales_completo.csv')

    ext.descripcioon(df_video_games)
    ext.descripcion(df)

    trs.limpieza (df_video_games)
    trs.transformacion (df_video_games_limpio)
    trs.resumen (df_video_games_limpio)
    trs.transformacion (df_video_games_limpio,df_all_games)
    trs.union (df_video_games_limpio, df_all_games_limpio)
    trs.transformacion (df_video_games_unido)
    trs.rellenar_valores_nulos(df_video_games_unido)
    trs.eliminacion_registros(platform_counts)
    trs.renombrar_registros(df_video_games_unido)
    trs.clasificar_consola(plataforma)
    trs.añadimos_columna(df_video_games_unido)
    trs.assign_launch_price(row)
    trs.añadir_columna(df_video_games_unido)
    trs.assign_launch_price_platform(row)
    trs.añadir_columna(df_video_games_unido)
    trs.imputar_user_score(df_video_games_unido,row)
    trs.añadir_columna(df_video_games_unido)
    trs.imputar_pegi(df_video_games_unido,row)
    trs.añadir_columna(df_video_games_unido)
    trs.añadir_columna(df_video_games_unido)
    trs.asignar_playtime(row)
    trs.clasificar_modo_juego(genero)
    trs.añadir_columna(df_video_games_unido)
    trs.calculo_año_lanzamiento (df_video_games_unido)
    trs.categorizar_pegi(nota)
    trs.añadir_columna(df_video_games_unido)
    trs.categorizar_duracion (df_video_games_unido)
    trs.extraer_nombre_base(nombre)
    trs.añadir_columna(df_video_games_unido)
    trs.añadir_columnas(df_video_games_unido)

    mdl.modelo (df)
    mdl.resultado (y_test, y_pred)