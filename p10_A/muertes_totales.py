import pandas as pd

def mostrar_muertes_totales_por_mes_ciudades():
    # Cargar el archivo CSV y seleccionar las columnas necesarias
    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'total_deaths'])

    # Seleccionar 10 ciudades
    ciudades = df['location'].unique()[:10]

    # Filtrar los datos para las 10 ciudades seleccionadas
    df_ciudades = df[df['location'].isin(ciudades)]

    # Convertir la columna 'date' a tipo datetime
    df_ciudades['date'] = pd.to_datetime(df_ciudades['date'])

    # Agrupar por ciudad y mes y sumar el número total de muertes
    df_agrupado = df_ciudades.groupby(['location', df_ciudades['date'].dt.year, df_ciudades['date'].dt.month]).sum()

    # Crear diccionario para almacenar los datos
    datos_por_ciudad = {}

    # Obtener los números totales de muertes por mes para cada ciudad
    for ciudad in ciudades:
        df_ciudad = df_agrupado.loc[ciudad]
        datos_por_ciudad[ciudad] = df_ciudad['total_deaths'].tolist()

    return datos_por_ciudad
