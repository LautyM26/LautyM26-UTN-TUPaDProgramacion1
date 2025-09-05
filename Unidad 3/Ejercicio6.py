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