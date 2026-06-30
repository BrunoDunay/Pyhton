# CONTEXTO: Expediente Digital de Empleado
# RRHH está migrando los expedientes de papel a un sistema en consola.
# Cada empleado es un expediente con campos rotulados. Hoy construimos
# el manejo de UN expediente; la próxima fase será el directorio completo.

# Campos del expediente:
#   · nombre            (str)
#   · departamento      (str)
#   · salario_mensual   (float)
#   · nivel_acceso      (int, 1-5)
#   · activo            (str: "si"/"no")

# Archivo: expediente_empleado.py

empleado = {
    "nombre" : "Ana García", 
    "departamento" : "Finanzas", 
    "salario_mensual": 45000.0, 
    "nivel_acceso": 4, 
    "activo": "si" 
    }

for clave, valor in empleado.items():
    print(clave, "->", valor)

empleado["salario_mensual"] = empleado["salario_mensual"] * 1.10
print("Salario tras aumento: ", empleado["salario_mensual"])