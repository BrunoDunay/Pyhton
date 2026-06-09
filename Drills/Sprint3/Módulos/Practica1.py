# PROCESADOR DE LOTES — SonidoLibre
# Completa los TODOs para que el sistema procese los lotes correctamente.

lotes_pendientes = 3
elementos_por_lote = 4
lote_actual = 1

# Guardamos el valor original para calcular el total al final
lotes_pendientes_original = lotes_pendientes

# TODO 1: Escribe el bucle while que continúe mientras haya lotes pendientes.
while lotes_pendientes > 0:

    # TODO 2: Imprime el inicio de cada lote con un f-string.
    print(f"=== Procesando lote {lote_actual} de {lotes_pendientes_original} ===")

    # TODO 3: Usa un bucle for con range() para procesar cada elemento del lote.
    for ticket in range(1, elementos_por_lote + 1):
        print(f"  Ticket {ticket}/{elementos_por_lote} procesado")

    # TODO 4: Actualiza el contador del while y el número de lote.
    lotes_pendientes -= 1
    lote_actual += 1

# TODO 5: Fuera de los bucles, imprime el total.
total = lotes_pendientes_original * elementos_por_lote
print(f"Todos los lotes procesados. Total de tickets: {total}")