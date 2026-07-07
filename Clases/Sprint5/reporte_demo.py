base_reclutas = [
    {"nombre": "Ana Torres", "area": "Finanzas", "salario_mensual": 28500.0},
    {"nombre": "Luis Quintero", "area": "Logística", "salario_mensual": 19200.0},
    {"nombre": "Mara Ibarra", "area": "Salud", "salario_mensual": 133750.0},
]

print("==== FASE 1: ====")
for recluta in base_reclutas:
    print(f"{recluta['nombre']}, {recluta['area']}, {recluta['salario_mensual']}")

print()
print("==== FASE 2: ====")
for recluta in base_reclutas:
    print(f"{recluta['nombre']:<5} | {recluta['area']:<5} | {recluta['salario_mensual']:<5}")