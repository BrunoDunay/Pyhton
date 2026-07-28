# DRILL 1: LA LAVADORA DE STRINGS DE LUCÍA

# TODO 1: Crea una variable llamada 'nombre_sucio'
nombre_sucio = "   dIaRiO DeL sUr   "

# TODO 2: Quitar los espacios al inicio y al final
sin_espacios = nombre_sucio.strip()

# TODO 3: Convertir todo a minúsculas
normalizado = sin_espacios.lower()

# TODO 4: Dar formato de título
limpio = normalizado.title()

# TODO 5: Imprimir cada transformación
print(f"Original: '{nombre_sucio}'")
print(f"Sin espacios: '{sin_espacios}'")
print(f"Normalizado: '{normalizado}'")
print(f"Limpio: '{limpio}'")