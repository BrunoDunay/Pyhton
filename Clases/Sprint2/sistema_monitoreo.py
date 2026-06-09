#Sistema de monitoreo SLA -> Contiene 3 niveles de atención a clientes

tipo_incidente = input("Ingrese el tipo de incidente (Crítico, Alto, Medio): ").upper()
tiempo_respuesta = int(input("Ingrese el tiempo de respuesta en horas: "))
cliente_premium = input("¿El cliente es premium? (si/no): ").upper()

if tipo_incidente == "CRÍTICO":
    if tiempo_respuesta <= 15:
        print("SLA cumplido...")
    else:
        if cliente_premium == "SI":
            print("SLA Cliente premium - escalar ...")
        else: 
            print("SLA: Notificar al cliente...")
elif tipo_incidente == "ALTO":
    if tiempo_respuesta <= 60:
        print("SLA cumplido, Alta prioridad...")
    else:
        print("SLA: Notificar al supervisor...")
else:
    print("SLA: Incidente de prioridad media, seguimiento estándar...")