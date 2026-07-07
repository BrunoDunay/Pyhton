# CALCULADORA CON FUNCIONES


# TODO 1: Importa el módulo math al inicio del archivo
# (lo vas a necesitar para math.ceil y math.floor más abajo).

import math


# ===== DEFINICIÓN DE FUNCIONES =====

# TODO 2: Define una función 'mostrar_bienvenida()' sin parámetros
# que imprima dos líneas: "Bienvenido a la calculadora" y "Versión 1.0".

def mostrar_bienvenida():
    print("Bienvenido a la calculadora")
    print("Versión 1.0")


# TODO 3: Define 'sumar(a, b)' que devuelva (con return) la suma de a y b.

def sumar(a, b):
    return a + b


# TODO 4: Define 'restar(a, b)' que devuelva la resta a - b.

def restar(a, b):
    return a - b


# TODO 5: Define 'dividir(a, b)' que devuelva la división a / b,
# PERO si b es 0, debe devolver el string "Error: División por cero"
# en lugar de intentar la división (evita el ZeroDivisionError).

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


# TODO 6: Define 'calcular_cajas(productos, capacidad)' que devuelva
# cuántas cajas se necesitan para guardar 'productos' unidades si cada
# caja tiene 'capacidad' espacios. Usa math.ceil() sobre la división,
# porque siempre hay que redondear ARRIBA: si te sobra 1 producto,
# necesitas una caja más.

def calcular_cajas(productos, capacidad):
    return math.ceil(productos / capacidad)


# ===== USAR LAS FUNCIONES =====

# TODO 7: Llama a mostrar_bienvenida() para que imprima el encabezado.

mostrar_bienvenida()


# TODO 8: Imprime un subtítulo "=== Operaciones Básicas ===" y luego
# cuatro líneas con f-string que muestren:
#   - sumar(10, 5)
#   - restar(10, 5)
#   - dividir(10, 3)
#   - dividir(10, 0)   ← debe mostrar el mensaje de error sin tronar

print("\n=== Operaciones Básicas ===")
print(f"Suma: {sumar(10, 5)}")
print(f"Resta: {restar(10, 5)}")
print(f"División: {dividir(10, 3)}")
print(f"División entre cero: {dividir(10, 0)}")


# TODO 9: Imprime un subtítulo "=== Redondeo con math ===". Crea una
# variable 'numero = 4.7' y muestra con f-strings:
#   - el valor original
#   - math.ceil(numero)   → debería dar 5
#   - math.floor(numero)  → debería dar 4
#   - int(numero)         → también da 4 (trunca, no redondea)

print("\n=== Redondeo con math ===")

numero = 4.7

print(f"Valor original: {numero}")
print(f"math.ceil(numero): {math.ceil(numero)}")
print(f"math.floor(numero): {math.floor(numero)}")
print(f"int(numero): {int(numero)}")


# TODO 10: Imprime "=== Cálculo de Cajas ===". Define dos variables:
#   productos = 47
#   capacidad_caja = 10
# Llama a calcular_cajas(productos, capacidad_caja) y guarda el resultado
# en 'cajas'. Imprime productos, capacidad y cajas necesarias.
# (Con 47/10 deberías obtener 5 cajas, no 4, porque sobran 7 productos.)

print("\n=== Cálculo de Cajas ===")

productos = 47
capacidad_caja = 10

cajas = calcular_cajas(productos, capacidad_caja)

print(f"Productos: {productos}")
print(f"Capacidad por caja: {capacidad_caja}")
print(f"Cajas necesarias: {cajas}")