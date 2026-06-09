print("=" * 40)
print("CONVERSOR DE TEMPERATURA")
print("=" * 40)

ciudad = input("¿En qué ciudad estás? :")
celcius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15


print(f"En {ciudad}, {celcius}°C equivale a {fahrenheit:.2f}°F")
print(f"En {ciudad}, {celcius}°C equivale a {kelvin:.2f}K")
print("=" * 40)
