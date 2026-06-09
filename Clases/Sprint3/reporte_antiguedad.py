anio_corte = 2025
anio_ingreso = int(input("¿Cuál es tu año de ingreso? "))

print(f"Reporte de antigüedad al año de corte: {anio_corte}\n")

if 2018 <= anio_ingreso <= 2025:
    antiguedad = anio_corte - anio_ingreso
    print(f"Año de ingreso: {anio_ingreso}, Antigüedad: {antiguedad} años")
else:
    print("Año de ingreso no válido. Por favor, ingresa un año entre 2018 y 2025.")


print("\nFechas de pago quincenales\n")

for dia_anio in range(15,361,15):
    pago = pago + 1
    print(f"PAgo programado: dia {dia_anio}, pago número {pago}")
