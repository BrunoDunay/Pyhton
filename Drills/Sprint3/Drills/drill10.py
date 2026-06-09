# DRILL 10: EL CONTEO SELECTIVO DE CHECO

# TODO 1: Crear el acumulador.
contador_aforo = 0

# TODO 2: Recorrer las credenciales del 1 al 20.
for credencial in range(1, 21):

    # Si es múltiplo de 5, es cortesía y se ignora.
    if credencial % 5 == 0:
        continue

    # Contar solo las credenciales válidas.
    contador_aforo += 1
    print(f"Credencial {credencial} contada -- aforo actual {contador_aforo}")

# TODO 3: Imprimir el resultado final.
print(f"Aforo oficial del día: {contador_aforo} personas (cortesías excluidas).")