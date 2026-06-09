# DRILL 7: AUTENTICACIÓN BIO-DIGITAL — BASE ARES

# TODO 1: Crea una variable 'clave_maestra' con el valor "ares2024".

clave_maestra = "ares2024"

# TODO 2: Usa input() para pedir el intento de acceso.
# Guárdalo en una variable llamada 'intento'.

intento = input("Ingresa la clave de acceso: ")

# TODO 3: Escribe un if/else:
# - Si el intento coincide con la clave maestra, imprime un mensaje de acceso concedido.
# - Si no coincide, imprime una alerta de intrusión.

if intento == clave_maestra:
    print("Acceso concedido. Bienvenido a la Base ARES.")
else:
    print("ALERTA: Intrusión detectada.")