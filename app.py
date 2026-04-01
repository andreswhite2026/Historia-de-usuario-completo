from servicios import agregar_producto,mostrar_inventario,buscar_producto,actualizar_producto,eliminar_producto,calcular_estadisticas
from archivos import guardar_csv,cargar_csv

inventario = []
activo = True
while activo:
    print("\n1 Agregar")
    print("2 Mostrar")
    print("3 Buscar")
    print("4 Actualizar")
    print("5 Eliminar")
    print("6 Estadisticas")
    print("7 Guardar")
    print("8 Cargar")
    print("9 Salir")

    try:
        op = int(input("Opcion: "))

        if op == 1:
            n = input("Nombre: ")
            p = float(input("Precio: "))
            c = int(input("Cantidad: "))
            agregar_producto(inventario, n, p, c)

        elif op == 2:
            mostrar_inventario(inventario)

        elif op == 3:
            n = input("Nombre: ")
            print(buscar_producto(inventario, n))

        elif op == 4:
            n = input("Nombre: ")
            p = input("Precio nuevo: ")
            c = input("Cantidad nueva: ")

            actualizar_producto(
                inventario,
                n,
                float(p) if p != "" else None,
                int(c) if c != "" else None
            )

        elif op == 5:
            n = input("Nombre: ")
            eliminar_producto(inventario, n)

        elif op == 6:
            datos = calcular_estadisticas(inventario)
            if datos:
                print("Unidades:", datos[0])
                print("Valor total:", datos[1])
                print("Mas caro:", datos[2])
                print("Mayor stock:", datos[3])
            else:
                print("Nada")

        elif op == 7:
            r = input("Ruta: ")
            guardar_csv(inventario, r)

        elif op == 8:
            r = input("Ruta: ")
            nuevos = cargar_csv(r)

            if len(nuevos) > 0:
                x = input("Sobrescribir? s/n: ")

                if x == "s":
                    inventario = nuevos
                else:
                    for p in nuevos:
                        encontrado = buscar_producto(inventario, p["nombre"])
                        if encontrado:
                            encontrado["cantidad"] += p["cantidad"]
                        else:
                            inventario.append(p)

        elif op == 9:
            break

        else:
            print("Mal")

    except Exception:
        print("Error")
