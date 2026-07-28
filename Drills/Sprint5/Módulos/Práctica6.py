# BASE DE RECLUTAS · INADAPTADOS
# Base de talento con menu de 4 opciones.
# Cada recluta es un diccionario con 5 campos:
#   nombre, area, salario_mensual, estatus, email

# Lista de arranque (ya poblada con 3 reclutas).
base_reclutas = [
    {
        "nombre": "Ana Torres",
        "area": "Finanzas",
        "salario_mensual": 28500.0,
        "estatus": "activo",
        "email": "ana.torres@inadaptados.mx"
    },
    {
        "nombre": "Luis Quintero",
        "area": "Logistica",
        "salario_mensual": 19200.0,
        "estatus": "activo",
        "email": "luis.quintero@inadaptados.mx"
    },
    {
        "nombre": "Mara Ibarra",
        "area": "Salud",
        "salario_mensual": 133750.0,
        "estatus": "inactivo",
        "email": "mara.ibarra@inadaptados.mx"
    },
]

while True:
    print()
    print("=== BASE DE RECLUTAS · INADAPTADOS ===")
    print("1) Alta de recluta")
    print("2) Listado (reporte)")
    print("3) Buscar por nombre")
    print("4) Salir")

    opcion = input("Elige una opcion: ").strip()

    # Opción 1: Alta
    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        area = input("Área: ").strip().title()
        salario = float(input("Salario mensual: ").strip())
        estatus = input("Estatus: ").strip().lower()
        email = input("Email: ").strip().lower()

        recluta = {
            "nombre": nombre,
            "area": area,
            "salario_mensual": salario,
            "estatus": estatus,
            "email": email
        }

        base_reclutas.append(recluta)

        print(f"\n[OK] Recluta '{nombre}' agregado correctamente.")
        print(f"Total de reclutas: {len(base_reclutas)}")

    # Opción 2: Listado
    elif opcion == "2":
        print()
        print(f'{"NOMBRE":<18}{"AREA":<14}{"ESTATUS":<11}{"SALARIO":>14}')
        print("-" * 57)

        for recluta in base_reclutas:
            print(
                f'{recluta["nombre"]:<18}'
                f'{recluta["area"]:<14}'
                f'{recluta["estatus"]:<11}'
                f'{recluta["salario_mensual"]:>14,.2f}'
            )

        print("-" * 57)
        print(f"Total de reclutas: {len(base_reclutas)}")

    # Opción 3: Buscar
    elif opcion == "3":
        termino = input("Nombre a buscar: ").strip().lower()

        encontrados = 0

        for recluta in base_reclutas:
            if termino in recluta["nombre"].lower():
                print()
                print(f'Nombre: {recluta["nombre"]}')
                print(f'Área: {recluta["area"]}')
                print(f'Estatus: {recluta["estatus"]}')
                print(f'Salario: {recluta["salario_mensual"]:,.2f}')
                print(f'Email: {recluta["email"]}')
                print("-" * 30)
                encontrados += 1

        if encontrados == 0:
            print("No se encontraron coincidencias.")

    # Opción 4: Salir
    elif opcion == "4":
        print("Gracias por usar la Base de Reclutas. ¡Hasta luego!")
        break

    # Opción inválida
    else:
        print("❌ Opción inválida. Intenta nuevamente.")