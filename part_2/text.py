texto = "Este es un texto."

print(
    texto[0:4]
)  # Desde el indice 0 hasta el 3, el caracter en el indice 4 no se incluye
print(texto[5:7])  # Desde el indice 5 hasta el 6
print(texto[:7])  # Desde el inicio hasta el indice 6
print(texto[10:])  # Desde el indice 10 hasta el final
print(texto[-5:])  # Ultimos 5 caracteres
print(texto[:-5])  # Desde el inicio hasta 5 caracteres antes del final
print(texto[::2])  # Desde el inicio hasta el final, tomando cada 2 caracteres

curso = "Este curso  es de  Python"
print(curso.replace("Python", "Bash"))
print(curso.split())  # Divide el texto en palabras, usando espacios como separadores
# Normalizacion de textos
textoNormalizado = "  PyThOn Es GeNiAl  "
textoNormalizado = textoNormalizado.strip().lower()
print(textoNormalizado)  # Output: "python es genial"
