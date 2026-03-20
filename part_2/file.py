# open (nombre,modo)
# R (read). Es el modo predeterminado. Permite leer el contenido del archivo.
# W (write). Permite escribir en el archivo. Si el archivo ya existe, se sobrescribirá. Si no existe, se creará uno nuevo.
# A (append). Permite agregar contenido al final del archivo sin sobrescribirlo. Si
# X (exclusive creation). Crea un nuevo archivo, pero falla si el archivo ya existe.

# try:
#     f = open("archivo.txt", "r")
#     print(f.readline())
#     f.close()
# except FileNotFoundError:
#     print("El archivo no existe.")
# try:
#     with open("archivo.txt", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("El archivo no existe.")


try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")
    open("archivo.txt", "x")
    print("Archivo creado exitosamente.")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")


try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("Hola, este es un nuevo archivo.\n")
        f.write("Esta es la segunda línea.")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")
