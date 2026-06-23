incidencias = [
    "caida del servidor",
    "fuga de datos",
    "ticket vencido",
    "backup fallido",
    "permiso de firma"]

prioridades = [
    "crítica",
    "crítica", 
    "media",
    "alta",
    "baja"
]

horas = [ 8, 12, 3, 6, 1]

print("========= Incidencias Pendientes =========")

numero = 1

for incidencia in incidencias:
    print(f"{numero}. {incidencia}")
    numero += 1

print("\n========= Solo críticas =========")

posicion = 0

for incidencia in incidencias:
    if prioridades[posicion] == "crítica":
        print(f"[!] {incidencia}")
    posicion += 1


