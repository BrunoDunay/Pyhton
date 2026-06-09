# DRILL 2: EL DETECTOR DE TIPOS DE LUCÍA

# TODO 1: Usa input() para pedir el nombre del medio de comunicación.
# Guárdalo en una variable llamada 'nombre_medio'.
# Usa print(type(nombre_medio)) para mostrar su tipo de dato.
nombre_medio = input("Ingresa el nombre del medio de comunicación: ")
print(type(nombre_medio))

# TODO 2: Usa input() para pedir el número de credencial de prensa.
# Guárdalo en una variable llamada 'num_credencial'.
# Usa print(type(num_credencial)) para mostrar su tipo de dato.
num_credencial = input("Ingresa el número de credencial de prensa: ")
print(type(num_credencial))

# TODO 3: Imprime un mensaje que confirme lo que Lucía sospechaba:
# que ambos datos llegaron como texto aunque uno parezca un número.
# Usa una f-string para el mensaje.
print(f"Tanto '{nombre_medio}' como '{num_credencial}' fueron guardados como texto (str).")