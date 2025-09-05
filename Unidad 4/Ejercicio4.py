# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

i = int(input("ingrese un numero: "))
suma = 0

while i != 0:
    suma = suma + i 
    i = int(input("ingrese otro numero: "))

print(suma)