import pandas as pd

def mostrar_muertes_por_mes_por_pais():
    # Cargar el archivo CSV y seleccionar las columnas necesarias
    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'new_deaths'])

    # Seleccionar 10 países
    paises = df['location'].unique()[:10]

    # Filtrar los datos para los 10 países seleccionados
    df_paises = df[df['location'].isin(paises)]

    # Convertir la columna 'date' a tipo datetime
    df_paises['date'] = pd.to_datetime(df_paises['date'])

    # Agrupar por país y mes y sumar el número de muertes
    df_agrupado = df_paises.groupby(['location', df_paises['date'].dt.year, df_paises['date'].dt.month]).sum()

    # Crear diccionario para almacenar los datos
    datos_por_pais = {}

    # Obtener el número de muertes por mes por país
    for pais in paises:
        df_pais = df_agrupado.loc[pais]
        datos_por_pais[pais] = df_pais['new_deaths'].tolist()

    return datos_por_pais

