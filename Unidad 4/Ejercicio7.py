# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero positivo: "))
suma = 0

for i in range(0, numero, 1):
    suma = suma + i

print(suma)