# DRILL 3: LA CANCELACIÓN DE ÚLTIMO MINUTO

bandas_confirmadas = [
    "Los Granados",
    "Cardumen",
    "La Sierra",
    "Voltio Norte",
    "Mareas Altas"
]

# TODO 1
bandas_confirmadas.remove("Voltio Norte")

# TODO 2
bandas_confirmadas.insert(3, "Espuma Fría")

# TODO 3
print(bandas_confirmadas)

# TODO 4
banda_retirada = bandas_confirmadas.pop()

# TODO 5
print(f"Banda retirada del cartel: {banda_retirada}")
print("Lista final:", bandas_confirmadas)