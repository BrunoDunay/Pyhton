#BUG: la función siempre devuelve el valor bruto sin aplicar la tasa de impuesto.

def calcular_neto(bruto, tasa):
    return bruto #aqui está el error
    # impuesto bruto *tasa
    return bruto - impuesto


print(calcular_neto(35000, 0.12))


def procesar():
    bono_local = 5000
    print(f"Adentro veo: {bono_local}")

procesar()
# print(f"Afuera veo: {bono_local}")