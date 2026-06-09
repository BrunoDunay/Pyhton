# CALIBRACIÓN — observa cómo se comporta random

# TODO 1: Importa el módulo random.
import random

# TODO 2: Genera un entero aleatorio entre 1 y 20.
numero = random.randint(1, 20)
print(numero)

# TODO 3: Elegir un emoji al azar.
emojis = ["🐶", "🐱", "🐰", "🦊"]
emoji_elegido = random.choice(emojis)
print(emoji_elegido)

# TODO 4: Mezclar los días de la semana.
dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
random.shuffle(dias)
print(dias)