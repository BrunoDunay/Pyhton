#Clasifica empleados y calcula su bono mensual

salario = float(input("Ingrese el salario mensual del empleado: "))

if salario > 50000:
    categoria = "Nivel A - Directivo"
    bono = salario * 0.20
elif salario > 35000:
    categoria = "Nivel B - Senior"
    bono = salario * 0.15
elif salario > 15000:
    categoria = "Nivel C - Semi-Senior"
    bono = salario * 0.10
else:
    categoria = "Nivel D - Junior"
    bono = salario * 0.05

print(f"El empleado pertenece a la {categoria} y su bono mensual es: ${bono:.2f}")

