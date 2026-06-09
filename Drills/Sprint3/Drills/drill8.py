# DRILL 8: EL ACUMULADOR DE CHECO

# TODO 1: Crear el acumulador antes del bucle.
total_asistentes = 0

# TODO 2: Recorrer las horas del 1 al 5.
for hora in range(1, 6):
    total_asistentes += hora
    print(f"Hora {hora}: total acumulado {total_asistentes}")

# TODO 3: Imprimir el total final fuera del bucle.
print(f"Total de asistentes del día: {total_asistentes} mil asistentes")