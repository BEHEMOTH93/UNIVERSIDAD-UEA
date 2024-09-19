# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=15):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada 1: Usando el valor por defecto del porcentaje de descuento (15%)
monto1 = 100  # Monto total de la compra
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Llamada 2: Especificando un porcentaje de descuento diferente (15%)
monto2 = 200  # Monto total de la compra
descuento2 = calcular_descuento(monto2, 15)
monto_final2 = monto2 - descuento2

# Mostrar resultados de la primera llamada
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")
print()

# Mostrar resultados de la segunda llamada
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")
