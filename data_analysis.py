import matplotlib.pyplot as plt
from data_processing import load_ftd_data, load_cpa_data

# Análisis y visualización de los datos
def analyze_and_plot():
    # Cargar los datos FTD y CPA
    ftd_data = load_ftd_data()
    cpa_data = load_cpa_data()

    # Graficar la cantidad de FTD por mes
    plt.figure(figsize=(10, 5))
    plt.plot(ftd_data['year'].astype(str) + '-' + ftd_data['month'].astype(str), ftd_data['ftd_count'], label='FTD', marker='o')

    # Graficar la cantidad de CPA por mes
    plt.plot(cpa_data['year'].astype(str) + '-' + cpa_data['month'].astype(str), cpa_data['cpa_count'], label='CPA', marker='o')

    # Personalizar el gráfico
    plt.title('FTD vs CPA por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Jugadores')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

# Llamar a la función para realizar el análisis
analyze_and_plot()
