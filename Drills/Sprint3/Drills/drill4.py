# DRILL 4: EL MINI-JUEGO DE LUCÍA

# TODO 1: Importa random.
import random

# TODO 2: Guarda en 'secreto' un número aleatorio entre 1 y 10.
secreto = random.randint(1, 10)

# TODO 3: Pide el primer intento.
intento = int(input("Adivina el número entre 1 y 10: "))

# TODO 4: Usa un while que repita MIENTRAS intento sea distinto de secreto.
while intento != secreto:
    # TODO 5: Dentro del bucle, vuelve a pedir un intento.
    intento = int(input("No es ese. Intenta de nuevo: "))

# TODO 6: Fuera del bucle, imprime el mensaje de éxito.
print(f"¡Acertaste! El número era {secreto}.")