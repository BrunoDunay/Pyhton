# DRILL 9: PROTOCOLO DE DAÑOS DEL CASCO — BASE ARES

# TODO 1: Usa input() con int() para pedir el porcentaje de daño en el casco.
# Guárdalo en una variable llamada 'danio'.

danio = int(input("Ingresa el porcentaje de daño del casco: "))

# TODO 2: Escribe un if/elif/elif/else con cuatro niveles de alerta:
# - Más de 90%: Nivel E (Evacuación Inmediata)
# - Más de 80%: Nivel D (Reparación Urgente)
# - Más de 70%: Nivel C (Mantenimiento)
# - Cualquier otro caso: Seguro

# TODO 3: Cada rama imprime el nivel de alerta correspondiente.

if danio > 90:
    print("Nivel E: Evacuación Inmediata")
elif danio > 80:
    print("Nivel D: Reparación Urgente")
elif danio > 70:
    print("Nivel C: Mantenimiento")
else:
    print("Seguro")