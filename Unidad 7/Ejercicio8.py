# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock = {}

while True:
    opcion = input("Ingrese 'consultar', 'agregar' o 'nuevo' (salir para terminar): ").lower()
    if opcion == "salir":
        break
    producto = input("Nombre del producto: ")
    
    if opcion == "consultar":
        print(f"Stock de {producto}: {stock.get(producto, 0)}")
    elif opcion == "agregar":
        unidades = int(input("Cantidad a agregar: "))
        if producto in stock:
            stock[producto] += unidades
        else:
            print("Producto no existe.")
    elif opcion == "nuevo":
        unidades = int(input("Cantidad inicial: "))
        stock[producto] = unidades
    print(stock)