def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿cuántos pesos "+ tipo_pesos +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $ "+ dolares + "  dólares")

menu =  """
Bienvenido al conversor de Monedas💲


1   - Pesos Colombianos
2   - Pesos Argentinos
3   - Pesos mexicanos

Elige una opción:

"""
opcion = int(input(menu))


if opcion == 1:
    conversor("colombianos", 4800)
elif opcion == 2:
    conversor("Argentinos",65)
elif opcion == 3:
    conversor("Mexicanos",24)
else:    
    print("Ingresa una opcion correcta")





