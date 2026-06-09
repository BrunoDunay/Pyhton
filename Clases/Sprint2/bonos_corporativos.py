#Divide por categorías, evalua años y desempeño del empleado para asignar un porcentaje de bono

categoría = input("Ingrese la categoría del empleado (A, B, C): ").upper()
anos_servicio = int(input("Ingrese los años de servicio del empleado: "))
evaluacion = float(input("Ingrese la evaluación de desempeño del empleado (0-100): "))

if categoría == "A":
    if anos_servicio > 5:
        if evaluacion >= 80:
            print("El bono asignado es del 20% del salario.")
        else: 
            print("El bono asignado es del 10% del salario.")
    else:
        print("Sin eligibilidad para bono.")
elif categoría == "B":
    if evaluacion >= 90:
        print("El bono asignado es del 15% del salario.")
    else:
        print("El bono asignado es del 5% del salario.")
else:
    print("Sin eligibilidad para bono, categoría sin esquema.")
