# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3
num = int(input("Ingrese un número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Actividad 5
contra = input("Ingrese su contraseña: ")
if 8 <= len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
m = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", m, "Mediana:", med, "Moda:", moda)

if m > med > moda:
    print("Sesgo positivo o a la derecha")
elif m < med < moda:
    print("Sesgo negativo o a la izquierda")
elif m == med == moda:
    print("Sin sesgo")
else:
    print("No se cumple ningún sesgo exacto")

# Actividad 7
texto = input("Ingrese una palabra o frase: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

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

# Actividad 9
magnitud = float(input("Ingrese magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Actividad 10
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día: "))

if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estación:", estacion)
