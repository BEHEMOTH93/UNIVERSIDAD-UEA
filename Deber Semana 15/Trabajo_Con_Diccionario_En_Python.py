# Crear un diccionario llamado 'informacion_personal' con claves: nombre, edad, ciudad, y profesion
informacion_personal = {
    "nombre": "Rafael Lopez",
    "edad": 31,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
# Cambiamos la ciudad a "Guayaquil"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario, que represente el "correo" de la persona
informacion_personal["correo"] = "ra.ralt@example.com"

# Verificar si la clave "telefono" existe en el diccionario, si no existe, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0966633396"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario, ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las modificaciones
print(informacion_personal)

