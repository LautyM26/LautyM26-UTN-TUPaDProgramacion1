# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

# Cargar 5 contactos
for _ in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número de teléfono: ")
    contactos[nombre] = numero

# Consultar un contacto
nombre_buscar = input("Ingrese un nombre a consultar: ")
if nombre_buscar in contactos:
    print(f"Número de {nombre_buscar}: {contactos[nombre_buscar]}")
else:
    print("Contacto no encontrado.")