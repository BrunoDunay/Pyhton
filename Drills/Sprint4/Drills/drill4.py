# DRILL 4: EL RADAR DE LUCÍA

cartel_oficial = [
    "Los Granados",
    "Cardumen",
    "La Sierra",
    "Espuma Fría",
    "Mareas Altas"
]

# TODO 1
consulta = input("Ingresa el nombre de una banda: ")

# TODO 2
if consulta in cartel_oficial:
    print(f"Confirmado: {consulta} toca en SonidoLibre.")
else:
    print(f"{consulta} no figura en el cartel oficial.")