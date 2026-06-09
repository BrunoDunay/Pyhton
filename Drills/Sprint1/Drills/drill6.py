# DRILL 6: EL REGISTRO DE BANDAS DE MATEO

# TODO 1: Usa input() para pedir el nombre de la banda
# y guárdalo en una variable llamada 'nombre_banda'.
nombre_banda = input("Ingresa el nombre de la banda: ")

# TODO 2: Usa input() para pedir el escenario asignado
# y guárdalo en una variable llamada 'escenario'.
escenario = input("Ingresa el escenario asignado: ")

# TODO 3: Usa input() para pedir el horario de prueba de sonido
# y guárdalo en una variable llamada 'horario'.
horario = input("Ingresa el horario de prueba de sonido: ")

# TODO 4: Usa una f-string para imprimir un resumen de registro.
# Ejemplo de salida:
# "Registro confirmado: [nombre_banda] — Escenario [escenario] — [horario]"
print(f"Registro confirmado: {nombre_banda} — Escenario {escenario} — {horario}")