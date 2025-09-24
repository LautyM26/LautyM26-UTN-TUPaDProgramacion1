# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

# Aprobó ambos
ambos = parcial1 & parcial2
print("Aprobó ambos:", ambos)

# Solo uno de los dos
solo_uno = parcial1 ^ parcial2
print("Solo uno de los dos:", solo_uno)

# Al menos un parcial
al_menos_uno = parcial1 | parcial2
print("Al menos un parcial:", al_menos_uno)