import math

tareas = []
OPCIONES_VALIDAS = ("1", "2", "3", "4", "5", "6")


def mostrar_menu():
    print("\n====== GESTOR DE TAREAS ======")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Eliminar Tarea")
    print("4. Ordenar A-Z")
    print("5. Resumen (días mínimos)")
    print("6. Salir")


def listar_tareas(lista):
    if len(lista) == 0:
        print("NO hay tareas registradas.")
    else:
        print("------ Tareas Pendientes ------")
        numero = 1
        for tarea in lista:
            print(f"{numero}. {tarea}")
            numero = numero + 1


def resumen(lista, por_dia):
    total = len(lista)
    if total == 0:
        print("Sin tareas: 0 días.")
    else:
        dias = math.ceil(total / por_dia)
        print(
            f"Tareas: {total} |Cerrando {por_dia}/día -> {dias} días hábiles mínimos"
        )


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n===== AGREGAR TAREA =====")
        texto = input("Describe la tarea: ")
        tareas.append(texto)
        print(f"Tarea agregada. Total: {len(tareas)}")

    elif opcion == "2":
        print("\n===== LISTAR TAREAS =====")
        listar_tareas(tareas)

    elif opcion == "3":
        print("\n===== ELIMINAR TAREA =====")
        if len(tareas) == 0:
            print("No hay tareas para eliminar")
        else:
            listar_tareas(tareas)
            numero = int(input("Número de la tarea a eliminar: "))
            indice = numero - 1
            if indice >= 0 and indice < len(tareas):
                eliminada = tareas.pop(indice)
                print(f"Tarea eliminada: {eliminada}")
            else:
                print(
                    f"Esa tarea no existe. Hay {len(tareas)} tareas (1 a {len(tareas)}). "
                )
    elif opcion == "4":
        print("\n===== ORDENAR TAREAS =====")

        tareas_ordenadas = sorted(tareas)
        listar_tareas(tareas_ordenadas)

        # listar_tareas(sorted(tareas))

    elif opcion == "5":
        print("\n===== RESUMEN TAREAS =====")
        resumen(tareas, 4)

    elif opcion == "6":
        print("\n===== SALIR =====")
        break

    else:
        print("Opción inválida. Elige del 1 al 6.")