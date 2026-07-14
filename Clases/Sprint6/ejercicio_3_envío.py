#1 Define una función llamada calcular_envio(peso, distancia) que reciba:

#  peso: peso del paquete en kilogramos.
#  distancia: distancia del envío en kilómetros.
#  La función deberá calcular el costo con las siguientes reglas:
#  El costo base es de $50.
#  Se cobran $8 por cada kilogramo.
#  Se cobran $0.75 por cada kilómetro.
#  La función debe devolver el costo total.

def calcular_envio(peso, distancia):
    costo_base = 50
    costo_por_peso = 8 * peso
    costo_por_distancia = 0.75 * distancia
    costo_total = costo_base + costo_por_peso + costo_por_distancia
    return costo_total

# Ejemplo

print("El costo del envío es:")
print(calcular_envio(20, 100))


