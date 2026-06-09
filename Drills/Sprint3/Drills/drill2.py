# DRILL 2: LA VALIDACIÓN OBSTINADA DE VALENTINA

# TODO 1: Pide la palabra clave y guárdala en 'palabra'.
palabra = input("Palabra clave del día: ")

# TODO 2: Repite mientras la palabra sea distinta de "area-tecnica".
while palabra != "area-tecnica":
    # TODO 3: Vuelve a pedir la palabra.
    palabra = input("Incorrecto. Intenta de nuevo: ")

# TODO 4: Fuera del bucle, imprime el mensaje de acceso.
print("Acceso a zona técnica concedido.")