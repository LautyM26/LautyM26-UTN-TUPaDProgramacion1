# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa principal
num = int(input("Ingrese la posición de la serie Fibonacci: "))
for i in range(num):
    print(fibonacci(i), end=" ")