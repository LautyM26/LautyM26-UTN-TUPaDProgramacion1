# Actividad 7
texto = input("Ingrese una palabra o frase: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)