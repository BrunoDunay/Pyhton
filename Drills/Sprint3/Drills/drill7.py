# DRILL 7: LA TABLA DE DON BETO

# TODO 1: Crear la variable precio_entrada.
precio_entrada = 250

# TODO 2: Recorrer del 1 al 10.
for num_entradas in range(1, 11):
    total = num_entradas * precio_entrada
    print(f"{num_entradas} entradas: {total} pesos")

# TODO 3: Mensaje final.
print("Tabla generada exitosamente.")