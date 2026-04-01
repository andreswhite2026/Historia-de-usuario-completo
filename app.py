def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto"""
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """Muestra productos"""
    if len(inventario) == 0:
        print("No hay productos")
    else:
        for p in inventario:
            print(p["nombre"], "-", p["precio"], "-", p["cantidad"])


def buscar_producto(inventario, nombre):
    """Busca producto"""
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza producto"""
    for p in inventario:
        if p["nombre"] == nombre:
            if nuevo_precio is not None:
                p["precio"] = nuevo_precio
            if nueva_cantidad is not None:
                p["cantidad"] = nueva_cantidad
            print("Actualizado")
            return
    print("No existe")


def eliminar_producto(inventario, nombre):
    """Elimina producto"""
    for p in inventario:
        if p["nombre"] == nombre:
            inventario.remove(p)
            print("Eliminado")
            return
    print("No existe")


def calcular_estadisticas(inventario):
    """Calcula datos"""
    if len(inventario) == 0:
        return None

    unidades = 0
    valor = 0

    mas_caro = inventario[0]
    mayor_stock = inventario[0]

    for p in inventario:
        unidades += p["cantidad"]
        valor += p["precio"] * p["cantidad"]

        if p["precio"] > mas_caro["precio"]:
            mas_caro = p

        if p["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = p

    return unidades, valor, mas_caro, mayor_stock