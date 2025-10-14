# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Programa principal
num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")