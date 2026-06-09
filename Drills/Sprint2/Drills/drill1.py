# DRILL 1: CALCULADORA DE SUMINISTROS — BASE ARES

# TODO 1: Usa input() con float() para pedir los kilos de oxígeno.
# Guárdalos en una variable llamada 'carga_a'.

carga_a = float(input("Ingresa los kilos de oxígeno: "))


# TODO 2: Usa input() con float() para pedir los litros de combustible.
# Guárdalos en una variable llamada 'carga_b'.

carga_b = float(input("Ingresa los litros de combustible: "))


# TODO 3: Usa print() con f-strings para mostrar los cuatro resultados:
# - Total: carga_a + carga_b
# - Diferencia: carga_a - carga_b
# - Rendimiento (multiplicación): carga_a * carga_b
# - Reparto por módulo (división): carga_a / carga_b

print(f"Total: {carga_a + carga_b}")
print(f"Diferencia: {carga_a - carga_b}")
print(f"Rendimiento: {carga_a * carga_b}")
print(f"Reparto: {carga_a / carga_b}")