# GESTOR DE NOMBRES — ÍNDICES, SLICING Y BÚSQUEDA

# TODO 1
nombres = ["Ana", "Luis", "Carlos", "María", "Pedro", "Sofía", "Diego"]

# TODO 2
print("=== Lista Completa ===")
print(nombres)
print(f"Total de nombres: {len(nombres)}")

# ===== ACCESO POR ÍNDICE =====

# TODO 3
print("\n=== Acceso por Índice ===")
print(f"Primer nombre: {nombres[0]}")
print(f"Último nombre: {nombres[-1]}")
print(f"Tercer nombre: {nombres[2]}")

# ===== SLICING =====

# TODO 4
print("\n=== Slicing ===")
print(f"Primeros 3 nombres: {nombres[:3]}")
print(f"Últimos 2 nombres: {nombres[-2:]}")
print(f"Del 2º al 5º: {nombres[1:5]}")
print(f"Todos menos el primero y el último: {nombres[1:-1]}")

# ===== BÚSQUEDA =====

# TODO 5
print("\n=== Búsqueda ===")

buscar = "Carlos"

if buscar in nombres:
    posicion = nombres.index(buscar)
    print(f"{buscar} está en la posición {posicion}")
else:
    print(f"{buscar} no está en la lista")

# TODO 6
nuevo = "Roberto"

if nuevo not in nombres:
    nombres.append(nuevo)
    print("Lista actualizada:")
    print(nombres)
else:
    print(f"{nuevo} ya existe en la lista")