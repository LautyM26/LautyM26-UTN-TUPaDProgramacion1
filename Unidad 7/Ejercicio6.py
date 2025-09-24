# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Nota {_+1} del alumno {nombre}: ")) for _ in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")