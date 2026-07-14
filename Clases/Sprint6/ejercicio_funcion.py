
def calcular_precio_final(precio_base, porcentaje_descuento):
    descuento = precio_base * porcentaje_descuento
    precio_final = precio_base - descuento
    return precio_final

print(calcular_precio_final(100, 0.1))  # Salida: 90.0
print(calcular_precio_final(200, 0.2))  # Salida: 160.0
print(calcular_precio_final(300, 0.3))  # Salida: 210.0