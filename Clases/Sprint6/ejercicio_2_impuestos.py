tasa_impuesto = 0.10

def calcular_tasa():
    tasa_impuesto = 0.12
    return tasa_impuesto

calcular_tasa()
print(f"La tasa de impuesto es: {tasa_impuesto}")

def calcular_pago_bruto(sueldo_base, bono):
    bruto = sueldo_base + bono
    return bruto

def calcular_impuesto(monto, tasa):
    return monto * tasa

bruto = calcular_pago_bruto(30000, 5000)   # 35000
impuesto = calcular_impuesto(bruto, 0.12)  # 4200.0
print(f"Impuesto a retener: ${impuesto}")


