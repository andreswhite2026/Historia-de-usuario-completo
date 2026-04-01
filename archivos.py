import csv

def guardar_csv(inventario, ruta):
    """Guardar archivo"""
    if len(inventario) == 0:
        print("Nada que guardar")
        return

    try:
        archivo = open(ruta, "w", newline="", encoding="utf-8")
        writer = csv.writer(archivo)

        writer.writerow(["nombre", "precio", "cantidad"])

        for p in inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        archivo.close()
        print("Guardado")

    except Exception:
        print("Error al guardar")


def cargar_csv(ruta):
    """Cargar archivo"""
    inventario = []
    errores = 0

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        reader = csv.reader(archivo)

        encabezado = next(reader)

        if encabezado != ["nombre", "precio", "cantidad"]:
            print("Archivo incorrecto")
            return []

        for fila in reader:
            try:
                nombre = fila[0]
                precio = float(fila[1])
                cantidad = int(fila[2])

                if precio < 0 or cantidad < 0:
                    raise ValueError

                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except Exception:
                errores += 1

        archivo.close()
        print("Errores:", errores)

        return inventario

    except Exception:
        print("No se pudo abrir el archivo")
        return []