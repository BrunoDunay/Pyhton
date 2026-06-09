# ENTREGABLE SPRINT 1: BIENVENIDA INTERACTIVA

print("--- SISTEMA DE INGRESO INADAPTADOS ---")

# TODO 1: Usa input() para pedir el nombre del usuario y guárdalo en una variable.
nombre = input("Ingresa tu nombre: ")

# TODO 2: Usa input() para pedir la ciudad de origen del usuario.
ciudad = input("Ingresa tu ciudad de origen: ")

# TODO 3: Pide el año de nacimiento del usuario.
# ¡CUIDADO! Aplica el casting con int() envolviendo el input para que sea un número.
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# TODO 4: Calcula la edad aproximada restándole el año de nacimiento a 2026.
# (Ej. edad = 2026 - año_nacimiento)
edad = 2026 - anio_nacimiento

# TODO 5: Usa un print() con f-string para mostrar un resumen espectacular.
# Debe decir algo como: "Bienvenido [nombre] de [ciudad]. Tienes [edad] años, ¡a hackear!"
print(f"Bienvenido {nombre} de {ciudad}. Tienes {edad} años, ¡a hackear!")