# Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (MAY), 2 (min), 3 (Primera may): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")