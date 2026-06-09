# DRILL 3: PROTOCOLO DE SALIDA AL EXTERIOR — BASE ARES

# TODO 1: Usa input() con float() para pedir el nivel de oxígeno.
# Guárdalo en una variable llamada 'oxigeno'.

oxigeno = float(input("Ingresa el nivel de oxígeno: "))


# TODO 2: Usa input() con float() para pedir el nivel de radiación.
# Guárdalo en una variable llamada 'radiacion'.

radiacion = float(input("Ingresa el nivel de radiación: "))


# TODO 3: Crea una variable 'autorizar_salida' que sea True
# solo si el oxígeno es mayor o igual a 18 AND la radiación es menor a 65.

autorizar_salida = oxigeno >= 18 and radiacion < 65


# TODO 4: Usa print() con f-string para mostrar el resultado.
# Ejemplo de salida:
# "¿Seguro salir al exterior?: [autorizar_salida]"

print(f"¿Seguro salir al exterior?: {autorizar_salida}")