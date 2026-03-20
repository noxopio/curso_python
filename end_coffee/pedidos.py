ARCHIVOS_PEDIDOS = "historial_bebidas.txt"


def pedir_cafe():
    print("\n Elige el cafe que prefieres: ")
    print("1. Espresso")
    print("2. Americano")
    print("3. Cappuccino")
    print("4. Latte")

    opcion = input("Seleccione una opción: ")

    cafes = {"1": "Espresso", "2": "Americano", "3": "Cappuccino", "4": "Latte"}

    if opcion in cafes:
        print(f"Preparando {cafes[opcion]}...")
        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{cafes[opcion]}\n")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
