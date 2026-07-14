#Usa es_salario_valido para procesar estos 4 salarios. Por cada uno imprime
#"PROCESAR: <salario>" si es valido, o "RECHAZAR: <salario>" si no:

#  20000, 500, 200000, 250000

# Salida esperada:
 # PROCESAR: 20000
 # RECHAZAR: 500
 # PROCESAR: 200000
 # RECHAZAR: 250000


def es_salario_valido(salario):
    if 1000 <= salario <= 200000:
        return True
    else:
        return False

salarios = [20000, 500, 200000, 250000]

for salario in salarios:
    if es_salario_valido(salario):
        print(f"PROCESAR: {salario}")
    else:
        print(f"RECHAZAR: {salario}")