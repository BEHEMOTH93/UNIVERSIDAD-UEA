# Función para calcular el promedio de temperatura por ciudad
def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio por ciudad.

    Parámetros:
    datos_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas de temperaturas semanales.

    Retorna:
    dict: Un diccionario con las ciudades y sus respectivas temperaturas promedio.
    """
    promedios = {}

    # Recorrer cada ciudad y sus datos de temperaturas
    for ciudad, temperaturas in datos_temperaturas.items():
        # Calcular el promedio de las temperaturas
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Datos de ejemplo (3 ciudades durante 4 semanas)
datos = {
    'Quito': [22.5, 23.1, 21.9, 22.0],
    'Guayaquil': [25.3, 26.1, 24.7, 25.0],
    'Cuenca': [19.8, 20.1, 18.7, 19.5]
}

# Llamada a la función
resultados = calcular_temperatura_promedio(datos)

# Mostrar resultados
for ciudad, promedio in resultados.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")
