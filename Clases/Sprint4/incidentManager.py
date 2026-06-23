# Sistema de Gestión de Incidentes - Help Desk
# Empresa: 200 empleados
# Turno: 8 horas
# Los datos se pierden al cerrar el sistema (en sprints futuros se guardarán en disco)

# Lista de incidentes pre-cargados del turno anterior
incidentes = [
    "TKT-001: usuario no puede ingresar al portal de nómina",
    "TKT-002: impresora del piso 4 sin conexión",
    "TKT-003: cliente reporta cargo duplicado"
]

while True:
    print("\n=== GESTOR DE INCIDENTES ===")
    print("1. Registrar nuevo incidente")
    print("2. Listar incidentes abiertos")
    print("3. Cerrar incidente")
    print("4. Buscar incidente por ID")
    print("5. Salir")

    opcion = input("\nElige una opción (1-5): ")

    if opcion == "1":
        print(f"Opción seleccionada: {opcion} - Registrar nuevo incidente")
        nuevo_incidente = input("Describe el nuevo incidente: ").strip()
        id_nuevo = f"TKT-{len(incidentes) + 1:03d}"
        incidente_completo = f"{id_nuevo}: {nuevo_incidente}"
        incidentes.append(incidente_completo)
        print(f"Incidente registrado: {incidente_completo}")

    elif opcion == "2":
        print(f"Opción seleccionada: {opcion} - Listar incidentes abiertos")
        print("\nIncidentes abiertos:")
        for incidente in incidentes:
            print(incidente)

    elif opcion == "3":
        print(f"Opción seleccionada: {opcion} - Cerrar incidente")
        posicion_cerrar = int(input("Ingresa el número del incidente a cerrar (1, 2, ...): ")) - 1
        if 0 <= posicion_cerrar < len(incidentes):
            cerrado = incidentes.pop(posicion_cerrar)
            print(f"Incidente cerrado: {cerrado}")
        else:
            print("Número de incidente inválido.")

    elif opcion == "4":
        print(f"Opción seleccionada: {opcion} - Buscar incidente por ID")
        id_buscar = input("Ingresa el ID del incidente a buscar (ej. TKT-002): ")
        encontrado = False
        for incidente in incidentes:
            if incidente.startswith(id_buscar):
                print(f"Incidente encontrado: {incidente}")
                encontrado = True
                break
        if not encontrado:
            print("Incidente no encontrado.")

    elif opcion == "5":
        print(f"Opción seleccionada: {opcion} - Salir")
        print("Saliendo del sistema. ¡Hasta luego!")
        break