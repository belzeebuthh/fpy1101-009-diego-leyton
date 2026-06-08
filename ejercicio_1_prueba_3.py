senior = 0
junior = 0

while True:
    cantidad = input("Cuantos medicos desea registrar? ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

for i in range(cantidad):
    print("\nMedico", i + 1)

    while True:
        nombre = input("Nombre: ")
        if len(nombre) < 6:
            print("El nombre debe tener al menos 6 caracteres.")
        elif " " in nombre:
            print("El nombre no puede tener espacios.")
        else:
            break

    while True:
        experiencia = input("Anos de experiencia: ")
        if experiencia.isdigit() and int(experiencia) > 0:
            experiencia = int(experiencia)
            break
        else:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    if experiencia > 5:
        senior = senior + 1
        print("Especialista Senior")
    else:
        junior = junior + 1
        print("Residente Junior")

print("\n¡El hospital cuenta con", senior, "Especialistas Senior y", junior, "Residentes Junior! ¡Sistema listo para operar!")