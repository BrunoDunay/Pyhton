# DRILL 5: REFACTORIZANDO EL ESPAGUETI DE SOFÍA

# TODO 1
def pedir_dato_limpio(etiqueta):
    dato = input(etiqueta)
    return dato.strip().title()

# TODO 2
nombre_artista = pedir_dato_limpio("Nombre del artista: ")
medio_prensa = pedir_dato_limpio("Nombre del medio de prensa: ")
zona_asignada = pedir_dato_limpio("Zona asignada: ")

# TODO 3
print(f"Artista: {nombre_artista}")
print(f"Medio de prensa: {medio_prensa}")
print(f"Zona asignada: {zona_asignada}")

# TODO 4
# Reflexión:
# La función evitó repetir 3 veces:
# dato = input(...)
# dato.strip()
# dato.title()
#
# En lugar de escribir aproximadamente 9 líneas repetidas,
# solo se creó la lógica una vez y se reutilizó con 3 llamadas.