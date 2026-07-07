# OPERACIÓN 1: ALTA

registro = []

contador = 0

while True:

    print("\n=== ALTA DE EMPLEADO ===")
    nombre = input("Nombre: ")
    departamento = input("Departamento: ")
    salario_mensual = float(input("Salario mensual ($): "))
    nivel_acceso = int(input("Nivel de acceso (1-5): "))

    # Diccionario del empleado
    empleado = {
        "nombre": nombre,
        "departamento": departamento,
        "salario_mensual": salario_mensual,
        "nivel_acceso": nivel_acceso
    }
    registro.append(empleado)

    contador += 1

    if contador >= 3:
        respuesta = input(
            "¿Agregar otro empleado? (si/no): "
        )
        if respuesta != "si":
            break



# OPERACIÓN 2: LISTADO DE EMPLEADOS

print("\n=== LISTADO DE EMPLEADOS ===")

if len(registro) == 0:
    print("No hay empleados registrados")

else:
    for numero, empleado in enumerate(registro, start=1):
        print(f"\nEmpleado {numero}")
        print("  nombre:", empleado.get("nombre"))
        print("  departamento:", empleado.get("departamento"))
        print("  salario_mensual:", empleado.get("salario_mensual"))
        print("  nivel_acceso:", empleado.get("nivel_acceso"))

# OPERACIÓN 3: BÚSQUEDA POR NOMBRE

print("\n=== BÚSQUEDA DE EMPLEADO ===")
nombre_buscar = input("Ingrese el nombre a buscar: ")
encontrado = False

for empleado in registro:
    if empleado.get("nombre") == nombre_buscar:
        print("\nEmpleado encontrado")
        print("  nombre:", empleado.get("nombre"))
        print("  departamento:", empleado.get("departamento"))
        print("  salario_mensual:", empleado.get("salario_mensual"))
        print("  nivel_acceso:", empleado.get("nivel_acceso"))

        encontrado = True

        break

# Si nunca se encontró coincidencia
if not encontrado:

    print("Empleado no encontrado")


# ==============================================================
# BONUS A (OPCIONAL)
# Contar cuántos empleados hay por departamento.
# ==============================================================

print("\n=== EMPLEADOS POR DEPARTAMENTO ===")

conteo_departamentos = {}

for empleado in registro:

    departamento = empleado.get("departamento")

    if departamento in conteo_departamentos:

        conteo_departamentos[departamento] += 1

    else:

        conteo_departamentos[departamento] = 1

for departamento, cantidad in conteo_departamentos.items():

    print(f"{departamento}: {cantidad}")