# DRILL 3: LAS MESAS DE VALENTINA

# TODO 1: Importa el módulo 'math' al inicio del archivo.

import math


# TODO 2: Define las variables:
#   - asistentes_vip = 487
#   - capacidad_mesa = 8
#   - kilos_carne = 120
#   - peso_porcion = 0.25

asistentes_vip = 487
capacidad_mesa = 8
kilos_carne = 120
peso_porcion = 0.25


# TODO 3: Calcula cuántas mesas se necesitan usando math.ceil()
# (redondea hacia arriba para que NADIE se quede parado).
# Guarda el resultado en 'mesas_necesarias'.

mesas_necesarias = math.ceil(asistentes_vip / capacidad_mesa)


# TODO 4: Calcula cuántas porciones completas salen usando math.floor()
# (redondea hacia abajo porque las porciones incompletas no cuentan).
# Guarda el resultado en 'porciones_servibles'.

porciones_servibles = math.floor(kilos_carne / peso_porcion)


# TODO 5: Imprime ambos resultados con f-strings:
# "Mesas a comprar: [mesas_necesarias]"
# "Porciones servibles: [porciones_servibles]"

print(f"Mesas a comprar: {mesas_necesarias}")
print(f"Porciones servibles: {porciones_servibles}")