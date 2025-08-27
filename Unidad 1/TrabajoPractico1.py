# Actividad 1   

print("Hola mundo")


# Actividad 2
nombre = input("¿Cómo te llamás?")
print(f"Hola " + nombre)


# Actividad 3

nombre = input("¿Cómo te llamás?")
apellido = input("¿Cómo te apellidas?")
edad = input("¿Cuantos años tienes?")
lugar = input("¿De donde eres?")

print(f"Hola soy {nombre} {apellido} Tengo {edad} años y vivo en {lugar}.")


# Actividad 4

pi = 3.1416

radio = float(input("Ingresa el radio del círculo: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


# Actividad 5

segundos = float(input("Ingresa la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")


# Actividad 6

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"El numero {numero} x 1 da un resultado de: {numero * 1}")
print(f"El numero {numero} x 2 da un resultado de: {numero * 2}")
print(f"El numero {numero} x 3 da un resultado de: {numero * 3}")
print(f"El numero {numero} x 4 da un resultado de: {numero * 4}")
print(f"El numero {numero} x 5 da un resultado de: {numero * 5}")
print(f"El numero {numero} x 6 da un resultado de: {numero * 6}")
print(f"El numero {numero} x 7 da un resultado de: {numero * 7}")
print(f"El numero {numero} x 8 da un resultado de: {numero * 8}")
print(f"El numero {numero} x 9 da un resultado de: {numero * 9}")
print(f"El numero {numero} x 10 da un resultado de: {numero * 10}")


# Actividad 7

numero1 = int(input("Ingresa un número que no sea 0: "))
numero2 = int(input("Ingresa un número que no sea 0: "))

print(f"La suma de los numeros que selecciono da: {numero1 + numero2}")
print(f"La division de los numeros que selecciono da: {numero1 / numero2}")
print(f"La multiplicacion de los numeros que selecciono da: {numero1 * numero2}")
print(f"La resta de los numeros que selecciono da: {numero1 - numero2}")


# Actividad 8

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


# Actividad 9

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# Actividad 10 

numero1 = int(input("Ingresa el primer numero para promediar: "))
numero2 = int(input("Ingresa el segundo numero para promediar: "))
numero3 = int(input("Ingresa el tercer numero para promediar: "))

suma = numero1 + numero2 + numero3

promedio = print(f"El promedio de los 3 numeros da: {suma / 3}")