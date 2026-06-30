import math

tareas = []
OPCIONES_VALIDAS = ("1", "2", "3", "4", "5", "6")

def mostrar_menu():
    print("\n=== Gestor de Tareas ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Ordenar A-Z")
    print("5. Resúmen (días mínimos)")
    print("6. Salir")

def listar_tareas(lista):
    if len(lista) == 0:
        print("No hay tareas registradas.")
    else:
        print("\n=== Lista de Tareas ===")
        numero = 1
        for tarea in lista:
            print(f"{numero}. {tarea}")
            numero += 1

def resumen(lista, por_dia):
    total = len(lista)
    if total == 0:
        print("No hay tareas registradas.")
    else:
        dias = math.ceil(total / por_dia)
        print(f"\n=== Resumen de Tareas ===")
        print(f"Tareas: {total} | Cerramdo {por_dia}/día -> Días mínimos: {dias}") 

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion not in OPCIONES_VALIDAS:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if opcion == "1":
        print("\n=== Agregar Tarea ===")
        tarea = input("Ingrese la descripción de la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada exitosamente. Total de tareas:", len(tareas))
    
    elif opcion == "2":
        print("\n=== Listar Tareas ===")
        listar_tareas()

    elif opcion == "3":
        print("\n=== Eliminar Tarea ===")

    elif opcion == "4":
        print("\n=== Ordenar Tareas A-Z ===")
        listar_tareas(sorted(tareas))

    elif opcion == "5":
        print("\n=== Resumen de Tareas ===")
        por_dia = int(input("Ingrese la cantidad de tareas que puede cerrar por día: "))
        resumen(tareas, por_dia)

    elif opcion == "6":
        print("Saliendo del programa...")
        break
        
    




