# DRILL 2: CORTAR Y UNIR — MATEO PROCESA EL WHATSAPP

# TODO 1: Crear la variable con el mensaje
mensaje_whatsapp = "Los Granados,Cardumen,La Sierra,Espuma Fría"

# TODO 2: Separar el texto en una lista usando split()
bandas = mensaje_whatsapp.split(",")

# TODO 3: Imprimir la lista completa
print(bandas)

# TODO 4: Imprimir cuántas bandas hay
print(f"Hay {len(bandas)} bandas.")

# TODO 5: Unir la lista con " | " como separador
cartel_formateado = " | ".join(bandas)

# Imprimir el resultado
print(cartel_formateado)