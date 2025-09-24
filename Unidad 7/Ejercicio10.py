#  Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises_capitales = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago"}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(capitales_paises)