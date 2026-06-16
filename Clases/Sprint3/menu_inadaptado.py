# REQUERIMIENTOS OBLIGATORIOS:
# 1. Archivo guardado como menu_inadaptado.py en clase-06/
# 2. El menú muestra EXACTAMENTE estas 4 opciones, numeradas:
#        1. Crear
#        2. Ver lista
#        3. Actualizar
#        4. Salir
# 3. Motor while True: como único bucle del programa
# 4. Validación de opción inválida con continue (mensaje + volver al menú)
# 5. Opciones 1, 2, 3 muestran mensaje placeholder:
#        "--- [Función] en construcción ---"
# 6. Opción 4 muestra "Cerrando aplicación..." y termina con break
# 7. Comparaciones del input como strings ("1", "2", "3", "4")
# 8. UN SOLO break en todo el archivo, exclusivamente en la opción 4

# CRITERIOS DE VERIFICACIÓN (correr el programa y validar):
# ☐ ¿El programa sigue corriendo después de elegir 1, 2 o 3?
# ☐ ¿El programa termina limpiamente solo con la opción 4?
# ☐ ¿Una letra (ej. "hola") muestra el mensaje de error y vuelve al menú?
# ☐ ¿Un número fuera de rango (ej. "9") muestra el mensaje de error y vuelve al menú?
# ☐ ¿Enter en blanco muestra el mensaje de error y vuelve al menú?
# ☐ ¿La opción inválida usa continue (NO break)?
# ☐ ¿Está el break únicamente en la opción 4?

while True:
    print("\n===== MENÚ INADAPTADO =====")
    print("1. Crear")
    print("2. Ver lista")
    print("3. Actualizar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if opcion == "1":
        print("--- Crear en construcción ---")

    if opcion == "2":
        print("--- Ver lista en construcción ---")

    if opcion == "3":
        print("--- Actualizar en construcción ---")

    if opcion == "4":
        print("Cerrando aplicación...")
        break