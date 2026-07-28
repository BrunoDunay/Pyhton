# ANTES: Código espagueti con variables globales
# nombre = "Inadaptado"
# nivel = 1
# experiencia = 0
#
# def subir_nivel():
#     global nivel, experiencia
#     experiencia = 0
#     nivel += 1
#     print(f"{nombre} subió al nivel {nivel}!")

print("=== SISTEMA DE NIVELES ===\n")

# TODO 1
def crear_jugador(nombre_inicial):
    return {
        "nombre": nombre_inicial,
        "nivel": 1,
        "experiencia": 0
    }

# TODO 2
def ganar_experiencia(jugador, puntos):
    jugador["experiencia"] += puntos
    print(
        f"{jugador['nombre']} ganó {puntos} XP. "
        f"Total: {jugador['experiencia']} XP."
    )
    return jugador

# TODO 3
def subir_nivel(jugador):
    jugador["nivel"] += 1
    jugador["experiencia"] = 0
    print(f"¡{jugador['nombre']} subió al nivel {jugador['nivel']}!")
    return jugador

# TODO 4
jugador = crear_jugador("Inadaptado")

print(f"Jugador: {jugador['nombre']}")
print(f"Nivel inicial: {jugador['nivel']}")

# TODO 5
jugador = ganar_experiencia(jugador, 50)
jugador = ganar_experiencia(jugador, 100)

# TODO 6
if jugador["experiencia"] >= 100:
    jugador = subir_nivel(jugador)

# TODO 7
jugador = ganar_experiencia(jugador, 75)

print("\nEstado final del jugador:")
print(jugador)