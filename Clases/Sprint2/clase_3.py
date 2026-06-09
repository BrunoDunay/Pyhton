empleado_id = input("ID empleado: ")
nivel_acceso = int(input("Nivel de acceso (1-5): "))
departamento = input("Departamento: ")
autorizacion = input("¿Autorización especial vigente? (si/no): ")
hora_ingreso = int(input("Hora de ingreso (0-23): "))

en_horario = hora_ingreso >= 8 and hora_ingreso <= 20
if nivel_acceso == 5 or autorizacion == "si":
    if en_horario:
        print(f"Acceso permitido: Empleado: {empleado_id}, área completamente autorizada.")
    else: 
        print(f"Acceso denegado: Empleado: {empleado_id}, fuera de horario permitido.")
elif nivel_acceso >= 3 and en_horario:
    depto_critico = departamento == "Tecnología" or departamento == "Finanzas" or departamento == "Dirección"
    if depto_critico:
        print(f"ACCESO CONCEDIDO - Empleado: {empleado_id}, área restringida ({departamento}).")
    else:
        print(f"ACCESO PARCIAL - Empleado: {empleado_id}, área general solamente (departamento sin permisos ampliados).")
elif nivel_acceso >= 2 and en_horario:
    print(f"ACCESO CONCEDIDO - Empleado: {empleado_id}, área general solamente.")
elif not en_horario:
    print(f"ACCESO DENEGADO - Empleado: {empleado_id}, fuera de horario permitido. Horario permitido: 8:00 a 20:00.")
else:
    print(f"ACCESO DENEGADO - Empleado: {empleado_id}, nivel de acceso insuficiente.")