while True:
    print("\n===== CAJERO =====")
    print("1. Consultar saldo")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion not in ["1", "2"]:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if opcion == "1":
        print("Su saldo actual es: $1000")

    if opcion == "2":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break

