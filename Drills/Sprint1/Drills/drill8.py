# DRILL 8: LOS AÑOS DEL FESTIVAL DE DON BETO

# TODO 1: Usa input() con int() para pedir el año de la primera edición
# del festival y guárdalo en una variable llamada 'anio_fundacion'.
anio_fundacion = int(input("Ingresa el año de la primera edición del festival: "))

# TODO 2: Calcula cuántos años lleva el festival en pie
# restando el año de fundación al año actual (2026).
# Guarda el resultado en una variable llamada 'anos_activo'.
anos_activo = 2026 - anio_fundacion

# TODO 3: Usa una f-string para imprimir el mensaje del cartel.
# Ejemplo de salida:
# "SonidoLibre: [anos_activo] años de música independiente."
print(f"SonidoLibre: {anos_activo} años de música independiente.")