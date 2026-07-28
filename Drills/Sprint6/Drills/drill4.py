# DRILL 4: EL ESPEJISMO DEL SCOPE

# TODO 1: Variable global
asistentes_totales = 400

# TODO 2: Función con variable local
def agregar_asistentes():
    asistentes_totales = 50
    print(f"Dentro de la función: {asistentes_totales}")

# TODO 3: Llamar a la función
agregar_asistentes()

# TODO 4: Imprimir variable global
print(f"Fuera de la función: {asistentes_totales}")