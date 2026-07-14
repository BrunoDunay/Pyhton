# DRILL 4: NOMBRES POR UN LADO, ZONAS POR OTRO

# TODO 1: Crea un diccionario llamado 'acreditaciones' con:
# "Ana López" → "Carpa de prensa"
# "Diego Ruiz" → "Backstage"
# "Mara Soto" → "Zona VIP"

acreditaciones = {
    "Ana López": "Carpa de prensa",
    "Diego Ruiz": "Backstage",
    "Mara Soto": "Zona VIP"
}

# TODO 2: Usa .keys() para imprimir solo los nombres acreditados.

print("Nombres acreditados:")
for nombre in acreditaciones.keys():
    print(nombre)

# TODO 3: Usa .values() para imprimir solo las zonas asignadas.

print("\nZonas asignadas:")
for zona in acreditaciones.values():
    print(zona)

# TODO 4: Usa una f-string para imprimir un resumen con el total de
# acreditaciones (usa len()).
# Ejemplo:
# "Total de acreditaciones procesadas: 3"

print(f"\nTotal de acreditaciones procesadas: {len(acreditaciones)}")