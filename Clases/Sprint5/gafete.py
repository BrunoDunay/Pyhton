# =====================================================================
#  gafete_referencia.py
#  Sprint 5 - Clase 10 - Ejercicio corto "El Gafete"
# =====================================================================

registro_crudo = "  MARA   ibarra ,  saLUD  , 133750.5  "

# Paso 1: partir por la coma
pedazos = registro_crudo.split(",")
# ['  MARA   ibarra ', '  saLUD  ', ' 133750.5  ']

# Pasos 2-4: limpiar cada campo (reasignando SIEMPRE)
nombre = pedazos[0].strip()
nombre = nombre.replace("   ", " ")  # colapsa los 3 espacios internos
nombre = nombre.title()  # Mara Ibarra

area = pedazos[1].strip().title()  # Salud

# Paso 5: el salario llega como texto; limpiar y LUEGO convertir
salario = float(pedazos[2].strip())  # 133750.5

# Paso 6: el gafete
print("=" * 50)
print(f" NOMBRE: {nombre}")
print(f" AREA:   {area}")
print(f" SALARIO: {salario:>14,.2f}")
print("=" * 50)

# ---------------------------------------------------------------------
#  STRETCH - referencia
# ---------------------------------------------------------------------
print()
print("--- stretch: lote de gafetes ---")
registros = [
    "  MARA   ibarra ,  saLUD  , 133750.5  ",
    "ana torres,finanzas,28500",
    "  LUIS QUINTERO  , LOGISTICA , 19200.0 ",
]

for linea in registros:
    pedazos = linea.split(",")
    nombre = pedazos[0].strip().replace("   ", " ").title()
    area = pedazos[1].strip().title()
    salario = float(pedazos[2].strip())

    print("=" * 50)
    print(f" NOMBRE: {nombre}")
    print(f" AREA:   {area}")
    print(f" SALARIO: {salario:>14,.2f}")
    print("=" * 50)