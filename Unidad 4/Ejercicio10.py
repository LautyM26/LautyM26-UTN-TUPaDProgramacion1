# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Pedimos un número al usuario
numero = input("Ingrese un número: ")

# Invertimos la cadena usando slicing [::-1]
numero_invertido = numero[::-1]

print("Número invertido:", numero_invertido)