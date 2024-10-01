# Escritura de Archivo de Texto
# Creamos un archivo llamado 'my_notes.txt' y escribimos tres líneas de notas personales.
# Utilizamos el modo 'w' para escribir en el archivo

my_notes = open( "my_notes.txt", "w")
# Método write(): escribir una linea a la vez

my_notes.write("Primera nota: Aprendiendo a trabajar con archivos en Python.\n")
my_notes.write("Segunda nota: Practicando voy a mejorar.\n")
my_notes.write("Tercera nota: ¡No te olvides cerrar los archivos!\n")

# Método Writelines(): escribir una lista en lineas

lineas = [ "Cuarta nota: Otro Ejemplo.\n", "Quinta Nota: finalizando el trabajo.\n"]
my_notes.writelines(lineas)

my_notes.close()

# Abrimos el archivo 'my_notes.txt' en modo de lectura.
# Utilizamos el modo 'r' para leer el archivo
my_notes = open("my_notes.txt", "r")

# Leemos el contenido del archivo linea por linea utilizando el método adecuado.

# Método 1. read()
print("Método 1: read()")
print("______________________")
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open("my_notes.txt", "r")
print("Método 2: readlines()")
print("______________________")
for linea in my_notes.readlines():
    print(linea.rstrip("\n"))
    my_notes.close()