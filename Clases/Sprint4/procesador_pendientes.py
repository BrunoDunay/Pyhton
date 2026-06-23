import math
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

print("========= Backlog completo =========")

numero = 1
posicion = 0
total_horas = 0
total_criticas = 0
total_altas = 0
total_medias = 0
total_bajas = 0
total_inc = len(incidencias)
por_dia = 4

for incidencia in incidencias:
    print(f"{numero}. {incidencia}")
    total_horas += horas[posicion]

    if prioridades[posicion] == "crítica":
        total_criticas += horas[posicion]

    elif prioridades[posicion] == "alta":
        total_altas += horas[posicion]
    
    elif prioridades[posicion] == "media":
        total_medias += horas[posicion]
    
    elif prioridades[posicion] == "baja":
        total_bajas += horas[posicion]

    numero += 1
    posicion += 1

print(f"\nTotal de horas: {total_horas}")
print(f"Total de horas críticas: {total_criticas}")
print(f"Total de horas altas: {total_altas}")
print(f"Total de horas medias: {total_medias}")
print(f"Total de horas bajas: {total_bajas}")

incidencias_ordenadas = sorted(incidencias)

print("\n========= ORDEN DE CAPTURA =========")

dias_minimos = math.ceil(total_inc / por_dia)
print(F"Incidencias: {total_inc} | Días hábiles mínimos: {dias_minimos}")

print(f"floor({total_inc} / {por_dia}) = {math.floor(total_inc / por_dia)}")

print(f"ceil({total_inc} / {por_dia}) = {math.ceil(total_inc / por_dia)}")
