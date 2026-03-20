# fruta = {"manzana", "pera", "naranja", "manzana"}
# print(fruta)
# # conjuntos no permiten elementos repetidos, por lo tanto se elimina la segunda "manzana"
# print(type(fruta))
# print(len(fruta))

# print(list(set(fruta)))

# for f in fruta:
#     print(f)

#     import json

# mi_diccionario = {"nombre": "Ejemplo", "valor": 123}
# json_string = json.dumps(mi_diccionario)
# print(mi_diccionario)
# print(json_string)


def sumar(a, b):
    return a + b  # Retorno de valor


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def division(a, b):
    return a / b


resultados = sumar(10, 2), resta(5, 3), multiplicar(2, 4), division(20, 5)
print("Resultados:", resultados)
