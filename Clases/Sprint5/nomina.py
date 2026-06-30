empleado = {"nombre" : "Ana García", "departamento" : "Finanzas"}

print("Procesando pago de: ", empleado["nombre"])
if empleado.get("salario") is not None:
    print("Salario a depositar: ", empleado["salario"])
