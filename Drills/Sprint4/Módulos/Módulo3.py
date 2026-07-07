# COMPARACIÓN: LISTAS VS TUPLAS


# ===== PARTE 1: LISTAS (modificables) =====

# TODO 1: Imprime un encabezado "=== LISTAS (Modificables) ===".

print("=== LISTAS (Modificables) ===")


# TODO 2: Crea una lista 'tareas' con tres strings:
#   "estudiar", "ejercicio", "compras".
# Imprímela con f-string para ver el estado inicial.

tareas = ["estudiar", "ejercicio", "compras"]
print(f"Estado inicial: {tareas}")


# TODO 3: Usa .append("leer") para agregar una cuarta tarea.
# Imprime la lista para verificar el cambio.

tareas.append("leer")
print(f"Lista después de agregar una tarea: {tareas}")


# TODO 4: Reemplaza la tarea en el índice 1 por "yoga" (asignación directa
# con corchetes: tareas[1] = "yoga"). Imprime la lista.

tareas[1] = "yoga"
print(f"Lista después de reemplazar una tarea: {tareas}")


# TODO 5: Quita "compras" con .remove("compras"). Imprime la lista resultante.

tareas.remove("compras")
print(f"Lista después de eliminar una tarea: {tareas}")


# ===== PARTE 2: TUPLAS (inmutables) =====

# TODO 6: Imprime un encabezado "=== TUPLAS (Inmutables) ===".

print("\n=== TUPLAS (Inmutables) ===")


# TODO 7: Crea una tupla 'config' con tres valores (servidor, puerto, ambiente):
#   "localhost", 8080, "producción".
# Imprímela.

config = ("localhost", 8080, "producción")
print(f"Configuración: {config}")


# TODO 8: Imprime cada elemento por separado accediendo por índice
# (config[0], config[1], config[2]) con f-string.

print(f"Servidor: {config[0]}")
print(f"Puerto: {config[1]}")
print(f"Ambiente: {config[2]}")


# TODO 9: Desempaqueta la tupla en tres variables nuevas (servidor,
# puerto, ambiente) en una sola línea: 'servidor, puerto, ambiente = config'.
# Imprime las tres en un f-string para confirmar que el desempaque funcionó.

servidor, puerto, ambiente = config
print(f"Servidor: {servidor}, Puerto: {puerto}, Ambiente: {ambiente}")


# TODO 10: Para "cambiar" el puerto a 9000 SIN romper la inmutabilidad,
# crea una NUEVA tupla 'config_nueva' tomando los valores actuales
# de config y reemplazando solo el puerto (pista: config[0], 9000, config[2]).
# Imprime la nueva tupla.

config_nueva = (config[0], 9000, config[2])
print(f"Nueva configuración: {config_nueva}")


# ===== PARTE 3: CASOS DE USO =====

# TODO 11: Imprime "=== CASOS DE USO ===".

print("\n=== CASOS DE USO ===")


# TODO 12: Crea una TUPLA 'ubicacion' con dos floats representando
# coordenadas GPS (por ejemplo, (19.4326, -99.1332) para CDMX).
# Decide POR QUÉ tupla y no lista: las coordenadas de un punto fijo
# no cambian. Imprímela.

ubicacion = (19.4326, -99.1332)
print(f"Ubicación: {ubicacion}")


# TODO 13: Crea una LISTA 'compras' con dos strings ("leche", "pan").
# Agrégale "huevos" con .append(). Es lista porque cambia. Imprímela.

compras = ["leche", "pan"]
compras.append("huevos")
print(f"Lista de compras: {compras}")


# TODO 14: Crea una TUPLA 'DIAS' con los 7 días abreviados de la semana
# ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"). En mayúsculas porque
# es una constante. Imprime el día en posición 2 con DIAS[2].

DIAS = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
print(f"Día en la posición 2: {DIAS[2]}")