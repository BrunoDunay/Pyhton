# DRILL 3: EL RADAR DE LUCÍA

# TODO 1: Crea un diccionario llamado 'medios_acreditados' con tres entradas:
# "Diario del Sur" → True
# "Radio Granado" → True
# "Revista Eco" → True

medios_acreditados = {
    "Diario del Sur": True,
    "Radio Granado": True,
    "Revista Eco": True
}

# TODO 2: Usa input() para pedir el nombre del medio que se quiere verificar
# y guárdalo en una variable llamada 'medio_buscado'.

medio_buscado = input("Ingresa el nombre del medio: ")

# TODO 3: Usa el operador 'in' dentro de un if/else para imprimir:
# - Si la clave existe: "[medio_buscado] ya está acreditado."
# - Si no existe: "[medio_buscado] aún no figura en el registro."

if medio_buscado in medios_acreditados:
    print(f"{medio_buscado} ya está acreditado.")
else:
    print(f"{medio_buscado} aún no figura en el registro.")