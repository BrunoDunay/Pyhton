# DRILL 5: EL FRENO DE EMERGENCIA DE REGINA

# TODO 1: Define password_correcto = "sonidolibre25".
password_correcto = "sonidolibre25"

# TODO 2: Crea un bucle infinito intencional con 'while True:'.
while True:

    # TODO 3: Dentro del bucle, pide el intento.
    intento = input("Contraseña de la sala de comunicaciones: ")

    # TODO 4: Si el intento es correcto, rompe el ciclo.
    if intento == password_correcto:
        break

# TODO 5: Fuera del bucle, imprime el mensaje final.
print("Acceso a comunicaciones autorizado.")