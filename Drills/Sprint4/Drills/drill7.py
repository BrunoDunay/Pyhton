# DRILL 2: LA CAJA FUERTE DE MATEO

# TODO 1: Crea una tupla llamada 'config_escenario' con tres valores
# en este orden: 440 (frecuencia base en Hz), 8 (canales), 2000 (potencia en watts).

config_escenario = (440, 8, 2000)


# TODO 2: Imprime cada valor accediendo por índice:
# "Frecuencia base: [valor] Hz"
# "Canales: [valor]"
# "Potencia máxima: [valor] W"

print(f"Frecuencia base: {config_escenario[0]} Hz")
print(f"Canales: {config_escenario[1]}")
print(f"Potencia máxima: {config_escenario[2]} W")


# TODO 3: Intenta modificar config_escenario[0] = 880
# Comenta la línea con # cuando hayas visto el error.

# config_escenario[0] = 880


# TODO 4: Imprime el tipo de dato de la variable usando type().
# Confirma que dice <class 'tuple'>.

print(type(config_escenario))