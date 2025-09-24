# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Conteo de palabras
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Conteo de palabras:", conteo)