# DRILL 1: DANIELA RECORRE EL CARTEL

cartel = [
  "Los Granados",
  "Cardumen",
  "La Sierra",
  "Espuma Fría",
  "Aurora Doble",
  "Vento Sur"
]

# TODO 1: Usa un bucle 'for' que recorra cada banda de la lista 'cartel'.

for banda in cartel:

    # TODO 2: Dentro del bucle, imprime un mensaje formateado por banda:
    # "🎵 [banda] toca en SonidoLibre 2026"

    print(f"🎵 {banda} toca en SonidoLibre 2026")


# TODO 3: Después del bucle (sin indentación), imprime un cierre:
# "Total de anuncios generados: [N]"
# donde [N] es el resultado de len(cartel).

print(f"Total de anuncios generados: {len(cartel)}")