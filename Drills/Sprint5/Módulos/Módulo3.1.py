# Caso 1: Normalizar Nombre de Usuario

print("=== NORMALIZACIÓN DE NOMBRES ===\n")

nombres_sucios = [
  "  JUAN PÉREZ  ",
  "ana maría lópez",
  "CARLOS   RUIZ",
  "  María   "
]

print("--- NOMBRES SUCIOS ---")
for nombre in nombres_sucios:
  print(f"'{nombre}'")

print("\n--- NOMBRES LIMPIOS ---")
for nombre_sucio in nombres_sucios:
  # TODO: Limpia nombre_sucio encadenando .strip(), .lower() y .title().
  # Guarda el resultado en 'nombre_limpio' e imprímelo entre comillas simples.
  nombre_limpio = nombre_sucio.strip().lower().title()
  print(f"'{nombre_limpio}'")

# TODO: Toma el string "  JUAN   PÉREZ  " y guárdalo en 'nombre_usuario'.
# Aplica .strip().title() y guarda en 'nombre_final'.
# Usa 'if "  " in nombre_final' para detectar espacios dobles internos.
# Si los hay, usa .split() y " ".join() para eliminarlos.
# Imprime: "Nombre guardado en BD: '[nombre_final]'"

nombre_usuario = "  JUAN   PÉREZ  "
nombre_final = nombre_usuario.strip().title()

if "  " in nombre_final:
    nombre_final = " ".join(nombre_final.split())

print(f"Nombre guardado en BD: '{nombre_final}'")