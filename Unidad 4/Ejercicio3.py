# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

a = int(input("Ingrese el numero 1: "))
b = int(input("Ingrese el numero 2: "))

# Aseguramos que 'a' sea el menor y 'b' el mayor
if a > b:
    a, b = b, a

suma = 0
for i in range(a + 1, b):
    suma += i

print("La suma es: ", suma)