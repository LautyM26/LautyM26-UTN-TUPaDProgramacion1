#  Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
num = int(input("Ingrese un número decimal: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")