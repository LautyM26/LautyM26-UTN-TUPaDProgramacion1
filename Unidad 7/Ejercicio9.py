# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {}

# Cargar eventos
for _ in range(3):
    dia = input("Día: ")
    hora = input("Hora: ")
    evento = input("Evento: ")
    agenda[(dia, hora)] = evento

# Consultar evento
dia = input("Ingrese día a consultar: ")
hora = input("Ingrese hora a consultar: ")
print("Evento:", agenda.get((dia, hora), "No hay evento"))