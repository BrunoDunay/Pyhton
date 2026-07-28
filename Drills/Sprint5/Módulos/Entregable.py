# Sistema de Gestión de Reclutas - Sprint 5 ENTREGABLE

print("=== SISTEMA DE GESTIÓN DE RECLUTAS ===\n")

reclutas = [
    {"nombre": "Ana López", "edad": 25, "email": "ana@example.com", "rango": "Aprendiz", "puntos": 200},
    {"nombre": "Luis García", "edad": 30, "email": "luis@example.com", "rango": "Experto", "puntos": 500},
    {"nombre": "Carlos Ruiz", "edad": 22, "email": "carlos@example.com", "rango": "Novato", "puntos": 100}
]

# TODO 1
def limpiar_string(texto):
    return texto.strip()

# TODO 2
def validar_email(email):
    email = email.strip().lower()

    if "@" not in email:
        return False

    dominio = email.split("@")[1]

    return "." in dominio

# TODO 3
def dar_alta_recluta():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")

    if not edad.isdigit() or not (18 <= int(edad) <= 100):
        print("❌ Edad inválida.")
        return

    if not validar_email(email):
        print("❌ Email inválido.")
        return

    nuevo = {
        "nombre": limpiar_string(nombre).title(),
        "edad": int(edad),
        "email": email.strip().lower(),
        "rango": "Novato",
        "puntos": 0
    }

    reclutas.append(nuevo)

    print(f"✅ Recluta '{nuevo['nombre']}' agregado correctamente.")

# TODO 4
def listar_reclutas():
    if not reclutas:
        print("No hay reclutas registrados.")
        return

    print(f"{'#':<4}{'Nombre':<20}{'Edad':<6}{'Rango':<12}{'Puntos':>8}")
    print("-" * 52)

    for i, recluta in enumerate(reclutas, 1):
        print(
            f"{i:<4}"
            f"{recluta['nombre']:<20}"
            f"{recluta['edad']:<6}"
            f"{recluta['rango']:<12}"
            f"{recluta['puntos']:>8,}"
        )

    print("-" * 52)
    print(f"Total de reclutas: {len(reclutas)}")

# TODO 5
def buscar_recluta():
    termino = input("Buscar nombre: ").strip().lower()

    encontrados = 0

    for recluta in reclutas:
        if termino in recluta["nombre"].lower():
            print(f"\nNombre: {recluta['nombre']}")
            print(f"Email: {recluta['email']}")
            print(f"Rango: {recluta['rango']}")
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron coincidencias.")

# TODO 6
def actualizar_puntos():
    if not reclutas:
        print("No hay reclutas registrados.")
        return

    print("\n=== RECLUTAS ===")

    for i, recluta in enumerate(reclutas, 1):
        print(f"{i}. {recluta['nombre']} ({recluta['puntos']} puntos)")

    opcion = input("Selecciona un recluta: ").strip()

    if not opcion.isdigit():
        print("❌ Selección inválida.")
        return

    indice = int(opcion) - 1

    if indice < 0 or indice >= len(reclutas):
        print("❌ Recluta inexistente.")
        return

    puntos_str = input("Puntos a agregar (pueden ser negativos): ").strip()

    if not puntos_str.lstrip("-").isdigit():
        print("❌ Cantidad inválida.")
        return

    puntos = int(puntos_str)

    reclutas[indice]["puntos"] += puntos

    print(f"✅ Ahora {reclutas[indice]['nombre']} tiene {reclutas[indice]['puntos']} puntos.")

# TODO 7
def mostrar_estadisticas():
    if not reclutas:
        print("No hay reclutas registrados.")
        return

    total = len(reclutas)
    puntos_totales = sum(r["puntos"] for r in reclutas)
    promedio = puntos_totales / total

    top = max(reclutas, key=lambda r: r["puntos"])

    rangos = {}

    for recluta in reclutas:
        rango = recluta["rango"]
        rangos[rango] = rangos.get(rango, 0) + 1

    print("\n=== ESTADÍSTICAS ===")
    print(f"Total de reclutas: {total}")
    print(f"Puntos totales: {puntos_totales:,}")
    print(f"Promedio de puntos: {promedio:.2f}")
    print(f"Top recluta: {top['nombre']} ({top['puntos']} puntos)")

    print("\nReclutas por rango:")

    for rango, cantidad in rangos.items():
        print(f"- {rango}: {cantidad}")

# TODO 8
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Alta de recluta")
    print("2. Listar reclutas")
    print("3. Buscar recluta")
    print("4. Actualizar puntos")
    print("5. Mostrar estadísticas")
    print("6. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        dar_alta_recluta()

    elif opcion == "2":
        listar_reclutas()

    elif opcion == "3":
        buscar_recluta()

    elif opcion == "4":
        actualizar_puntos()

    elif opcion == "5":
        mostrar_estadisticas()

    elif opcion == "6":
        print("¡Gracias por usar el sistema de gestión de reclutas!")
        break

    else:
        print("❌ Opción inválida.")