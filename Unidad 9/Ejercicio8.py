# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número. Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# Programación I
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Programa principal
num = int(input("Ingrese un número: "))
d = int(input("Ingrese un dígito (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}")