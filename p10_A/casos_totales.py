import pandas as pd

def mostrar_casos_totales_por_mes():
    # Cargar el archivo CSV y seleccionar las columnas necesarias
    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'total_cases'])

    # Seleccionar 10 países
    paises = df['location'].unique()[:10]

    # Filtrar los datos para los 10 países seleccionados
    df_paises = df[df['location'].isin(paises)]

    # Convertir la columna 'date' a tipo datetime
    df_paises['date'] = pd.to_datetime(df_paises['date'])

    # Agrupar por país y mes y sumar la cantidad total de casos
    df_agrupado = df_paises.groupby(['location', df_paises['date'].dt.year, df_paises['date'].dt.month]).sum()

    # Mostrar la cantidad total de casos por mes para cada país
    for pais in paises:
        df_pais = df_agrupado.loc[pais]
        print(f"País: {pais}")
        print(df_pais)

# Llamar a la función para mostrar la cantidad total de casos por mes para los 10 países
mostrar_casos_totales_por_mes()
