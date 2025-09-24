# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números 
# al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
print(f"Promedio: {calcular_promedio(n1, n2, n3):.2f}")