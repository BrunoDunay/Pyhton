# DRILL 4: LA PRIMERA RECETA DE SOFÍA

# TODO 1: Define una función llamada 'saludo_festival' que reciba
# un parámetro llamado 'nombre' y un parámetro llamado 'rol'.

def saludo_festival(nombre, rol):

    # TODO 2: Dentro de la función, imprime un mensaje formateado:
    # "🎪 Bienvenido al equipo, [nombre]. Tu rol: [rol]."

    print(f"🎪 Bienvenido al equipo, {nombre}. Tu rol: {rol}.")


# TODO 3: Llama a la función tres veces, con datos distintos:
#   - "Daniela", "Productora artística"
#   - "Mateo", "Responsable de sonido"
#   - "Lucía", "Encargada de prensa"

saludo_festival("Daniela", "Productora artística")
saludo_festival("Mateo", "Responsable de sonido")
saludo_festival("Lucía", "Encargada de prensa")


# TODO 4: Define una función llamada 'calcular_anos_festival' que reciba
# un parámetro 'anio_actual' y retorne (con return) el resultado de
# anio_actual - 2001.

def calcular_anos_festival(anio_actual):
    return anio_actual - 2001


# TODO 5: Llama a la función con 2026 y guarda el resultado en una variable
# llamada 'aniversario'. Imprime: "El festival cumple [aniversario] años."

aniversario = calcular_anos_festival(2026)
print(f"El festival cumple {aniversario} años.")