# DRILL 10: DIAGNÓSTICO DE EMERGENCIA — BASE ARES

# TODO 1: Usa input() para preguntar si hay señales vitales (si/no).
# Guárdalo en una variable llamada 'senales_vitales'.

senales_vitales = input("¿Hay señales vitales? (si/no): ")

# TODO 2: Escribe un if que verifique si senales_vitales es "si".
# Dentro de ese bloque:
#   - Usa input() con int() para pedir el nivel de consciencia (0-100).
#   - Escribe un if/elif/else con tres diagnósticos:
#     * Consciencia >= 70: Estable, en observación.
#     * Consciencia >= 30: Moderado, monitoreo intensivo.
#     * Cualquier otro caso: Crítico, requiere intervención inmediata.

if senales_vitales == "si":
    consciencia = int(input("Ingresa el nivel de consciencia (0-100): "))

    if consciencia >= 70:
        print("Estable, en observación.")
    elif consciencia >= 30:
        print("Moderado, monitoreo intensivo.")
    else:
        print("Crítico, requiere intervención inmediata.")

# TODO 3: En el else del if exterior (cuando no hay señales vitales):
# Imprime: "Sin respuesta — activar protocolo de emergencia."

else:
    print("Sin respuesta — activar protocolo de emergencia.")