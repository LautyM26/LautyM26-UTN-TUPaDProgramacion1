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