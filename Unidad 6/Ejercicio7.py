# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: división por 0"
    return suma, resta, multiplicacion, division

# Programa principal
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")