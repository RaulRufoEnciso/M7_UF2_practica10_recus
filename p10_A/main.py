import casos_totales
import muertes_totales
import muertes_por_mes
import matplotlib.pyplot as plt

def main():
    # Obtener los datos de casos totales por mes por país
    casos_totales_por_mes = casos_totales.mostrar_casos_totales_por_mes()

    # Generar la gráfica de líneas para cada país
    for pais, datos in casos_totales_por_mes.items():
        plt.plot(datos, marker='o', label=pais)

    plt.title("Casos totales por mes")
    plt.xlabel("Mes")
    plt.ylabel("Casos Totales")
    plt.legend()
    plt.show()

    # Obtener los datos de muertes totales por mes por ciudad
    muertes_totales_por_mes_ciudades = muertes_totales.mostrar_muertes_totales_por_mes_ciudades()

    # Generar la gráfica de líneas para cada ciudad
    for ciudad, datos in muertes_totales_por_mes_ciudades.items():
        plt.plot(datos, marker='o', label=ciudad)

    plt.title("Muertes totales por mes (ciudades)")
    plt.xlabel("Mes")
    plt.ylabel("Muertes Totales")
    plt.legend()
    plt.show()

    # Obtener los datos de muertes por mes por país
    muertes_por_mes_por_pais = muertes_por_mes.mostrar_muertes_por_mes_por_pais()

    # Generar la gráfica de líneas para cada país
    for pais, datos in muertes_por_mes_por_pais.items():
        plt.plot(datos, marker='o', label=pais)

    plt.title("Muertes por mes (países)")
    plt.xlabel("Mes")
    plt.ylabel("Muertes")
    plt.legend()
    plt.show()

# Llamar a la función main
main()
