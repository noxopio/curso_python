from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    main()
