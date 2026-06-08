libros = 120
historial = 0

print("Bienvenida")
print("Bienvenido al sistema de gestión de préstamos de la Biblioteca Central")

while True:
    print("\n===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        print("Libros disponibles:", libros)

    elif opcion == "2":
        while True:
            cantidad = input("Cuantos libros desea prestar? ")
            if not cantidad.isdigit() or int(cantidad) <= 0:
                print("Valor inválido. Ingresa un número mayor a 0.")
            elif int(cantidad) > libros:
                print("No hay suficientes libros disponibles. Stock actual:", libros)
            else:
                cantidad = int(cantidad)
                libros = libros - cantidad
                historial = historial + cantidad
                print("tus", cantidad, "libros fuero registrados correctamente. Ahora hay", libros, "libros disponibles.")
                break

    elif opcion == "3":
        while True:
            cantidad = input("Cuantos libros desea devolver? ")
            if not cantidad.isdigit() or int(cantidad) <= 0:
                print("Valor inválido. Ingresa un número mayor a 0.")
            elif libros + int(cantidad) > 120:
                print("No se puede devolver esa cantidad. Supera el máximo de 120 libros.")
            else:
                cantidad = int(cantidad)
                libros = libros + cantidad
                historial = historial - cantidad
                print("Devolución de", cantidad, "libros realizada. Libros restantes:", libros)
                break

    elif opcion == "4":
        print("Total de préstamos activos durante la sesión:", historial)

    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima querido usuario.")
        break

    else:
        print("Opción inválida. Elige una opción entre 1 y 5.")