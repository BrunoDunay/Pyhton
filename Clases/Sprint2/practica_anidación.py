print(" Evaluación de Crédito Empresarial ")

ingresos = float(input("Ingresa los ingresos mensuales del cliente: "))
historial = input("¿El historial crediticio es bueno, regular o malo?: ")
anios_empleo = int(input("¿Cuántos años lleva en su empleo actual?: "))

# Ingresos
if ingresos >= 30000:
    print("Ingresos suficientes.")

    # Historial
    if historial == "bueno":
        print("Historial excelente.")

        # Antiguedad
        if anios_empleo >= 2:
            print("Crédito aprobado.")
        elif anios_empleo == 1:
            print("Crédito aprobado con revisión adicional.")
        else:
            print("Crédito rechazado por poca estabilidad laboral.")

    elif historial == "regular":
        print("Historial aceptable.")

        if anios_empleo >= 3:
            print("Crédito aprobado con tasa de interés alta.")
        else:
            print("Crédito rechazado por riesgo medio.")

    else:
        print("Crédito rechazado por mal historial crediticio.")

elif ingresos >= 15000:
    print("Ingresos mínimos detectados.")

    if historial == "bueno":
        print("Puede aplicar a un microcrédito.")
    else:
        print("No cumple con los requisitos para financiamiento.")

else:
    print("Ingresos insuficientes.")