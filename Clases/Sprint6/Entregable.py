tasa_impuesto = 0.12

def calcular_pago_bruto(sueldo_base, bono):
    return sueldo_base + bono

def calcular_neto(bruto, tasa):
    impuesto = bruto * tasa
    return bruto - impuesto

def es_salario_valido(sueldo_base):
    return 8000 <= sueldo_base <= 200000

def formatear_linea(num_em, bruto, neto):
    return f"Empleado {num_em}: Bruto = ${bruto:.2f}, Neto = ${neto:.2f}"

empleados = [
    (1, 20000, 2000),
    (2, 25000, 0),
    (3, 500, 100)
]

procesados = 0
rechazados = 0
total_neto = 0

for num_em, sueldo, bono in empleados:
    if not es_salario_valido(sueldo):
        print(f"Empleado {num_em} | RECHAZADO: salario fuera del rango ({sueldo})")
        rechazados += 1
        continue
    bruto = calcular_pago_bruto(sueldo, bono)
    neto = calcular_neto(bruto, tasa_impuesto)
    print(formatear_linea(num_em, bruto, neto))
    procesados += 1
    total_neto += neto


print(f"Empleados procesados: {procesados}")
print(f"Empleados rechazados: {rechazados}")
print(f"Total neto a depositar: ${total_neto:.2f}")