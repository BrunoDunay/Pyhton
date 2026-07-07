# Recursos Humanos imprime gafetes para los reclutas nuevos.
# El sistema de registro les manda UNA línea de texto por persona, con los tres campos
# separados por comas... y capturada como la capturó un humano 
# con prisa:

pythonregistro_crudo = "  MARA   ibarra ,  saLUD  , 133750.5  "

# Tu programa debe imprimir el gafete limpio y formateado, # exactamente así:

# ==================================================
#  NOMBRE:   Mara Ibarra
#  AREA:   Salud
#  SALARIO:   133,750.50
# ==================================================

pythonregistro = pythonregistro_crudo.strip()  # Elimina espacios al inicio y al final
partes = pythonregistro.split(",")  # Separa los campos por comas
nombre = partes[0].strip().title()  # Limpia y formatea el nombre
nombre_limpio = nombre.replace("   ", " ")  # Quita los espacios
area = partes[1].strip().title()  # Limpia y formatea el área
salario = float(partes[2].strip())  # Limpia y convierte el salario a float

print("==================================================")
print(f" NOMBRE: {nombre_limpio}")
print(f" AREA: {area}")
print(f" SALARIO: {salario:,.2f}")
print("==================================================")