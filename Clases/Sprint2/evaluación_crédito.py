
# Una institución financiera necesita un módulo de pre-evaluación crediticia.
# El sistema toma 6 variables de entrada y aplica las reglas de negocio en el orden correcto.

# ── VARIABLES DE ENTRADA ───────────────────────────────────────────────────
#   nombre           → str   (nombre completo del solicitante)
#   ingreso_mensual  → float (ingreso neto mensual en pesos)
#   deuda_mensual    → float (total de pagos de deuda actuales por mes)
#   tipo_empleo      → str   ("permanente" / "contrato" / "independiente" / "desempleado")
#   score_crediticio → int   (score de buró, rango 300-850)
#   antiguedad_años  → int   (años en el empleo actual o en actividad independiente)

# ── CÁLCULOS REQUERIDOS (ANTES de los if) ──────────────────────────────────
#   ratio_deuda      = deuda_mensual / ingreso_mensual
#      (Ejemplo: si ingreso=30,000 y deuda=9,000 → ratio = 0.30 = 30%)
#   capacidad_pago   = ingreso_mensual - deuda_mensual
#      (Cuánto le queda disponible después de pagar deudas actuales)

# ── REGLAS DE NEGOCIO (en este orden exacto) ────────────────────────────────
#   Regla 1: tipo_empleo == "desempleado"
#            → DENEGADO: sin actividad económica activa

#   Regla 2: score_crediticio < 500
#            → DENEGADO: score en rango de alto riesgo

#   Regla 3: ratio_deuda > 0.50
#            → DENEGADO: más del 50% del ingreso comprometido en deudas

#   Regla 4: tipo_empleo == "independiente" AND antiguedad_años < 3
#            → DENEGADO: actividad independiente con menos de 3 años de antigüedad

#   Regla 5: score_crediticio >= 750 AND ratio_deuda <= 0.25 AND tipo_empleo == "permanente"
#            → APROBADO: tasa preferencial (el mejor perfil)

#   Regla 6: score_crediticio >= 600 AND ratio_deuda <= 0.40
#            → APROBADO: tasa estándar

#   Regla 7: score_crediticio >= 500 AND ratio_deuda <= 0.50
#            → PENDIENTE: requiere análisis adicional por un ejecutivo

#   Regla 8 (else): Ninguna condición anterior fue True
#            → DENEGADO: perfil no cumple ningún criterio de aprobación

# ── FORMATO DE SALIDA ───────────────────────────────────────────────────────
#   El mensaje debe incluir: nombre, resultado, y los valores calculados relevantes.
#   Ejemplo: "APROBADO (preferencial) — Ana García | Score: 790 | Ratio deuda: 18.5%"


nombre           = input("Nombre del solicitante: ")
ingreso_mensual  = float(input("Ingreso mensual neto ($): "))
deuda_mensual    = float(input("Deuda mensual total ($): "))
tipo_empleo      = input("Tipo de empleo (permanente/contrato/independiente/desempleado): ")
score_crediticio = int(input("Score crediticio (300-850): "))
antiguedad_años  = float(input("Antigüedad laboral (años): "))

if ingreso_mensual <= 0:
    print(f"DENEGADO — {nombre} | Ingreso mensual no puede ser cero o negativo.")
    exit()

ratio_deuda = deuda_mensual / ingreso_mensual
capacidad_pago = ingreso_mensual - deuda_mensual

if tipo_empleo == "desempleado":
    print(f"DENEGADO — {nombre} | Sin actividad económica activa.")
elif score_crediticio < 500:
    print(f"DENEGADO — {nombre} | Score en rango de alto riesgo: {score_crediticio}.")
elif ratio_deuda > 0.50:
    print(f"DENEGADO — {nombre} | Más del 50% del ingreso comprometido en deudas (Ratio: {ratio_deuda:.2%}).")
elif tipo_empleo == "independiente" and antiguedad_años < 3:
    print(f"DENEGADO — {nombre} | Actividad independiente con menos de 3 años de antigüedad (Antigüedad: {antiguedad_años} años).")
elif score_crediticio >= 750 and ratio_deuda <= 0.25 and tipo_empleo == "permanente":
    print(f"APROBADO (preferencial) — {nombre} | Score: {score_crediticio} | Ratio deuda: {ratio_deuda:.2%}")
elif score_crediticio >= 600 and ratio_deuda <= 0.40:
    print(f"APROBADO (estándar) — {nombre} | Score: {score_crediticio} | Ratio deuda: {ratio_deuda:.2%}")
elif score_crediticio >= 500 and ratio_deuda <= 0.50:
    print(f"PENDIENTE — {nombre} | Score: {score_crediticio} | Ratio deuda: {ratio_deuda:.2%}. Requiere análisis adicional.")
else:    print(f"DENEGADO — {nombre} | Perfil no cumple ningún criterio de aprobación. Score: {score_crediticio} | Ratio deuda: {ratio_deuda:.2%}.")