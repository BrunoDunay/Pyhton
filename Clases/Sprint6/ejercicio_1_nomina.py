#Módulo de nómina - Calcular pago bruto

def calcular_pago_bruto(sueldo_base, bono):
    total = sueldo_base + bono
    return total

pago = calcular_pago_bruto(20000, 2000)

print(f"El pago bruto es: {pago}")