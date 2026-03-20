nombre = input("Ingrese su nombre:")
ingresos = float(input("Ingrese sus ingresos:"))
ingresos_Mensuales = round(ingresos * 13 / 100, 2)
print(f"{nombre}, sus ingresos mensuales son: {ingresos_Mensuales}")
