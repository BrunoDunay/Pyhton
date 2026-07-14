# Sistema de Ficha de Recluta

print("=== REGISTRO DE RECLUTA ===\n")

# TODO 1
recluta = {
    "nombre": "Bruno",
    "edad": 24,
    "rango": "Cadete",
    "puntos": 850,
    "especialidad": "Desarrollo Web"
}

# TODO 2
print("--- FICHA COMPLETA ---")
for clave, valor in recluta.items():
    print(f"{clave}: {valor}")

# TODO 3
print("\n--- PROMOCIÓN ---")
recluta["rango"] = "Aprendiz"
recluta["puntos"] += 150

print(f"Nuevo rango: {recluta['rango']}")
print(f"Puntos totales: {recluta['puntos']}")

# TODO 4
recluta["proyecto_actual"] = "Sistema de Gestión Militar"
recluta["mentores"] = ["Carlos", "Ana", "Luis"]

# TODO 5
print("\n--- CAMPOS DISPONIBLES ---")
for clave in recluta.keys():
    print(f"- {clave}")

# TODO 6
certificaciones = recluta.get("certificaciones", [])
print("\nCertificaciones:", certificaciones)

# TODO 7
if "proyecto_actual" in recluta:
    proyecto_eliminado = recluta.pop("proyecto_actual")
    print("\nProyecto eliminado:", proyecto_eliminado)

# TODO 8
print("\n--- FICHA FINAL ---")
for clave, valor in recluta.items():
    print(f"{clave}: {valor}")