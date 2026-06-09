# DRILL 2: LA FICHA DE PATROCINADORES

# TODO 1: Crea las siguientes variables:
# 'nombre_festival' con "SonidoLibre"
# 'anio' con 2026
# 'anos_activo' con 25
# 'patrocinador' con el nombre de un patrocinador ficticio

nombre_festival = "SonidoLibre"
anio = 2026
anos_activo = 25
patrocinador = "AudioMax"


# TODO 2: Usa una f-string para construir el mensaje

print(f"Estimado {patrocinador}: {nombre_festival} celebra {anos_activo} años en su edición {anio}. Queremos que seas parte de esto.")


# TODO 3: Cambia el valor de la variable 'patrocinador' a otro nombre.
# Vuelve a llamar el mensaje sin tocar el print().

patrocinador = "SoundWave"

print(f"Estimado {patrocinador}: {nombre_festival} celebra {anos_activo} años en su edición {anio}. Queremos que seas parte de esto.")