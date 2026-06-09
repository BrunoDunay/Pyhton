# BUSCADOR DE NÚMEROS PARES

# TODO 1: Crear la lista.
numeros = [1, 3, 5, 7, 8, 11, 13, 16, 19]

# === PARTE 1: Encontrar el primer par usando break ===

# TODO 2: Imprimir mensaje inicial.
print("Buscando el primer número par...")

# TODO 3: Recorrer la lista y detenerse al encontrar el primer par.
for num in numeros:
    print(f"Revisando {num}...")

    if num % 2 == 0:
        print(f"¡Encontrado! El primer par es {num}")
        break

# === PARTE 2: Imprimir solo los impares usando continue ===

# TODO 4: Encabezado.
print("Números impares de la lista:")

# TODO 5: Recorrer la lista e imprimir solo los impares.
for num in numeros:
    if num % 2 == 0:
        continue

    print(num)