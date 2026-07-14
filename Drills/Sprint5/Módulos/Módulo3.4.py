# Caso 4: F-Strings Avanzados

print("=== FORMATEO PROFESIONAL ===\n")

recluta = {
  "nombre": "Carlos Ruiz",
  "puntos": 1234,
  "precision": 0.8567,
  "rango": "aprendiz"
}

# TODO 1: Imprime un reporte BÁSICO con cuatro líneas:
# "Nombre: [nombre]"
# "Puntos: [puntos]"
# "Precisión: [precision]"
# "Rango: [rango]"

print(f"Nombre: {recluta['nombre']}")
print(f"Puntos: {recluta['puntos']}")
print(f"Precisión: {recluta['precision']}")
print(f"Rango: {recluta['rango']}")


# TODO 2: Imprime un reporte PROFESIONAL usando alineación y formatos:
# - Label a la izquierda en ancho 20 (:<20)
# - Nombre con su rango en MAYÚSCULAS (rango.upper())
# - Puntos con separador de miles (:,)
# - Precisión como porcentaje con 2 decimales (:.2%)
# - Precisión como decimal con 2 decimales (:.2f)

print("\n--- REPORTE PROFESIONAL ---")

print(f"{'Nombre':<20}{recluta['nombre']} - {recluta['rango'].upper()}")
print(f"{'Puntos':<20}{recluta['puntos']:,}")
print(f"{'Precisión %':<20}{recluta['precision']:.2%}")
print(f"{'Precisión decimal':<20}{recluta['precision']:.2f}")


# TODO 3: Imprime el título "REPORTE DE RECLUTA" centrado en ancho 50
# usando "=" como carácter de relleno (:=^50).

print(f"\n{'REPORTE DE RECLUTA':=^50}")


# TODO 4: Imprime una tabla de estadísticas:
# Encabezado: "Métrica" (izquierda 15), "Valor" (derecha 10), "Estado" (derecha 10)
# Separadora de "-" con el ancho total correcto.
# Tres filas: Puntos (con :,), Precisión (con :.1%), Rango (con .title()).

print("\nTabla de estadísticas")
print(f"{'Métrica':<15}{'Valor':>10}{'Estado':>10}")
print("-" * 35)

print(f"{'Puntos':<15}{recluta['puntos']:>10,}{'OK':>10}")
print(f"{'Precisión':<15}{recluta['precision']:>10.1%}{'OK':>10}")
print(f"{'Rango':<15}{recluta['rango'].title():>10}{'OK':>10}")