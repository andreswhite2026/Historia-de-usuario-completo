# --------------------------------------------
# Programa de Inventario Simple
# --------------------------------------------

# Solicitar nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar precio
precio = input("Ingrese el precio del producto: ")

# Validar que el precio sea un número
while not precio.replace('.', '', 1).isdigit():
    print("Error: debe ingresar un número válido para el precio.")
    precio = input("Ingrese el precio del producto nuevamente: ")

precio = float(precio)

# Solicitar cantidad
cantidad = input("Ingrese la cantidad del producto: ")

# Validar que la cantidad sea un número entero
while not cantidad.isdigit():
    print("Error: debe ingresar un número entero válido para la cantidad.")
    cantidad = input("Ingrese la cantidad del producto nuevamente: ")

cantidad = int(cantidad)

# Calcular costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# --------------------------------------------
# Explicación del programa
# --------------------------------------------
# Este programa registra un producto en un inventario.
# Primero solicita el nombre del producto.
# Luego pide el precio y verifica que sea un número válido.
# Después solicita la cantidad y valida que sea un número entero.
# Finalmente calcula el costo total multiplicando el precio por la cantidad
# y muestra toda la información en consola.
