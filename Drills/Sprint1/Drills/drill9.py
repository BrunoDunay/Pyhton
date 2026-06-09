# DRILL 4: EL CONVERSOR DE VALENTINA

# TODO 1: Usa input() con float() para pedir la temperatura en Celsius
# y guárdala en una variable llamada 'celsius'.
celsius = float(input("Ingresa la temperatura en Celsius: "))

# TODO 2: Aplica la fórmula de conversión: (celsius * 9/5) + 32
# y guarda el resultado en una variable llamada 'fahrenheit'.
fahrenheit = (celsius * 9/5) + 32

# TODO 3: Usa una f-string para mostrar el resultado.
# Ejemplo de salida:
# "[celsius]°C equivale a [fahrenheit]°F"
print(f"{celsius}°C equivale a {fahrenheit}°F")