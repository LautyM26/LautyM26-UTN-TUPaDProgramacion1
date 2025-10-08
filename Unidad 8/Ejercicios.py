# Crear el archivo productos.txt con tres productos
with open("productos.txt", "w") as archivo:
    archivo.write("Monitor,200,50\n")
    archivo.write("Teclado,80,70\n")
    archivo.write("Mouse,50,70\n")

print("Archivo 'productos.txt' creado correctamente.")



# Leer y mostrar productos del archivo productos.txt
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Eliminar saltos de línea y dividir por comas
        nombre, precio, cantidad = linea.strip().split(",")

        # Mostrar el producto con el formato pedido
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")



# Pedir al usuario que ingrese un nuevo producto
print("\n--- Agregar nuevo producto ---")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

# Agregar el nuevo producto al archivo sin borrar el contenido
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado correctamente ✅")



# Cargar productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar la lista de productos
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Mostrar la lista completa (opcional, para verificar)
print("\nLista de diccionarios:")
for p in productos:
    print(p)



# Cargar productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar productos cargados (opcional)
print("\nProductos disponibles:")
for p in productos:
    print(f"- {p['nombre']}")

# Buscar producto por nombre
print("\n--- Búsqueda de producto ---")
busqueda = input("Ingrese el nombre del producto que desea buscar: ")

# Variable para marcar si se encontró
encontrado = False

for p in productos:
    if p["nombre"].lower() == busqueda.lower():
        print(f"\nProducto encontrado ✅")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n❌ El producto no existe en la lista.")



# Cargar productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar productos cargados
print("\nProductos disponibles:")
for p in productos:
    print(f"- {p['nombre']}")

# Agregar un nuevo producto desde teclado
print("\n--- Agregar nuevo producto ---")
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

productos.append({
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
})

print("\nProducto agregado correctamente ✅")

# Guardar los productos actualizados en productos.txt (sobrescribiendo)
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado con éxito ✅")