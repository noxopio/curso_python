# Crear diccionario como fuente de datos
peliculas = {
    1: {
        "Nombre": "Titanic",
        "Estreno": 1997,
        "Protagonista": "Leonardo DiCaprio",
        "Num_Oscar": 11,
    },
    2: {
        "Nombre": "Rocky",
        "Estreno": 1976,
        "Protagonista": "Sylvester Stallone",
        "Num_Oscar": 3,
    },
    3: {
        "Nombre": "Toy Story",
        "Estreno": 1995,
        "Protagonista": "Tom Hanks (voz de Woody)",
        "Num_Oscar": 1,
    },
    4: {
        "Nombre": "Home Alone",
        "Estreno": 1990,
        "Protagonista": "Macaulay Culkin",
        "Num_Oscar": 0,
    },
    5: {
        "Nombre": "Iron Man",
        "Estreno": 2008,
        "Protagonista": "Robert Downey Jr.",
        "Num_Oscar": 0,
    },
    6: {
        "Nombre": "Avatar",
        "Estreno": 2009,
        "Protagonista": "Sam Worthington",
        "Num_Oscar": 3,
    },
}
# Variables de tipo String con las opciones
opciones = "\t".join(f"{k}) {v['Nombre']}" for k, v in peliculas.items())

opciones2 = (
    "1) Fecha de Estreno \t 2) Protagonista \t 3) Cuantos Oscar Gano \t 4) Todo\n"
)

valor1 = int(
    input(
        "Seleccione una pelicula ingresando su valor correspondiente entre 1 y 6: \n"
        + opciones
        + "\n"
    )
)

if valor1 <= 0 or valor1 > 6:
    print("Valor incorrecto")
else:
    valor2 = int(
        input(
            "Ingrese el Dato que quiere saber ingresando su valor correspondiente entre 1 y 4: \n"
            + opciones2
        )
    )

    match valor2:
        case 1:
            print(
                "La pelicula "
                + str(peliculas[valor1]["Nombre"])
                + " se estreno en el año "
                + str(peliculas[valor1]["Estreno"])
            )
        case 2:
            print(
                "El protagonista de la pelicula "
                + str(peliculas[valor1]["Nombre"])
                + " fue el actor "
                + str(peliculas[valor1]["Protagonista"])
            )
        case 3:
            print(
                "La pelicula "
                + str(peliculas[valor1]["Nombre"])
                + " gano "
                + str(peliculas[valor1]["Num_Oscar"])
                + " Oscar"
            )
        case 4:
            print(
                "La pelicula "
                + str(peliculas[valor1]["Nombre"])
                + " protagonizada por "
                + str(peliculas[valor1]["Protagonista"])
                + " gano "
                + str(peliculas[valor1]["Num_Oscar"])
                + " Oscar"
            )
        case _:
            print("Valor incorrecto")
