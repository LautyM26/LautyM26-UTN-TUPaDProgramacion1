#  Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
print(f"IMC: {calcular_imc(peso, altura):.2f}")