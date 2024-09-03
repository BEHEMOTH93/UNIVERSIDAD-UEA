# Definimos las dimensiones de la matriz 3D
# 3 ciudades
ciudades = ["Quito", "Esmeraldas", "Tena"]

# 7 días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 4 semanas
semanas = 4

# Inicializamos la matriz 3D para almacenar las temperaturas
import random

temperaturas = [[[random.uniform(10.0, 30.0) for _ in range(len(dias))] for _ in range(semanas)] for _ in ciudades]

# Calculamos los promedios de temperaturas por ciudad y por semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")

    for semana in range(semanas):
        total_temperatura_semana = sum(temperaturas[i][semana])  # Suma las temperaturas de la semana
        promedio_semana = total_temperatura_semana / len(dias)  # Calcula el promedio
        print(f"  Semana {semana + 1}: {promedio_semana:.2f} °C")
