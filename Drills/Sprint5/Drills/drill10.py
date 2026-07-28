# DRILL 5: REPORTE DE ACREDITADOS — SOFÍA CIERRA LA SEMANA

# TODO 1: Reutilizar el archivero
archivero = [
    {"nombre": "Ana López", "zona": "Carpa de prensa"},
    {"nombre": "Diego Ruiz", "zona": "Backstage"},
    {"nombre": "Mara Soto", "zona": "Zona VIP"}
]

# TODO 2: Imprimir el encabezado
print("=== ACREDITACIONES SONIDOLIBRE 2026 ===")

# TODO 3: Recorrer la lista con un for
for acreditado in archivero:
    print(f"→ {acreditado['nombre']} | Zona: {acreditado['zona']}")

# TODO 4: Imprimir el total de acreditados
print(f"Total acreditados: {len(archivero)}")