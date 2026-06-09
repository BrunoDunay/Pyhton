
# ESPECIFICACIÓN — procesador_lotes.py

# CONTEXTO
# Trabajas en el área de procesamiento batch de una financiera. Cada noche,
# el sistema procesa N lotes pendientes. Cada lote contiene M transacciones
# del mismo monto. Tu programa debe procesar todos los lotes, acumular el
# total, y emitir una alerta cada vez que el acumulado cruza el umbral.

# VARIABLES DE ENTRADA (declaradas al inicio del archivo — NO uses input())
#   lotes_pendientes        = 5         # número de lotes a procesar
#   transacciones_por_lote  = 3         # transacciones que contiene cada lote
#   monto_por_transaccion   = 1200.50   # monto fijo de cada transacción
#   umbral_alerta           = 10000     # umbral para emitir alerta

# COMPORTAMIENTO ESPERADO
#   1. Procesa los lotes uno por uno con un loop `while`.
#   2. Por cada lote, procesa sus transacciones con un loop `for` + `range()`.
#   3. Imprime una línea por cada transacción:
#      "[Lote X | Trans Y] Monto: $1200.5 | Acumulado: $XXXX.XX"
#   4. Cada vez que el acumulado supere el umbral_alerta y la línea anterior
#      no lo superaba, imprime UNA SOLA VEZ:
#      "[ALERTA] Umbral de $10000 excedido en lote X, transacción Y"
#   5. Al finalizar todos los lotes, imprime un resumen:
#      "Total procesado: $XXXXX.XX"
#      "Lotes procesados: X"
#      "Transacciones procesadas: X"

# REGLAS DE CONSTRUCCIÓN
#   - El `while` exterior controla los lotes pendientes.
#   - El `for` interior controla las transacciones dentro del lote.
#   - PROHIBIDO usar: break, continue, while True, def, return, listas, dicts.
#   - Numera los lotes empezando en 1, no en 0.
#   - Numera las transacciones empezando en 1, no en 0.

# VALORES ESPERADOS (con la configuración base)
#   - Total procesado: $18007.5
#   - Lotes procesados: 5
#   - Transacciones procesadas: 15
#   - La alerta debe aparecer UNA SOLA VEZ (cuando se cruza por primera vez)

# Variables de entrada
lotes_pendientes        = 5         # número de lotes a procesar
transacciones_por_lote  = 3         # transacciones que contiene cada lote
monto_por_transaccion   = 1200.50   # monto fijo de cada transacción
umbral_alerta           = 10000     # umbral para emitir alerta

# Estado del procesamiento
acumulado = 0
lotes_procesados = 0
transacciones_procesadas = 0
alerta_emitida = False

# Procesamiento de lotes
while lotes_procesados < lotes_pendientes:
    lotes_procesados = lotes_procesados + 1
    lote_actual = lotes_procesados
    for transacción in range(transacciones_por_lote):
        transacciones_procesadas = transacciones_procesadas + 1
        transacción_actual = transacción + 1
        acumulado = acumulado + monto_por_transaccion
        if acumulado > umbral_alerta and not alerta_emitida:
            print(f"[ALERTA] Umbral de ${umbral_alerta} excedido en lote {lote_actual}, transacción {transacción_actual}")
            alerta_emitida = True
        print(f"[Lote {lote_actual} | Trans {transacción_actual}] Monto: ${monto_por_transaccion:.2f} | Acumulado: ${acumulado:.2f}")
    print(f"Lote {lote_actual} procesado")
    
print(f"Total procesado: ${acumulado:.2f}")
print(f"Lotes procesados: {lotes_procesados}")
print(f"Transacciones procesadas: {transacciones_procesadas}")

        

