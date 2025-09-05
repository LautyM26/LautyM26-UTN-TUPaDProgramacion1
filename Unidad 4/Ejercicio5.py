# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random

# Generar número aleatorio entre 0 y 9
secreto = random.randint(0, 9)

intentos = 0
adivinado = False

while not adivinado:
    numero = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    
    if numero == secreto:
        adivinado = True
        print(f"¡Correcto! El número era {secreto}.")
        print(f"Lo lograste en {intentos} intentos.")