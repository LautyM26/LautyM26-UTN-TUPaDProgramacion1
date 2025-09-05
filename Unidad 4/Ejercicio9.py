#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0
cantidad = 10  

for i in range(cantidad):
    i = int(input("Ingrese un número: "))
    suma = suma + i

promedio = suma / cantidad
print("La media es:", promedio)