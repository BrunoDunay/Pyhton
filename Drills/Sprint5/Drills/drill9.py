# DRILL 4: EL GRAN ARCHIVERO DE OMAR

# TODO 1: Crear una lista vacía
archivero = []

# TODO 2: Agregar tres diccionarios usando append()
archivero.append({
    "nombre": "Ana López",
    "zona": "Carpa de prensa"
})

archivero.append({
    "nombre": "Diego Ruiz",
    "zona": "Backstage"
})

archivero.append({
    "nombre": "Mara Soto",
    "zona": "Zona VIP"
})

# TODO 3: Imprimir la lista completa
print(archivero)

# TODO 4: Acceder al nombre del segundo acreditado
print(f"Segundo acreditado: {archivero[1]['nombre']}")