ARCHIVOS_PEDIDOS = "historial_bebidas.txt"


def ver_historial():
    try:
        print("\n Historial de bebidas preparadas:\n")
        with open(ARCHIVOS_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(f"{i}. {pedido.strip()}")
                    # print(str(i) + ". " + pedido.strip())
            else:
                print("No se han preparado bebidas aún.")

    except FileNotFoundError:
        print("\n Aun no exite historial de pedidos.")
        return
