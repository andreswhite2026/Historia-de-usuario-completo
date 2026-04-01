# ==============================
# SISTEMA DE INVENTARIO
# ==============================

inventario = []

# ------------------------------
# Función para validar números
# ------------------------------
def pedir_numero(mensaje, tipo):
    valido = False

    while not valido:
        dato = input(mensaje)

        try:
            valor = tipo(dato)

            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                valido = True
                return valor

        except:
            print("Entrada inválida. Intente nuevamente.")


# ------------------------------
# Agregar producto
# ------------------------------
def agregar_producto():
    print("\nAgregar nuevo producto")

    nombre = input("Nombre: ").strip()

    precio = pedir_numero("Precio: ", float)
    cantidad = pedir_numero("Cantidad: ", int)

    producto = {
        "nombre": nombre.capitalize(),
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")


# ------------------------------
# Mostrar inventario
# ------------------------------
def mostrar_inventario():
    print("\nInventario actual")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        indice = 1
        for producto in inventario:
            print(f"{indice}. Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
            indice += 1


# ------------------------------
# Calcular estadísticas
# ------------------------------
def calcular_estadisticas():
    print("\nEstadísticas del inventario")

    if len(inventario) == 0:
        print("No hay datos para calcular.")
    else:
        valor_total = 0
        total_unidades = 0

        for producto in inventario:
            valor_total = valor_total + (producto["precio"] * producto["cantidad"])
            total_unidades = total_unidades + producto["cantidad"]

        print("Valor total del inventario:", valor_total)
        print("Cantidad total de productos:", total_unidades)


# ------------------------------
# Menú
# ------------------------------
def menu():
    print("\n====================")
    print("MENU PRINCIPAL")
    print("====================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion


# ------------------------------
# Programa principal
# ------------------------------
opcion = ""

while opcion != "4":
    opcion = menu()

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        calcular_estadisticas()

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        print("Opción inválida. Intente nuevamente.")


# ---------------------------------------
# Objetivo:
# Este programa permite gestionar un inventario
# utilizando listas y diccionarios. Se aplican
# estructuras condicionales y ciclos para validar
# datos, almacenar información y calcular
# estadísticas básicas.
# ---------------------------------------
