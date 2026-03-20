# o = "    5 is greater than 3"

# print(o.split())
# print(o.split(" "))

# dic = {"clave1": [1, 2, 3], "clave2": [4, 5, 6], "clave3": [7, 8, 9]}


# print(dic["clave2"][1])

# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.get("clave1"))
# print(len(dic))
# prueba = 10 == 10
# print(prueba)


# div = 17834 / 34
# mult = 87 * 56

# print(div > mult)

# raiz = 25**0.5

# print(raiz)

# print(raiz == 5)


# redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]

# print(redes)
# print(sorted(redes))


## ingreesar un texto, luego ingresar tres letras y contar cuantas veces aparece cada letra en el texto,cuantas palabras tiene el texto y mostrar el resultado, primeta y ultima letra ,palabras en orden inverso,dtetectar si en el texto esta la palabra "python"


texto = input("Ingrese un texto:\t ")
letra1 = input("Ingrese la primera letra:\t ")
letra2 = input("Ingrese la segunda letra:\t ")
letra3 = input("Ingrese la tercera letra:\t ")

contador_letra1 = texto.count(letra1)
contador_letra2 = texto.count(letra2)
contador_letra3 = texto.count(letra3)
palabras = texto.split()
print(palabras)
cantidad_palabras = len(palabras)
primera_letra = texto[0]
ultima_letra = texto[-1]
palabras_invertidas = " ".join(palabras[::-1])
palabra_a_buscar = "python"
encontrada = palabra_a_buscar in texto
print(f"La letra '{letra1}' aparece {contador_letra1} veces.")
print(f"La letra '{letra2}' aparece {contador_letra2} veces.")
print(f"La letra '{letra3}' aparece {contador_letra3} veces.")
print(f"El texto tiene {cantidad_palabras} palabras.")
print(
    f"La primera letra del texto es '{primera_letra}' y la última letra es '{ultima_letra}'."
)
print(f"Las palabras en orden inverso son: {palabras_invertidas}")

dic = {True: "Es verdadero", False: "Es falso"}
print(dic[encontrada])

if encontrada:
    print(f"La palabra '{palabra_a_buscar}' se encuentra en el texto.")
else:
    print(f"La palabra '{palabra_a_buscar}' no se encuentra en el texto.")
