# GESTOR DE INCIDENTES — SonidoLibre
# Un sistema básico para registrar y resolver incidentes técnicos.

incidentes = []

# TODO 1: Agrega los siguientes 3 incidentes a la lista con append():
# "microfono escenario principal sin señal"
# "generador zona VIP con fluctuación"
# "pantalla LED intermitente"

incidentes.append("microfono escenario principal sin señal")
incidentes.append("generador zona VIP con fluctuación")
incidentes.append("pantalla LED intermitente")

# TODO 2: Imprime la lista completa y el número de incidentes.

print("Lista de incidentes:", incidentes)
print("Número de incidentes:", len(incidentes))

# TODO 3: Sofía resuelve el primer incidente. Elimínalo con pop(0)
# y guarda el resultado en una variable. Imprime qué incidente se resolvió.

incidente_resuelto = incidentes.pop(0)
print("Incidente resuelto:", incidente_resuelto)

# TODO 4: Llega un incidente nuevo: "cable de poder roto en escenario 2".
# Agrégalo. Imprime la lista actualizada.

incidentes.append("cable de poder roto en escenario 2")
print("Lista actualizada:", incidentes)

# TODO 5: El equipo busca si "generador zona VIP con fluctuación" sigue abierto.
# Usa "in" para verificarlo e imprime un mensaje según el resultado.

if "generador zona VIP con fluctuación" in incidentes:
    print("El incidente sigue abierto.")
else:
    print("El incidente ya fue resuelto.")

# TODO 6: Imprime todos los incidentes abiertos con un for loop.
# Formato: "→ [incidente]" por cada uno.

for incidente in incidentes:
    print("→", incidente)