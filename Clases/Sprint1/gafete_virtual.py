# ==========================================
# GAFETE VIRTUAL - INDPTDOS
# Autor: [TuNombre]
# Clase: 2 - Sprint 1
# ==========================================

# Paso 1: Pedir los 4 datos. Antes de teclear, deciden conmigo: ¿Qué tipo de dato es cada uno?
# Nombre
# Año
# Sueldo
# Ciudad

# Paso 2: calcular la edad. Estamos en 2026, así que edad = 2026 - año de nacimiento.
# Paso 3: Imprimir el gafete.

nombre = input("Ingresa tu nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
sueldo = float(input("Ingresa tu sueldo: "))
ciudad = input("Ingresa tu ciudad: ")

edad = 2026 - anio_nacimiento
sueldo_anual = sueldo * 12

print("=" * 40)
print(f"--- GAFETE VIRTUAL ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Sueldo: ${sueldo:.2f}")
print(f"Ciudad: {ciudad}")
print(f" Tu sueldo anual es: ${sueldo_anual:.2f}")
print("=" * 40)
