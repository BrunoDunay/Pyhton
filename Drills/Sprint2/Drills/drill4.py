# DRILL 4: ACCESO A LA CABINA DE MANDO — BASE ARES

# TODO 1: Usa input() para pedir el comando de voz.
# Guárdalo en una variable llamada 'comando'.

comando = input("Ingresa el comando de voz: ")


# TODO 2: Crea una variable 'acceso_cabina' que sea True
# si el comando es "activar" OR si el comando es "Activar".

acceso_cabina = comando == "activar" or comando == "Activar"


# TODO 3: Usa print() con f-string para mostrar el resultado.
# Ejemplo de salida:
# "¿Comando reconocido?: [acceso_cabina]"

print(f"¿Comando reconocido?: {acceso_cabina}")