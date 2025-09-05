# Actividad 8

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")