# Calculadora Modular con Funciones

print("=== CALCULADORA MODULAR ===\n")

# TODO 1
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # TODO 2
    if b == 0:
        return "Error: división por cero"
    return a / b

# TODO 3
num1 = 20
num2 = 5

print(f"Suma: {num1} + {num2} = {sumar(num1, num2)}")
print(f"Resta: {num1} - {num2} = {restar(num1, num2)}")
print(f"Multiplicación: {num1} * {num2} = {multiplicar(num1, num2)}")
print(f"División: {num1} / {num2} = {dividir(num1, num2)}")

# TODO 4
print(f"División entre cero: {dividir(10, 0)}")

# TODO 5
print(f"Suma reutilizable: 100 + 250 = {sumar(100, 250)}")
print(f"Resta reutilizable: 1000 - 750 = {restar(1000, 750)}")